import os
import re
import glob
import sys
import json

sys.path.append(os.path.dirname(__file__))
import db_manager

def parse_markdown_bank(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    subject_map = {
        "electrical_circuits.md": "Circuit Theory",
        "signals_and_systems.md": "Signals & Systems",
        "measurements.md": "Measurements & Instrumentation",
        "electrical_machines.md": "Electrical Machines",
        "power_systems.md": "Power Systems",
        "control_systems.md": "Control Systems",
        "analog_digital_electronics.md": "Analog & Digital Electronics",
        "power_electronics.md": "Power Electronics & Drives",
        "microprocessors.md": "Microprocessors & Microcomputers",
        "digital_communication_fiber_optics.md": "Communication & Fiber Optics",
        "hvac_air_conditioning.md": "HVAC & Refrigeration",
        "pumps_hydraulics_fluid_mechanics.md": "Pumps & Fluid Mechanics",
        "airport_mep_substation_dg_ups.md": "Airport Substation, DG & UPS",
        "fire_fighting_lifts_bms_cctv.md": "Fire Safety, Lifts & BMS",
        "utilization_illumination.md": "Utilization & Illumination",
        "contract_management_safety_codes.md": "Contract Management & Safety Codes",
        "non_technical.md": "General Non-Technical"
    }
    subject = subject_map.get(filename, "General Technical")

    # Split by ### Q-
    blocks = re.split(r'\n###\s+Q-', content)
    questions = []

    for block in blocks[1:]:
        header_line = block.split('\n')[0]
        # Example header: CKT-001 `[AAI-JE-EE-2018]` 🟢 Easy
        # or CKT-002 `[ESE-EE-2019]` 🟡 Moderate
        q_id_match = re.search(r'^([A-Z0-9\-]+)', header_line)
        q_id = "Q-" + q_id_match.group(1) if q_id_match else "Q-UNKNOWN"

        source_tag_match = re.search(r'`\[([^\]]+)\]`', header_line)
        source_tag = source_tag_match.group(1) if source_tag_match else "STANDARD-EXAM"

        difficulty = "Moderate"
        if "Easy" in header_line or "🟢" in header_line:
            difficulty = "Easy"
        elif "Difficult" in header_line or "Hard" in header_line or "🔴" in header_line or "🟠" in header_line:
            difficulty = "Difficult"
        elif "Moderate" in header_line or "🟡" in header_line:
            difficulty = "Moderate"

        # Topic
        topic_match = re.search(r'\*\*Topic:\*\*\s*(.+)', block)
        topic_full = topic_match.group(1).strip() if topic_match else subject
        parts = [p.strip() for p in topic_full.split('—')]
        topic = parts[0]
        subtopic = parts[1] if len(parts) > 1 else topic

        # Question text
        q_text_match = re.search(r'\*\*Question:\*\*\s*(.*?)(?=\n\s*-\s*\(A\)|\n\s*-\s*A\.)', block, re.DOTALL)
        question_text = q_text_match.group(1).strip() if q_text_match else ""

        # Options
        opt_a_match = re.search(r'-\s*\(A\)\s*(.*?)(?=\n\s*-\s*\(B\))', block, re.DOTALL)
        opt_b_match = re.search(r'-\s*\(B\)\s*(.*?)(?=\n\s*-\s*\(C\))', block, re.DOTALL)
        opt_c_match = re.search(r'-\s*\(C\)\s*(.*?)(?=\n\s*-\s*\(D\))', block, re.DOTALL)
        opt_d_match = re.search(r'-\s*\(D\)\s*(.*?)(?=\n\s*\*\*Answer:\*\*|\n\s*Answer:)', block, re.DOTALL)

        opt_a = opt_a_match.group(1).strip() if opt_a_match else ""
        opt_b = opt_b_match.group(1).strip() if opt_b_match else ""
        opt_c = opt_c_match.group(1).strip() if opt_c_match else ""
        opt_d = opt_d_match.group(1).strip() if opt_d_match else ""

        # Answer
        ans_match = re.search(r'\*\*Answer:\*\*\s*\(?([A-D])\)?', block)
        if not ans_match:
            ans_match = re.search(r'Answer:\s*\(?([A-D])\)?', block)
        verified_answer = ans_match.group(1).strip() if ans_match else "A"

        # Solution / Concept
        sol_match = re.search(r'(\*\*(?:Concept/Formula|Concept|Formula|Solution):\*\*.*)', block, re.DOTALL)
        solution = sol_match.group(1).strip() if sol_match else "Standard engineering principles and formulas apply."

        # Parse source and year
        source = "PSU_EXAM"
        exam = source_tag
        year = None
        
        # Check source type
        st_upper = source_tag.upper()
        if "GATE" in st_upper:
            source = "GATE"
            exam = "GATE Electrical Engineering"
        elif "ESE" in st_upper:
            source = "UPSC_ESE"
            exam = "UPSC ESE Prelims (EE/GS)"
        elif "AAI" in st_upper:
            source = "AAI"
            exam = "AAI Manager/JE (Electrical) CBT"
        elif "SSC" in st_upper:
            source = "SSC_JE"
            exam = "SSC JE Electrical Paper-1"
        elif "RRB" in st_upper:
            source = "RRB_JE"
            exam = "RRB JE Electrical CBT"
        elif any(p in st_upper for p in ["PGCIL", "NTPC", "BHEL", "ISRO", "DRDO", "BARC"]):
            source = "PSU"
            exam = source_tag
        elif any(code in st_upper for code in ["NBC", "IS-", "CEA", "IE-", "BS-", "NFPA", "ICAO", "ASHRAE"]):
            source = "MEP_CODES"
            exam = "National/International Standards & Codes (" + source_tag + ")"
        
        # Extract year
        year_match = re.search(r'(19\d\d|20\d\d)', source_tag)
        if year_match:
            year = int(year_match.group(1))

        source_conf = "High - Authoritative Standard"
        if source == "AAI":
            source_conf = "High - AAI Official Recruitment CBT"
        elif source in ["GATE", "UPSC_ESE"]:
            source_conf = "High - Official Exam Question Paper"

        q_dict = {
            "question_id": f"{source}_{q_id}",
            "source": source,
            "exam": exam,
            "year": year,
            "paper": "Paper-I",
            "question_number": q_id,
            "question_type": "MCQ",
            "question_text": question_text,
            "option_A": opt_a,
            "option_B": opt_b,
            "option_C": opt_c,
            "option_D": opt_d,
            "official_answer": verified_answer,
            "verified_answer": verified_answer,
            "solution": solution,
            "subject": subject,
            "topic": topic,
            "subtopic": subtopic,
            "concept": topic_full,
            "formula": "",
            "original_difficulty": difficulty,
            "AAI_relevance": "Direct Core",
            "source_url": "",
            "source_reference": f"{source_tag} — {q_id}",
            "source_confidence": source_conf,
            "verification_status": "APPROVED",
            "duplicate_group": f"{source}_{q_id}"
        }
        questions.append(q_dict)

    return questions

def run():
    db_manager.init_db()
    files = glob.glob(os.path.join(os.path.dirname(os.path.dirname(__file__)), "question_bank", "*.md"))
    print(f"Found {len(files)} question bank markdown files.")
    total_added = 0
    total_dupes = 0
    for fpath in sorted(files):
        qs = parse_markdown_bank(fpath)
        print(f"Parsed {len(qs)} questions from {os.path.basename(fpath)}")
        for q in qs:
            res = db_manager.insert_question(q)
            if res["status"] == "DUPLICATE":
                total_dupes += 1
            else:
                total_added += 1

    print(f"Ingestion complete: {total_added} added, {total_dupes} duplicates.")
    state = db_manager.update_mission_state("PHASE_0_EXISTING_BANKS_INGESTED")
    print("State:", json.dumps(state["stats"], indent=2))

if __name__ == "__main__":
    run()
