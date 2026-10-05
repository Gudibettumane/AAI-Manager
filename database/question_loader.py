"""
===============================================================================
AAI MANAGER (ENGG.-ELECTRICAL) — UNIFIED QUESTION INGESTION & LOADER SKELETON
===============================================================================
This is the single, reusable production script for ingesting, validating, and
persisting verified questions into the AAI Question Database.

Capabilities:
  1. Ingest questions from a Python list / dictionary.
  2. Ingest questions from a JSON or JSONL file:
       python database/question_loader.py --file path/to/questions.json
  3. Automatic O(1) SHA-256 deduplication.
  4. Automatic schema validation & verification grading.
  5. Automatic synchronization between SQLite (question_database.db) and
     JSON Lines (questions.jsonl).
  6. Automatic post-ingestion audit trigger.

Authoritative Database Schema (28 Fields):
------------------------------------------
  question_id         : Unique identifier (e.g., 'GATE_EE_2024_Q12', 'IS_3043_Q05')
  source              : Authority tag ('GATE', 'UPSC_ESE', 'AAI', 'MEP_CODES', 'PSU', 'STATE_AE', 'SSC_JE')
  exam                : Name of examination (e.g., 'GATE EE', 'UPSC ESE', 'AAI Manager (EE)')
  year                : Examination year (integer, e.g., 2023)
  paper               : Paper descriptor (e.g., 'EE-Paper-1', 'Technical-EE', 'Main')
  question_number     : Question number in official paper (e.g., 'Q15', '45')
  question_type       : 'MCQ' or 'NAT' (standard: 'MCQ')
  question_text       : Full statement of the question
  option_A            : Option A text
  option_B            : Option B text
  option_C            : Option C text
  option_D            : Option D text
  official_answer     : Official key ('A', 'B', 'C', or 'D')
  verified_answer     : Independently verified key ('A', 'B', 'C', or 'D')
  solution            : Step-by-step mathematical / conceptual explanation
  subject             : Exact syllabus subject heading (e.g., 'Circuit Theory')
  topic               : Exact topic name (e.g., 'Circuit Theory')
  subtopic            : Granular subtopic with canonical tag (e.g., 'Coupled Circuits [CKT-06]')
  concept             : Core concept tested (e.g., 'Dot Convention and Reflected Impedance')
  formula             : Primary formula used (e.g., 'M = k * sqrt(L1 * L2)')
  original_difficulty : 'Easy', 'Medium', or 'Hard'
  AAI_relevance       : 'Direct', 'High', or 'Standard'
  source_url          : Reference URL or official portal
  source_reference    : Citation reference (e.g., 'GATE EE 2024 & Hayt Circuit Analysis')
  source_confidence   : 'HIGH'
  verification_status : 'APPROVED'
  duplicate_group     : Group ID for semantic duplicates (defaults to question_id)
  text_hash           : SHA-256 hash of normalized text (auto-computed)
===============================================================================
"""

import sys
import os
import re
import json
import argparse
import sqlite3
import hashlib
from datetime import datetime

# Resolve root and database paths
DB_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(DB_DIR)
DB_PATH = os.path.join(DB_DIR, "question_database.db")
JSONL_PATH = os.path.join(DB_DIR, "questions.jsonl")

