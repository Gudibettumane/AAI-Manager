import sqlite3
import json
import os
import re
import hashlib
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "question_database.db")
JSONL_PATH = os.path.join(os.path.dirname(__file__), "questions.jsonl")
STATE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "DB_MISSION_STATE.json")

OFFICIAL_SUBJECTS = [
    "Circuit Theory",
    "Signals & Systems",
    "Measurements & Instrumentation",
    "Electrical Machines",
    "Power Systems",
    "Control Systems",
    "Analog & Digital Electronics",
    "Power Electronics & Drives",
    "Microprocessors & Microcomputers",
    "Communication & Fiber Optics",
    "HVAC & Refrigeration",
    "Pumps & Fluid Mechanics",
    "Airport Substation, DG & UPS",
    "Fire Safety, Lifts & BMS",
    "Utilization & Illumination",
    "Contract Management & Safety Codes",
    "General Non-Technical"
]

def init_db():
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
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_status ON questions(verification_status)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_hash ON questions(text_hash)")
    conn.commit()
    conn.close()

def compute_hash(text):
    clean = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return hashlib.sha256(clean.encode('utf-8')).hexdigest()

def insert_question(q_data):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    text_hash = compute_hash(q_data['question_text'])
    
    # Check duplicate
    cursor.execute("SELECT question_id, duplicate_group FROM questions WHERE text_hash = ?", (text_hash,))
    row = cursor.fetchone()
    if row:
        canonical_id = row[1] if row[1] else row[0]
        conn.close()
        return {"status": "DUPLICATE", "canonical_id": canonical_id, "question_id": q_data['question_id']}

    # Verification checks
    status = q_data.get('verification_status', 'APPROVED')
    if q_data['question_type'] == 'MCQ':
        if not (q_data.get('option_A') and q_data.get('option_B') and q_data.get('option_C') and q_data.get('option_D')):
            status = 'UNVERIFIED'
        if q_data['verified_answer'] not in ['A', 'B', 'C', 'D', '(A)', '(B)', '(C)', '(D)']:
            status = 'UNVERIFIED'
    
    if not q_data.get('solution') or len(q_data['solution'].strip()) < 10:
        status = 'UNVERIFIED'

    # Clean verified_answer to standard 'A', 'B', 'C', 'D'
    ans = q_data['verified_answer'].strip().upper()
    ans = ans.replace('(', '').replace(')', '').strip()
    q_data['verified_answer'] = ans

    off_ans = q_data.get('official_answer', ans).strip().upper()
    off_ans = off_ans.replace('(', '').replace(')', '').strip()
    q_data['official_answer'] = off_ans

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
        q_data['question_id'],
        q_data['source'],
        q_data['exam'],
        q_data.get('year', None),
        q_data.get('paper', 'Main'),
        str(q_data.get('question_number', '1')),
        q_data.get('question_type', 'MCQ'),
        q_data['question_text'].strip(),
        q_data.get('option_A', '').strip(),
        q_data.get('option_B', '').strip(),
        q_data.get('option_C', '').strip(),
        q_data.get('option_D', '').strip(),
        q_data['official_answer'],
        q_data['verified_answer'],
        q_data['solution'].strip(),
        q_data['subject'],
        q_data['topic'],
        q_data.get('subtopic', q_data['topic']),
        q_data.get('concept', ''),
        q_data.get('formula', ''),
        q_data.get('original_difficulty', 'Moderate'),
        q_data.get('AAI_relevance', 'Direct Core'),
        q_data.get('source_url', ''),
        q_data['source_reference'],
        q_data.get('source_confidence', 'High - Standard Reference'),
        status,
        q_data.get('duplicate_group', q_data['question_id']),
        text_hash
    ))
    conn.commit()
    conn.close()
    return {"status": status, "question_id": q_data['question_id']}

def export_jsonl():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions ORDER BY subject, year, question_id")
    rows = cursor.fetchall()
    with open(JSONL_PATH, 'w', encoding='utf-8') as f:
        for r in rows:
            d = dict(r)
            f.write(json.dumps(d, ensure_ascii=False) + '\n')
    conn.close()

def get_stats():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT count(*) FROM questions")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT count(*) FROM questions WHERE verification_status = 'APPROVED'")
    approved = cursor.fetchone()[0]

    cursor.execute("SELECT count(*) FROM questions WHERE verification_status = 'UNVERIFIED'")
    unverified = cursor.fetchone()[0]

    cursor.execute("SELECT count(*) FROM questions WHERE verification_status = 'REJECTED'")
    rejected = cursor.fetchone()[0]

    cursor.execute("SELECT source, count(*) FROM questions GROUP BY source")
    by_source = dict(cursor.fetchall())

    cursor.execute("SELECT subject, count(*) FROM questions GROUP BY subject")
    by_subject = dict(cursor.fetchall())

    cursor.execute("SELECT original_difficulty, count(*) FROM questions GROUP BY original_difficulty")
    by_diff = dict(cursor.fetchall())

    conn.close()
    return {
        "total": total,
        "approved": approved,
        "unverified": unverified,
        "rejected": rejected,
        "by_source": by_source,
        "by_subject": by_subject,
        "by_difficulty": by_diff
    }

def update_mission_state(stage="RUNNING"):
    stats = get_stats()
    state = {
        "mission": "BUILD THE AAI ELECTRICAL QUESTION DATABASE",
        "timestamp": datetime.now().isoformat(),
        "stage": stage,
        "database_file": DB_PATH,
        "jsonl_file": JSONL_PATH,
        "stats": stats
    }
    with open(STATE_PATH, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2)
    export_jsonl()
    return state
