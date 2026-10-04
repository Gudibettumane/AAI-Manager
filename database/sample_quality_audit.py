import sqlite3
import json
import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(ROOT_DIR, "database", "question_database.db")

SAMPLE_IDS = [
    # 1. GATE (IITs)
    "GATE_EE_2022_Q14",   # Critical damping series RLC
    "GATE_EE_2020_Q38",   # Induction motor slip at max torque
    "GATE_EE_2018_Q14",   # MI meter true RMS calculation

    # 2. UPSC ESE (Prelims EE & GS)
    "ESE_GS_2022_Q12",    # PERT expected time and variance
    "ESE_EE_2022_Q35",    # Open-Delta V-V transformer capacity
    "ESE_EE_2021_Q74",    # Dual-trace vs Dual-beam CRO

    # 3. AAI (Manager & JE CBT)
    "AAI_EE_2021_Q48",    # Taxiway edge & threshold light colors
    "AAI_EE_2021_Q52",    # Airfield 6.6A series loop CCR
    "AAI_EE_2022_PAPI_07",# PAPI 2W 2R glide slope indication

    # 4. MEP_CODES (Statutory Standards)
    "STAT_NBC_FIRE_03",   # Sprinkler glass bulb 68 deg C Red
    "STAT_IS_LIFTS_04",   # Lift overspeed governor 115% tripping
    "STAT_BEE_HVAC_05",   # Cooling tower Range and Approach

    # 5. Central PSUs (PGCIL, NTPC, BHEL, ISRO)
    "PSU_PGCIL_2021_Q15", # Tower footing resistance <= 10 ohms
    "PSU_BHEL_2020_Q22",  # Hydrogen cooling in turbo-generators
    "PSU_ISRO_2020_Q19",  # Satellite MPPT converter principle

    # 6. State AE / Other PSUs
    "STATE_AE_UPPCL_2021_Q21", # SF6 arc quenching properties
    "STATE_AE_KPTCL_2020_Q38", # Cable capacitance grading
    "PSU_EXAM_Q-SUB-002",      # Legacy CPWD transformer impedance

    # 7. SSC JE
    "SSC_JE_EE_2020_Q14", # Sine wave form factor 1.11, crest 1.414
    "SSC_JE_EE_2019_Q28", # Wave winding dummy coils
    "SSC_JE_EE_2018_Q62", # Maintenance factor * Depreciation factor = 1

    # 8. RRB JE
    "RRB_JE_EE_2019_Q45", # Fusing factor > 1.0 definition
    "RRB_JE_EE_2019_Q11"  # Resistance temperature coefficient
]

def audit_sample():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sample_results = []
    
    for qid in SAMPLE_IDS:
        cursor.execute("SELECT * FROM questions WHERE question_id = ?", (qid,))
        row = cursor.fetchone()
        if not row:
            sample_results.append({"question_id": qid, "status": "NOT_FOUND"})
            continue
        
        q = dict(row)
        
        # Verify question mechanics
        options = [q["option_A"], q["option_B"], q["option_C"], q["option_D"]]
        has_all_options = all(opt and len(opt.strip()) > 0 for opt in options)
        unique_options = len(set(opt.strip().lower() for opt in options)) == 4
        valid_answer = q["verified_answer"] in ["A", "B", "C", "D"]
        keys_match = (q["official_answer"] == q["verified_answer"])
        has_solution = bool(q["solution"] and len(q["solution"].strip()) > 30)

        # Provenance check
        has_paper = bool(q.get("paper"))
        has_year = bool(q.get("year"))
        has_source_ref = bool(q.get("source_reference"))
        has_url = bool(q.get("source_url"))

        sample_results.append({
            "question_id": qid,
            "source": q["source"],
            "exam": q["exam"],
            "year": q["year"],
            "subject": q["subject"],
            "topic": q["topic"],
            "has_all_options": has_all_options,
            "unique_options": unique_options,
            "valid_answer": valid_answer,
            "keys_match": keys_match,
            "verified_answer": q["verified_answer"],
            "has_solution": has_solution,
            "has_year": has_year,
            "has_url": has_url,
            "source_reference": q["source_reference"],
            "solution_snippet": q["solution"][:100] + "...",
            "audit_verdict": "VERIFIED_CORRECT" if (has_all_options and unique_options and valid_answer and keys_match and has_solution) else "NEEDS_ATTENTION"
        })

    conn.close()
    
    with open(os.path.join(ROOT_DIR, "database", "sample_audit_results.json"), "w", encoding="utf-8") as f:
        json.dump(sample_results, f, indent=2)

    print(f"Sample audit finished for {len(sample_results)} questions.")
    return sample_results

if __name__ == "__main__":
    audit_sample()