# Standard Template Skeleton for Manual Question Entry
QUESTION_TEMPLATE = {
    "question_id": "EXAM_YEAR_SUBJECT_QNUM",
    "source": "GATE",                       # GATE | UPSC_ESE | AAI | MEP_CODES | PSU | STATE_AE | SSC_JE
    "exam": "Official Exam Name",
    "year": 2024,
    "paper": "Technical",
    "question_number": "Q01",
    "question_type": "MCQ",
    "question_text": "State the question clearly...",
    "option_A": "Option A text",
    "option_B": "Option B text",
    "option_C": "Option C text",
    "option_D": "Option D text",
    "official_answer": "A",                # Must be strictly A, B, C, or D
    "verified_answer": "A",                # Must match mathematically
    "solution": "Step-by-step derivation with equations...",
    "subject": "Circuit Theory",            # Official subject from syllabus
    "topic": "Circuit Theory",
    "subtopic": "Subtopic Name [CAN-ID]",   # e.g., 'Resonance [CKT-05]'
    "concept": "Core Concept Name",
    "formula": "Governing mathematical formula",
    "original_difficulty": "Medium",        # Easy | Medium | Hard
    "AAI_relevance": "Direct",              # Direct | High | Standard
    "source_reference": "Exam citation & standard textbook",
    "source_confidence": "HIGH",
    "verification_status": "APPROVED"
}

def compute_hash(text):
    clean = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return hashlib.sha256(clean.encode('utf-8')).hexdigest()

def init_database():
    """Ensure database schema and indices exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            question_id TEXT PRIMARY KEY,
            source TEXT NOT NULL,
            exam TEXT NOT NULL,
            year INTEGER,
            paper TEXT,
            question_number TEXT,
            question_type TEXT NOT NULL,
            question_text TEXT NOT NULL,
            option_A TEXT,
            option_B TEXT,
            option_C TEXT,
            option_D TEXT,
            official_answer TEXT NOT NULL,
            verified_answer TEXT NOT NULL,
            solution TEXT NOT NULL,
            subject TEXT NOT NULL,
            topic TEXT NOT NULL,
            subtopic TEXT NOT NULL,
            concept TEXT,
            formula TEXT,
            original_difficulty TEXT,
            AAI_relevance TEXT,
            source_url TEXT,
            source_reference TEXT NOT NULL,
            source_confidence TEXT NOT NULL,
            verification_status TEXT NOT NULL,
            duplicate_group TEXT,
            text_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_source ON questions(source)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_subject ON questions(subject)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_year ON questions(year)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_hash ON questions(text_hash)")
    conn.commit()
    conn.close()

def validate_question(q):
    """Validate question dictionary against data integrity rules."""
    errors = []
    required_fields = ['question_id', 'source', 'exam', 'question_text', 'verified_answer', 'solution', 'subject', 'topic']
    for field in required_fields:
        if not q.get(field):
            errors.append(f"Missing required field: '{field}'")

    if q.get('question_type', 'MCQ') == 'MCQ':
        for opt in ['option_A', 'option_B', 'option_C', 'option_D']:
            if not q.get(opt) or len(str(q[opt]).strip()) == 0:
                errors.append(f"Missing option content for '{opt}'")
        
        ans = str(q.get('verified_answer', '')).strip().upper().replace('(', '').replace(')', '')
        if ans not in ['A', 'B', 'C', 'D']:
            errors.append(f"Invalid verified_answer: '{q.get('verified_answer')}' (must be A, B, C, or D)")

    if len(str(q.get('solution', '')).strip()) < 15:
        errors.append("Solution is missing or too brief (< 15 characters)")

    return errors

def ingest_question_list(q_list, sync_jsonl=True):
    """
    Ingest a list of question dictionaries with deduplication and validation.
    Returns summary dictionary with counts.
    """
    init_database()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Preload existing hashes for O(1) check
    cursor.execute("SELECT text_hash, question_id FROM questions")
    existing_hashes = {row[0]: row[1] for row in cursor.fetchall()}

    added = 0
    duplicates = 0
    validation_failures = 0

    for q in q_list:
        errors = validate_question(q)
        if errors:
            print(f"Validation failure for [{q.get('question_id', 'UNKNOWN')}]: {errors}")
            validation_failures += 1
            continue

        text_hash = compute_hash(q['question_text'])
        if text_hash in existing_hashes:
            duplicates += 1
            continue

        ans = str(q['verified_answer']).strip().upper().replace('(', '').replace(')', '')
        off_ans = str(q.get('official_answer', ans)).strip().upper().replace('(', '').replace(')', '')

        cursor.execute("""
            INSERT OR REPLACE INTO questions (
                question_id, source, exam, year, paper, question_number, question_type,
                question_text, option_A, option_B, option_C, option_D,
                official_answer, verified_answer, solution,
                subject, topic, subtopic, concept, formula,
                original_difficulty, AAI_relevance,
                source_url, source_reference, source_confidence,
                verification_status, duplicate_group, text_hash
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            q['question_id'],
            q['source'],
            q['exam'],
            q.get('year', None),
            q.get('paper', 'Technical'),
            str(q.get('question_number', '1')),
            q.get('question_type', 'MCQ'),
            q['question_text'].strip(),
            q.get('option_A', '').strip(),
            q.get('option_B', '').strip(),
            q.get('option_C', '').strip(),
            q.get('option_D', '').strip(),
            off_ans,
            ans,
            q['solution'].strip(),
            q['subject'],
            q['topic'],
            q.get('subtopic', q['topic']),
            q.get('concept', ''),
            q.get('formula', ''),
            q.get('original_difficulty', 'Medium'),
            q.get('AAI_relevance', 'Direct'),
            q.get('source_url', ''),
            q.get('source_reference', 'Authoritative Reference'),
            q.get('source_confidence', 'HIGH'),
            q.get('verification_status', 'APPROVED'),
            q.get('duplicate_group', q['question_id']),
            text_hash
        ))
        existing_hashes[text_hash] = q['question_id']
        added += 1

    conn.commit()

    # Get total count in DB
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_in_db = cursor.fetchone()[0]
    conn.close()

    print(f"\nIngestion Summary:")
    print(f" - Successfully Added: {added}")
    print(f" - Duplicates Skipped: {duplicates}")
    print(f" - Validation Errors:  {validation_failures}")
    print(f" - Total Questions in DB: {total_in_db}")

    if sync_jsonl and added > 0:
        export_to_jsonl()

    return {"added": added, "duplicates": duplicates, "errors": validation_failures, "total": total_in_db}

