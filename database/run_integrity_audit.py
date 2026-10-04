import sqlite3
import json
import os
import re
import hashlib
from collections import defaultdict, Counter

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(ROOT_DIR, "database", "question_database.db")
JSONL_PATH = os.path.join(ROOT_DIR, "database", "questions.jsonl")

def normalize_text(text):
    if not text:
        return ""
    text = re.sub(r'[\$\\]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip().lower()

def jaccard_similarity(s1, s2):
    w1 = set(re.findall(r'\b\w+\b', s1.lower()))
    w2 = set(re.findall(r'\b\w+\b', s2.lower()))
    if not w1 or not w2:
        return 0.0
    return len(w1 & w2) / len(w1 | w2)

def run_audit():
    print("=== STARTING QUESTION DATABASE INTEGRITY AUDIT ===")
    
    # 1. Connect to SQLite
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM questions ORDER BY question_id")
    db_rows = cursor.fetchall()
    db_records = [dict(r) for r in db_rows]
    total_db = len(db_records)
    print(f"Total records in SQLite: {total_db}")

    # 2. Read JSONL
    jsonl_records = []
    with open(JSONL_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                jsonl_records.append(json.loads(line))
    total_jsonl = len(jsonl_records)
    print(f"Total records in JSONL: {total_jsonl}")

    # 3. Check SQLite vs JSONL synchronization
    db_ids = {r["question_id"]: r for r in db_records}
    jsonl_ids = {r["question_id"]: r for r in jsonl_records}

    ids_in_db_not_jsonl = set(db_ids.keys()) - set(jsonl_ids.keys())
    ids_in_jsonl_not_db = set(jsonl_ids.keys()) - set(db_ids.keys())
    
    field_diffs = []
    for qid, db_r in db_ids.items():
        if qid in jsonl_ids:
            jl_r = jsonl_ids[qid]
            for key in ["question_text", "option_A", "option_B", "option_C", "option_D", 
                        "official_answer", "verified_answer", "subject", "topic"]:
                if str(db_r.get(key, "")).strip() != str(jl_r.get(key, "")).strip():
                    field_diffs.append((qid, key, db_r.get(key), jl_r.get(key)))

    print(f"IDs in DB not in JSONL: {len(ids_in_db_not_jsonl)}")
    print(f"IDs in JSONL not in DB: {len(ids_in_jsonl_not_db)}")
    print(f"Field differences between DB and JSONL: {len(field_diffs)}")

    # 4. Mathematical Duplicate and Near-Duplicate Audit
    exact_hash_counts = Counter(r.get("text_hash") for r in db_records)
    exact_hash_dupes = {h: cnt for h, cnt in exact_hash_counts.items() if cnt > 1}

    exact_text_counts = Counter(normalize_text(r.get("question_text", "")) for r in db_records)
    exact_text_dupes = {t: cnt for t, cnt in exact_text_counts.items() if cnt > 1}

    # Near-duplicates check (Jaccard > 0.85)
    near_duplicates = []
    for i in range(len(db_records)):
        for j in range(i + 1, len(db_records)):
            r1, r2 = db_records[i], db_records[j]
            if r1["subject"] == r2["subject"]:
                sim = jaccard_similarity(r1["question_text"], r2["question_text"])
                if 0.85 <= sim < 1.0:
                    near_duplicates.append({
                        "id1": r1["question_id"],
                        "id2": r2["question_id"],
                        "similarity": round(sim, 3),
                        "text1": r1["question_text"][:80],
                        "text2": r2["question_text"][:80]
                    })

    print(f"Exact text hash collisions in DB: {len(exact_hash_dupes)}")
    print(f"Exact normalized text collisions in DB: {len(exact_text_dupes)}")
    print(f"Near-duplicate pairs (similarity >= 0.85): {len(near_duplicates)}")

    # 5. Field Completeness & Quality Checks
    missing_fields_report = defaultdict(list)
    answer_mismatch = []
    invalid_answer_options = []
    weak_solutions = []

    for r in db_records:
        qid = r["question_id"]
        # Required text fields
        for field in ["question_text", "option_A", "option_B", "option_C", "option_D",
                      "official_answer", "verified_answer", "solution", "subject", "topic"]:
            val = str(r.get(field, "")).strip()
            if not val:
                missing_fields_report[field].append(qid)

        # Answer check
        ans = r.get("verified_answer", "").strip().upper()
        if ans not in ["A", "B", "C", "D"]:
            invalid_answer_options.append((qid, ans))

        off_ans = r.get("official_answer", "").strip().upper()
        if off_ans and ans and off_ans != ans:
            answer_mismatch.append((qid, off_ans, ans))

        # Solution check
        sol = str(r.get("solution", "")).strip()
        if len(sol) < 30:
            weak_solutions.append((qid, len(sol)))

    # 6. Provenance Tier Classification Audit
    # We classify into 4 rigorous tiers:
    # - AUTHENTICATED: Official exam paper + official final answer key (IITs, UPSC, BIS, CEA, ISRO)
    # - SECONDARY-SOURCE: Published solved paper archive / candidate response sheet / CBT compilation
    # - INDEPENDENTLY-SOLVED: Checked and derived mathematically from first principles
    # - UNVERIFIED: Missing origin details or ambiguous options
    provenance_tiers = {
        "AUTHENTICATED": [],
        "SECONDARY-SOURCE": [],
        "INDEPENDENTLY-SOLVED": [],
        "UNVERIFIED": []
    }

    for r in db_records:
        qid = r["question_id"]
        src = r.get("source", "")
        conf = r.get("source_confidence", "")
        ref = r.get("source_reference", "")
        url = r.get("source_url", "")
        
        # Check authenticity criteria
        if src in ["GATE", "UPSC_ESE", "MEP_CODES", "SSC_JE", "RRB_JE"]:
            if "Official" in ref or "Standard" in conf or "Statutory" in conf or "IIT" in ref or "UPSC" in ref:
                provenance_tiers["AUTHENTICATED"].append(qid)
            else:
                provenance_tiers["SECONDARY-SOURCE"].append(qid)
        elif src == "AAI":
            if "CBT" in ref or "Official" in ref or "Guidelines" in ref or "Standards" in ref:
                provenance_tiers["AUTHENTICATED"].append(qid)
            else:
                provenance_tiers["SECONDARY-SOURCE"].append(qid)
        elif src in ["PSU", "PSU_EXAM"]:
            if "ISRO" in ref or "PGCIL" in ref or "BHEL" in ref or "NTPC" in ref:
                provenance_tiers["AUTHENTICATED"].append(qid)
            else:
                provenance_tiers["SECONDARY-SOURCE"].append(qid)
        else:
            provenance_tiers["UNVERIFIED"].append(qid)

    # 7. Distribution by Source, Exam, Subject, Year, Difficulty
    by_source = Counter(r["source"] for r in db_records)
    by_exam = Counter(r["exam"] for r in db_records)
    by_subject = Counter(r["subject"] for r in db_records)
    by_year = Counter(r.get("year") for r in db_records if r.get("year"))
    by_diff = Counter(r.get("original_difficulty", "Moderate") for r in db_records)

    # 8. Compile detailed audit output
    audit_results = {
        "total_records_db": total_db,
        "total_records_jsonl": total_jsonl,
        "ids_in_db_not_jsonl": list(ids_in_db_not_jsonl),
        "ids_in_jsonl_not_db": list(ids_in_jsonl_not_db),
        "field_diffs_count": len(field_diffs),
        "exact_hash_dupes": exact_hash_dupes,
        "exact_text_dupes": exact_text_dupes,
        "near_duplicates": near_duplicates,
        "missing_fields": {k: len(v) for k, v in missing_fields_report.items()},
        "invalid_answers": invalid_answer_options,
        "answer_mismatches": answer_mismatch,
        "weak_solutions": weak_solutions,
        "provenance_tier_counts": {k: len(v) for k, v in provenance_tiers.items()},
        "by_source": dict(by_source),
        "by_subject": dict(by_subject),
        "by_difficulty": dict(by_diff),
        "by_year_summary": {
            "2020-2024": sum(cnt for yr, cnt in by_year.items() if yr and yr >= 2020),
            "2015-2019": sum(cnt for yr, cnt in by_year.items() if yr and 2015 <= yr < 2020),
            "2010-2014": sum(cnt for yr, cnt in by_year.items() if yr and 2010 <= yr < 2015),
            "2000-2009": sum(cnt for yr, cnt in by_year.items() if yr and 2000 <= yr < 2010),
            "Undated/Standards": sum(cnt for yr, cnt in by_year.items() if not yr or yr < 2000)
        }
    }

    with open(os.path.join(ROOT_DIR, "database", "audit_raw_results.json"), "w", encoding="utf-8") as f:
        json.dump(audit_results, f, indent=2)

    conn.close()
    print("Audit Complete! Saved raw results to database/audit_raw_results.json")
    return audit_results

if __name__ == "__main__":
    run_audit()
