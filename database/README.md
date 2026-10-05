# AAI MANAGER (ELECTRICAL) — DATABASE ARCHITECTURE & TOOLING

This directory contains the central question database, data integrity engines, canonical syllabus auditors, and reusable ingestion tooling for the **AAI Manager (Engg.-Electrical) CBT** preparation system.

---

## 1. Directory Structure

```
database/
├── question_database.db       # Authoritative SQLite database (908 verified questions)
├── questions.jsonl            # Synchronized JSON Lines store (908 records)
├── question_loader.py         # Reusable skeleton & CLI for question ingestion & validation
├── db_manager.py              # Low-level SQLite database connection and query manager
├── run_integrity_audit.py     # Cryptographic integrity, schema, and math verification suite
├── audit_canonical_syllabus.py# Real-time mapper & auditor across 131 canonical syllabus topics
├── deep_pdf_syllabus_audit.py # Multi-question depth auditor for 44 official PDF focal subtopics
├── generate_reports.py        # Automated Markdown report generator
├── syllabus_topic_audit.json  # Topic-to-question mapping cache
└── README.md                  # This documentation
```

---

## 2. Reusable Tool Suite

### A. Question Loader Skeleton (`question_loader.py`)
The unified CLI for adding, validating, and managing questions.

* **View Question Template Skeleton:**
  ```bash
  python database/question_loader.py --template
  ```

* **Generate Starter JSON Template File:**
  ```bash
  python database/question_loader.py --template-file new_batch.json
  ```

* **Validate Question File (Dry-Run, No DB Modification):**
  ```bash
  python database/question_loader.py --validate new_batch.json
  ```

* **Ingest Question File (Deduplication + DB + JSONL Sync):**
  ```bash
  python database/question_loader.py --file new_batch.json
  ```

* **Verify Record Parity:**
  ```bash
  python database/question_loader.py --count
  ```

* **Export SQLite to JSONL:**
  ```bash
  python database/question_loader.py --export-jsonl
  ```

---

### B. Full System & Integrity Audit (`run_integrity_audit.py`)
Validates SQLite vs. JSONL parity, SHA-256 hash integrity, option formats, and answer keys.
```bash
python database/run_integrity_audit.py
```

---

### C. Canonical Syllabus Coverage Audit (`audit_canonical_syllabus.py`)
Maps all 908 questions against the 131 canonical syllabus topics defined in `SYLLABUS_MASTER.md` and flags any gaps.
```bash
python database/audit_canonical_syllabus.py
```

---

### D. Official PDF Depth Audit (`deep_pdf_syllabus_audit.py`)
Performs regex and semantic verification across all 44 specific subtopics mentioned in the official 4-page notification PDF (`Manager (Engg-Electrical) Syllabus.pdf`).
```bash
python database/deep_pdf_syllabus_audit.py
```

---

### E. Report Generation (`generate_reports.py`)
Regenerates all Markdown tracking reports:
* `QUESTION_DATABASE_STATS.md`
* `SYLLABUS_COVERAGE_REPORT.md`
* `DATABASE_GAPS.md`
* `SOURCE_COVERAGE_REPORT.md`

```bash
python database/generate_reports.py
```