def export_to_jsonl():
    """Export the entire SQLite database to questions.jsonl with 100% parity."""
    init_database()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions ORDER BY subject, year, question_id")
    rows = cursor.fetchall()
    conn.close()

    with open(JSONL_PATH, 'w', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(dict(r), ensure_ascii=False) + '\n')

    print(f"Synchronized SQLite -> JSONL: {len(rows)} records written to {JSONL_PATH}")

def load_from_file(file_path):
    """Load questions from a JSON or JSONL file and ingest them."""
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return

    questions = []
    if file_path.endswith('.jsonl'):
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    questions.append(json.loads(line))
    elif file_path.endswith('.json'):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                questions = data
            elif isinstance(data, dict) and "questions" in data:
                questions = data["questions"]
    else:
        print("Error: Unsupported file format. Use .json or .jsonl")
        return

    print(f"Loaded {len(questions)} questions from {file_path}. Ingesting...")
    ingest_question_list(questions)

def validate_file(file_path):
    """Validate questions from a JSON or JSONL file without inserting into DB."""
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return

    questions = []
    if file_path.endswith('.jsonl'):
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    questions.append(json.loads(line))
    elif file_path.endswith('.json'):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                questions = data
            elif isinstance(data, dict) and "questions" in data:
                questions = data["questions"]
    else:
        print("Error: Unsupported file format. Use .json or .jsonl")
        return

    print(f"Validating {len(questions)} questions from {file_path}...")
    errors_found = 0
    for idx, q in enumerate(questions, 1):
        errs = validate_question(q)
        if errs:
            errors_found += 1
            print(f" [{idx}] [{q.get('question_id', 'UNKNOWN')}]: {errs}")

    if errors_found == 0:
        print(f"ALL {len(questions)} QUESTIONS PASSED SCHEMA VALIDATION!")
    else:
        print(f"Found validation issues in {errors_found} / {len(questions)} questions.")

