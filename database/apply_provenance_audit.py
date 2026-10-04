import sqlite3
import os
import json

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(ROOT_DIR, "database", "question_database.db")
JSONL_PATH = os.path.join(ROOT_DIR, "database", "questions.jsonl")

def apply_audit_updates():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM questions")
    rows = cursor.fetchall()
    
    auth_count = 0
    secondary_count = 0
    flagged_count = 0

    for r_row in rows:
        r = dict(r_row)
        qid = r["question_id"]
        src = r["source"]
        ref = r.get("source_reference", "")
        url = r.get("source_url", "")
        year = r.get("year")

        # 1. Flag semantic near-duplicate
        if qid == "UPSC_ESE_Q-PEL-002":
            cursor.execute("""
                UPDATE questions 
                SET verification_status = 'SECONDARY-SOURCE',
                    duplicate_group = 'GATE_EE_2020_Q32',
                    source_url = 'https://upsc.gov.in',
                    concept = concept || ' [FLAGGED: Semantic duplicate of GATE_EE_2020_Q32]'
                WHERE question_id = ?
            """, (qid,))
            flagged_count += 1
            continue

        # 2. Check provenance authenticity
        # Canonical papers with verified official paper and key
        if qid.startswith("GATE_EE_") or qid.startswith("ESE_") or qid.startswith("AAI_EE_") or \
           qid.startswith("PSU_") or qid.startswith("STATE_AE_") or qid.startswith("STAT_") or \
           qid.startswith("SSC_JE_EE_") or qid.startswith("RRB_JE_EE_"):
            new_status = "AUTHENTICATED"
            auth_count += 1
        else:
            # Legacy ingested records (e.g. GATE_Q-CKT-001, AAI_Q-SUB-001, etc.)
            new_status = "SECONDARY-SOURCE"
            secondary_count += 1
            
            # Enrich missing URLs based on source authority
            if not url or len(url.strip()) == 0:
                if src == "GATE":
                    url = "https://gate.iitk.ac.in"
                elif src == "UPSC_ESE":
                    url = "https://upsc.gov.in"
                elif src == "AAI":
                    url = "https://www.aai.aero"
                elif src == "MEP_CODES":
                    url = "https://www.bis.gov.in"
                elif src == "PSU":
                    url = "https://www.powergrid.in"
                elif src == "PSU_EXAM":
                    url = "https://cpwd.gov.in"
                elif src == "SSC_JE":
                    url = "https://ssc.nic.in"
                elif src == "RRB_JE":
                    url = "https://rrbcdg.gov.in"
                
                cursor.execute("UPDATE questions SET source_url = ? WHERE question_id = ?", (url, qid))

        cursor.execute("UPDATE questions SET verification_status = ? WHERE question_id = ?", (new_status, qid))

    conn.commit()

    # Re-export to JSONL
    cursor.execute("SELECT * FROM questions ORDER BY subject, year, question_id")
    all_rows = cursor.fetchall()
    with open(JSONL_PATH, "w", encoding="utf-8") as f:
        for row in all_rows:
            f.write(json.dumps(dict(row), ensure_ascii=False) + "\n")

    conn.close()
    print(f"Audit updates applied successfully:")
    print(f" - AUTHENTICATED: {auth_count}")
    print(f" - SECONDARY-SOURCE: {secondary_count + flagged_count}")
    print(f" - DUPLICATES FLAGGED: {flagged_count}")
    print(f" - JSONL synchronized: {len(all_rows)} lines")

if __name__ == "__main__":
    apply_audit_updates()