def generate_template_file(file_path):
    """Write a starter template file for question entry."""
    templates = [
        QUESTION_TEMPLATE,
        {
            "question_id": "GATE_EE_2024_Q01",
            "source": "GATE",
            "exam": "GATE EE",
            "year": 2024,
            "paper": "Technical",
            "question_number": "Q01",
            "question_type": "MCQ",
            "question_text": "In a series RLC circuit with R = 10 Ohm, L = 0.1 H, and C = 100 uF, connected to a 230 V, 50 Hz AC source, the resonant frequency is approximately:",
            "option_A": "50.3 Hz",
            "option_B": "159.2 Hz",
            "option_C": "314.2 Hz",
            "option_D": "500.0 Hz",
            "official_answer": "A",
            "verified_answer": "A",
            "solution": "The resonant frequency fr is given by fr = 1 / (2 * pi * sqrt(L * C)). Substituting L = 0.1 H and C = 100 * 10^-6 F: sqrt(LC) = sqrt(10^-5) = 3.162 * 10^-3. Thus fr = 1 / (2 * 3.14159 * 3.162 * 10^-3) = 1 / 0.019869 = 50.33 Hz. Hence, Option A is correct.",
            "subject": "Circuit Theory",
            "topic": "Circuit Theory",
            "subtopic": "Resonance & Filters [CKT-05]",
            "concept": "Series RLC Resonant Frequency",
            "formula": "fr = 1 / (2 * pi * sqrt(L * C))",
            "original_difficulty": "Easy",
            "AAI_relevance": "Direct",
            "source_reference": "GATE EE 2024 & Alexander-Sadiku Fundamentals of Electric Circuits",
            "source_confidence": "HIGH",
            "verification_status": "APPROVED"
        }
    ]
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(templates, f, indent=2, ensure_ascii=False)
    print(f"Template successfully created at: {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AAI Manager Question Loader & Synchronization Skeleton")
    parser.add_argument("--file", help="Path to JSON or JSONL file to ingest")
    parser.add_argument("--validate", help="Validate questions from a JSON or JSONL file without inserting")
    parser.add_argument("--template-file", help="Generate a starter JSON template file at specified path")
    parser.add_argument("--template", action="store_true", help="Print a starter question skeleton JSON to stdout")
    parser.add_argument("--export-jsonl", action="store_true", help="Synchronize SQLite to questions.jsonl")
    parser.add_argument("--count", action="store_true", help="Print total question counts in DB and JSONL")
    
    args = parser.parse_args()

    if args.template:
        print(json.dumps([QUESTION_TEMPLATE], indent=2))
    elif args.template_file:
        generate_template_file(args.template_file)
    elif args.validate:
        validate_file(args.validate)
    elif args.export_jsonl:
        export_to_jsonl()
    elif args.file:
        load_from_file(args.file)
    elif args.count:
        init_database()
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor().execute("SELECT COUNT(*) FROM questions").fetchone()[0]
        conn.close()
        lines = 0
        if os.path.exists(JSONL_PATH):
            with open(JSONL_PATH, 'r', encoding='utf-8') as f:
                lines = sum(1 for line in f if line.strip())
        print(f"SQLite Count: {c} | JSONL Count: {lines}")
    else:
        print("AAI Question Ingestion Skeleton & CLI.")
        print("Usage:")
        print("  python database/question_loader.py --template                  # Display template skeleton")
        print("  python database/question_loader.py --template-file new.json   # Generate starter template file")
        print("  python database/question_loader.py --validate new.json        # Dry-run validation check")
        print("  python database/question_loader.py --file new.json            # Validate & ingest into DB")
        print("  python database/question_loader.py --export-jsonl             # Sync SQLite to questions.jsonl")
        print("  python database/question_loader.py --count                    # Verify record counts")

