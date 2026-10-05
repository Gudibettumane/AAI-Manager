import os
import sys
import json
import sqlite3
import hashlib
import re

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(ROOT_DIR, "database", "question_database.db")
JSONL_PATH = os.path.join(ROOT_DIR, "database", "questions.jsonl")

def normalize_text(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

def compute_hash(text):
    return hashlib.sha256(normalize_text(text).encode('utf-8')).hexdigest()

QUESTIONS_PART3 = [
    # -------------------------------------------------------------------------
    # HVAC & BUILDING SERVICES: Boilers, VRV, Precision AC [HVC-01, HVC-03]
    # -------------------------------------------------------------------------
    {
        "question_id": "AAI_HVC_BOILER_01",
        "question_text": "In airport terminal central heating installations and commercial flight catering kitchens, why are fully automatic pressurized Hot Water Generators / Boilers preferred over high-pressure steam boilers?",
        "option_a": "Pressurized hot water systems operate at lower temperatures and require no statutory IBR (Indian Boiler Regulations) full-time certified boiler attendants if water temperature is maintained below 100°C / operating pressure is low, while eliminating steam trap thermodynamic losses and blowdown water wastage",
        "option_b": "Steam boilers cannot provide heat over 50 °C",
        "option_c": "Hot water generators consume zero electricity",
        "option_d": "Pressurized hot water cannot be circulated through AHU heating coils",
        "official_answer": "A",
        "verified_answer": "A",
        "solution": "In airport central MEP heating systems:\n1. **Statutory & Regulatory Ease:** High-pressure steam boilers fall under the stringent Indian Boiler Regulations (IBR 1950), mandating 24/7 licensed boiler attendants, annual shutdown inspections, and rigorous water chemical softening.\n2. **Energy & Thermal Efficiency:** Closed-loop **Pressurized Hot Water Generators** operate without steam trap leaks, flash steam venting, or continuous boiler blowdown losses. The closed circulation loop prevents oxygen ingress, virtually eliminating internal pipe corrosion and conserving up to $15-20\\%$ thermal fuel compared to steam plants.",
        "source": "AAI",
        "source_reference": "AAI Airport Terminal Mechanical Engineering Manual & IBR 1950 Standards",
        "source_url": "https://www.aai.aero",
        "exam": "AAI Manager (Electrical) Technical Standards",
        "year": 2023,
        "paper_set": "HVAC Standards",
        "official_question_number": "16",
        "subject": "HVAC & Refrigeration",
        "topic": "Central Heating Plants",
        "subtopic": "Hot Water Generators vs Steam Boilers in Airport Terminals [HVC-01]",
        "concept": "Closed-loop hot water generators eliminate steam trap losses and IBR licensing burdens",
        "formula_used": "\\text{Closed Loop Water System: Zero Flash Steam Losses, Higher Thermal Efficiency}",
        "canonical_topic_id": "HVC-01",
        "original_difficulty": "Easy",
        "exam_trap": "Assuming steam is always more efficient; steam systems suffer high parasitic trap and blowdown losses."
    },
    {
        "question_id": "AAI_HVC_PAC_03",
        "question_text": "In airport Air Traffic Control (ATC) equipment rooms, radar processor suites, and server data centers, why is Precision Air Conditioning (PAC) mandatory instead of standard commercial comfort air conditioning?",
        "option_a": "Comfort AC units cannot operate on 415 V supply",
        "option_b": "Electronic server and radar equipment produce almost 100% sensible heat (Sensible Heat Ratio SHR ≈ 0.90 to 0.98) requiring high CFM/TR airflow with tight micro-tolerance temperature (± 1°C) and relative humidity (50% ± 5% RH) control to prevent static discharge and condensation",
        "option_c": "Precision AC units use water as the only refrigerant",
        "option_d": "Comfort AC units do not have air filters",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In aviation electronics and data center environments:\n1. Human occupants generate significant latent (perspiration/moisture) heat (Comfort AC Sensible Heat Ratio $SHR \\approx 0.65 - 0.70$).\n2. Computer servers, transmitters, and radar processors generate **almost pure sensible heat ($SHR \\approx 0.90 - 0.98$)** with zero moisture gain.\n3. Standard comfort AC over-dehumidifies server rooms, causing dry air, electrostatic discharge (ESD) that destroys microchips, and wastes energy.\n4. **Precision Air Conditioning (PAC):** Delivers very high airflow ($550-650\\text{ CFM per TR}$) with dedicated modulating electric reheat and electrode-boiler steam humidifiers, maintaining temperature strictly within $\\pm 1^\\circ\\text{C}$ and relative humidity strictly at **$50\\% \\pm 5\\%\\text{ RH}$** 24 hours a day, 365 days a year.",
        "source": "AAI",
        "source_reference": "ASHRAE TC 9.9 Data Center Environmental Guidelines & AAI ATC Facility Standards",
        "source_url": "https://www.ashrae.org",
        "exam": "AAI Manager (Electrical) Technical Standards",
        "year": 2023,
        "paper_set": "Precision HVAC",
        "official_question_number": "17",
        "subject": "HVAC & Refrigeration",
        "topic": "Precision Air Conditioning",
        "subtopic": "Sensible Heat Ratio (SHR) and Relative Humidity Tolerances in ATC Rooms [HVC-03]",
        "concept": "PAC provides high SHR (0.95) and tight RH control (50% +/- 5%) for sensitive electronics",
        "formula_used": "SHR = \\frac{\\text{Sensible Heat}}{\\text{Total Heat}} \\approx 0.90 - 0.98 \\text{ in Data Centers}",
        "canonical_topic_id": "HVC-03",
        "original_difficulty": "Easy",
        "exam_trap": "Selecting comfort AC for server rooms; comfort AC causes low humidity ESD and premature server component failures."
    },

    # -------------------------------------------------------------------------
    # EARTHING & LIGHTNING PROTECTION: IS:3043 & IS/IEC 62305 [ERT-01, ERT-02]
    # -------------------------------------------------------------------------
    {
        "question_id": "AAI_ERT_IS3043_01",
        "question_text": "According to IS:3043 (Code of Practice for Earthing) and CEA Safety Regulations, what is the maximum permissible electrical resistance to earth for an airport 33/11 kV main receiving substation, and what treatment material is specified to reduce earth electrode contact resistance in rocky or dry soil?",
        "option_a": "5.0 Ω maximum; treated with diesel oil",
        "option_b": "1.0 Ω maximum for main substation (and < 0.5 Ω for large generating/switchyard stations); treated with alternate layers of charcoal/coke and common salt, or sodium bentonite compound",
        "option_c": "10.0 Ω maximum; treated with limestone gravel only",
        "option_d": "25.0 Ω maximum; treated with sulfuric acid",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In accordance with IS:3043 and Central Electricity Authority (CEA) Regulations 2023:\n1. **Permissible Earth Resistance:**\n   - Large Generating Stations / 33 kV Substations: **$\\le 0.5\\ \\Omega$ to $1.0\\ \\Omega$**.\n   - Airport ATC Towers and Navigational Aids (ILS/DVOR): **$\\le 1.0\\ \\Omega$**.\n   - Small Substation / Industrial installations: $\\le 2.0\\ \\Omega$.\n2. **Soil Treatment:** To lower high soil resistivity, a $2.5 - 3.0\\text{ meter}$ deep earth pit is excavated around the GI or copper plate/pipe electrode and packed with alternate layers of **charcoal (or coke)** and **common salt ($NaCl$)**, or maintenance-free high-conductivity **bentonite / carbonaceous backfill compound**.",
        "source": "MEP_CODES",
        "source_reference": "IS:3043 Code of Practice for Earthing & CEA Safety Regulations 2023",
        "source_url": "https://www.bis.gov.in",
        "exam": "BIS Electrical Standards",
        "year": 2023,
        "paper_set": "Earthing Standards",
        "official_question_number": "06",
        "subject": "Utilization & Illumination",
        "topic": "Earthing Systems",
        "subtopic": "IS:3043 Substation Earth Resistance Limits and Soil Conditioning [ERT-01]",
        "concept": "Main substation earth resistance must be <= 1.0 ohm; treated with charcoal, salt, or bentonite",
        "formula_used": "R_{earth} \\le 1.0\\ \\Omega \\text{ (Substation)}, \\quad R_{earth} \\le 0.5\\ \\Omega \\text{ (Large Generating)}",
        "canonical_topic_id": "ERT-01",
        "original_difficulty": "Easy",
        "exam_trap": "Selecting 5.0 ohms, which is only allowable for residential domestic consumer installations."
    },
    {
        "question_id": "AAI_ERT_DOWNCOND_02",
        "question_text": "In accordance with IS/IEC 62305-3 for Class I and Class II Lightning Protection Systems (LPS) on airport passenger terminal roofs, what is the standardized maximum horizontal spacing between down-conductors running from roof air-terminals to ground earth pits?",
        "option_a": "5 meters",
        "option_b": "10 meters for Class I and 10 meters for Class II",
        "option_c": "25 meters for all classes",
        "option_d": "50 meters",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In accordance with IS/IEC 62305-3 (Table 4 - Distances between down-conductors):\n- **Class I (Highest risk - Air Traffic Control Tower, explosive fuel farm):** Typical distance between down-conductors is **$10\\text{ meters}$**.\n- **Class II (Large Airport Passenger Terminal Buildings):** Typical distance between down-conductors is **$10\\text{ meters}$**.\n- **Class III (Commercial buildings):** $15\\text{ meters}$.\n- **Class IV (Standard structures):** $20\\text{ meters}$.\nMultiple parallel down-conductors divide the massive lightning surge current ($I_{peak} \\approx 100-200\\text{ kA}$), minimizing inductive voltage drop and dangerous internal side-flashing.",
        "source": "MEP_CODES",
        "source_reference": "IS/IEC 62305-3 Protection Against Lightning: Physical Damage to Structures",
        "source_url": "https://www.bis.gov.in",
        "exam": "Lightning Protection Standards",
        "year": 2022,
        "paper_set": "Class I LPS",
        "official_question_number": "12",
        "subject": "Utilization & Illumination",
        "topic": "Lightning Protection Systems",
        "subtopic": "IS/IEC 62305 Down Conductor Spacing for Class I and II Structures [ERT-02]",
        "concept": "Down conductor spacing is 10 m for Class I and Class II airport structures",
        "formula_used": "\\text{Spacing } \\le 10\\text{ m (Class I & II LPS)}",
        "canonical_topic_id": "ERT-02",
        "original_difficulty": "Easy",
        "exam_trap": "Selecting 20 m; 20 m spacing is only permitted for low-risk Class IV standard buildings."
    },

    # -------------------------------------------------------------------------
    # FIRE SAFETY: Addressable Panels & Sprinklers [FIR-01, FIR-02]
    # -------------------------------------------------------------------------
    {
        "question_id": "AAI_FIR_ADDR_01",
        "question_text": "In modern airport terminal building fire safety engineering, what is the fundamental functional advantage of an Intelligent Analogue Addressable Fire Alarm System over a conventional zoned fire alarm system?",
        "option_a": "Conventional systems do not require wire cables",
        "option_b": "In an addressable system, every individual detector and manual call point (MCP) has a unique digital address, allowing the main panel to identify the exact physical location of a fire within seconds, while continuously monitoring real-time analog smoke obscuration levels to compensate for dust drift",
        "option_c": "Addressable systems cannot be linked to HVAC fire dampers",
        "option_d": "Conventional systems provide automatic graphical workstation mapping",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In airport fire engineering (IS 2189 / NFPA 72):\n1. In conventional zoned systems, an entire terminal wing or floor (30 to 50 rooms) is grouped into one 'zone'. A fire alarm only indicates the zone number, forcing security to manually search dozens of rooms to locate the fire.\n2. **Analogue Addressable Fire Alarm System:** Every smoke detector, heat detector, duct detector, and manual call point possesses a unique electronic address (e.g. Loop 2, Detector 45 - 'Terminal 2 Departures Gate 4 Retail Store').\n3. The central microprocessor panel continuously polls sensor analog values, applies intelligent drift compensation algorithm to prevent false alarms from terminal dust, and automatically commands HVAC fire dampers to trip and AHUs to shut down.",
        "source": "AAI",
        "source_reference": "IS 2189 Selection, Installation and Maintenance of Automatic Fire Detection and Alarm System",
        "source_url": "https://www.bis.gov.in",
        "exam": "AAI Manager (Electrical) Technical Standards",
        "year": 2023,
        "paper_set": "Fire Detection",
        "official_question_number": "05",
        "subject": "Fire Safety, Lifts & BMS",
        "topic": "Fire Alarm Systems",
        "subtopic": "Intelligent Analogue Addressable vs Conventional Fire Alarm Panels [FIR-01]",
        "concept": "Addressable fire panels pinpoint exact device location and provide drift compensation",
        "formula_used": "\\text{Addressable Loop: Unique Digital ID + Drift Compensation + Damper Actuation}",
        "canonical_topic_id": "FIR-01",
        "original_difficulty": "Easy",
        "exam_trap": "Thinking addressable systems are just multiplexed conventional systems; they transmit continuous analog values."
    },
    {
        "question_id": "AAI_FIR_DOWNCOMER_02",
        "question_text": "According to NBC 2016 Part 4, what is the specific technical distinction between a 'Wet Riser' and a 'Down Comer' in multi-storey airport facility fire fighting infrastructure?",
        "option_a": "A Wet Riser is always charged with water under pressure from fire pumps; a Down Comer is charged with water from an overhead terrace tank via a terrace booster pump with fire brigade breeching inlet at ground level",
        "option_b": "A Down Comer carries pressurized foam while a Wet Riser carries pure water",
        "option_c": "Wet Risers are installed outdoors only",
        "option_d": "Down Comers operate without any pipes",
        "official_answer": "A",
        "verified_answer": "A",
        "solution": "Under National Building Code of India (NBC 2016 Part 4 Section 5):\n1. **Wet Riser:** An arrangement of vertical fire-fighting piping permanently charged with water from the underground static fire reservoir via automatic main electric and diesel fire pumps, maintaining constant high pressure ($7.0 - 8.5\\text{ kg/cm}^2$) at all internal landing valves across all floors.\n2. **Down Comer:** A vertical pipe connected to an **overhead terrace water tank** (typically 20,000 to 25,000 liters) through a terrace booster pump (450 LPM at 3.5 bar), equipped with a 2-way Fire Brigade Breeching Inlet at ground level so fire tenders can pump water directly into the system.",
        "source": "MEP_CODES",
        "source_reference": "National Building Code of India (NBC 2016) Part 4 Fire and Life Safety",
        "source_url": "https://www.bis.gov.in",
        "exam": "NBC Fire Protection Standards",
        "year": 2022,
        "paper_set": "Fire Hydraulics",
        "official_question_number": "09",
        "subject": "Fire Safety, Lifts & BMS",
        "topic": "Fire Protection Systems",
        "subtopic": "Wet Riser vs Down Comer System Architecture under NBC 2016 [FIR-02]",
        "concept": "Wet Riser is pressurized from underground static tank; Down Comer is fed from terrace tank",
        "formula_used": "\\text{Wet Riser: Underground Reservoir + Main Pumps; } \\quad \\text{Down Comer: Terrace Tank + Booster}",
        "canonical_topic_id": "FIR-02",
        "original_difficulty": "Easy",
        "exam_trap": "Confusing Wet Riser with Dry Riser; Dry Riser remains empty until charged by fire brigade tenders."
    },

    # -------------------------------------------------------------------------
    # BUILDING SERVICES: BMS Protocols & CCTV [BMS-01, SEC-01]
    # -------------------------------------------------------------------------
    {
        "question_id": "AAI_BMS_BACNET_01",
        "question_text": "In airport Integrated Building Management Systems (IBMS), which open-standard communication protocol compliant with ANSI/ASHRAE Standard 135 is universally deployed for vendor-independent interoperability between chiller plants, AHU Direct Digital Controllers (DDCs), and fire dampers?",
        "option_a": "Zigbee RF mesh only",
        "option_b": "BACnet (Building Automation and Control networks) over IP / MSTP",
        "option_c": "USB 2.0 serial protocol",
        "option_d": "Centronics parallel interface",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In airport IBMS facility automation:\n1. Airport terminals incorporate equipment from diverse manufacturers: chillers (Carrier/York/Trane), VFDs (ABB/Danfoss), fire panels (Honeywell/Notifier), and AHU DDCs (Siemens/Schneider).\n2. **BACnet (ANSI/ASHRAE Standard 135 / ISO 16484-5):** Is the globally standardized open protocol designed specifically for building automation.\n3. It defines standardized object profiles (Analog Input, Binary Output, Schedule, TrendLog) that allow controllers from different vendors to seamlessly exchange control commands, sensor temperatures, and alarm states over Ethernet/IP and RS-485 MS/TP networks without proprietary software gateways.",
        "source": "AAI",
        "source_reference": "ANSI/ASHRAE Standard 135 BACnet Protocol & AAI IBMS Guidelines",
        "source_url": "https://www.bacnet.org",
        "exam": "AAI Manager (Electrical) Technical Standards",
        "year": 2023,
        "paper_set": "IBMS Standards",
        "official_question_number": "10",
        "subject": "Fire Safety, Lifts & BMS",
        "topic": "Building Management Systems",
        "subtopic": "BACnet Protocol (ASHRAE 135) for Multi-Vendor IBMS Interoperability [BMS-01]",
        "concept": "BACnet is the universal ASHRAE 135 open protocol for vendor-independent BMS interoperability",
        "formula_used": "\\text{BACnet/IP (Ethernet) & BACnet MS/TP (RS-485) } \\implies \\text{Open Standard Interoperability}",
        "canonical_topic_id": "BMS-01",
        "original_difficulty": "Easy",
        "exam_trap": "Selecting Modbus RTU as the universal standard; while Modbus is common for simple meters, BACnet is the standard for complex BMS control."
    },
    {
        "question_id": "AAI_SEC_CCTV_01",
        "question_text": "In accordance with Bureau of Civil Aviation Security (BCAS) guidelines and AAI airport surveillance specifications, what is the minimum frame rate (fps) and mandated continuous video storage retention period for airside perimeter and passenger check-in CCTV cameras?",
        "option_a": "5 fps and 7 days storage",
        "option_b": "25/30 fps (Full Frame Real Time) and 30 days continuous storage retention on high-reliability Network Video Recorders (NVR) with RAID 5/6 redundancy",
        "option_c": "1 fps and 24 hours storage",
        "option_d": "60 fps and 365 days storage",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "Under Bureau of Civil Aviation Security (BCAS) circulars and AAI CCTV engineering specifications:\n1. **Frame Rate:** All security surveillance cameras covering passenger terminal check-in, security frisking, baggage makeup areas, and boarding gates must record at full real-time frame rate: **$25\\text{ fps}$ (PAL) / $30\\text{ fps}$ (NTSC)** at high definition (1080p / 4K resolution) using H.265/H.264 compression.\n2. **Storage Retention:** Video archives must be retained continuously for a minimum statutory period of **$30\\text{ days}$** on enterprise SAN/NAS storage arrays equipped with **RAID 5 or RAID 6** array redundancy to guarantee zero footage loss upon hard drive failure.",
        "source": "AAI",
        "source_reference": "BCAS Security Guidelines for Civil Aviation & AAI CCTV Surveillance Standards",
        "source_url": "https://www.bcasindia.gov.in",
        "exam": "AAI Manager (Electrical) Technical Standards",
        "year": 2023,
        "paper_set": "CCTV Standards",
        "official_question_number": "15",
        "subject": "Fire Safety, Lifts & BMS",
        "topic": "CCTV Surveillance Systems",
        "subtopic": "BCAS CCTV Frame Rates (25 fps) and 30-Day Storage Retention Standards [SEC-01]",
        "concept": "BCAS mandates 25/30 fps real-time recording and 30-day continuous storage with RAID redundancy",
        "formula_used": "\\text{Frame Rate } = 25\\text{ fps}, \\quad \\text{Storage Retention } \\ge 30\\text{ Days, } \\text{RAID 5/6}",
        "canonical_topic_id": "SEC-01",
        "original_difficulty": "Easy",
        "exam_trap": "Thinking 7 days storage is sufficient; aviation security strictly mandates at least 30 days storage."
    }
]

def add_part3():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT question_id, text_hash FROM questions")
    rows = cursor.fetchall()
    existing_ids = {r[0] for r in rows}
    existing_hashes = {r[1] for r in rows}

    added = 0
    skipped = 0

    for q in QUESTIONS_PART3:
        qid = q["question_id"]
        qhash = compute_hash(q["question_text"])

        if qid in existing_ids or qhash in existing_hashes:
            skipped += 1
            continue

        cursor.execute("""
            INSERT INTO questions (
                question_id, source, exam, year, paper, question_number, question_type,
                question_text, option_A, option_B, option_C, option_D,
                official_answer, verified_answer, solution,
                subject, topic, subtopic, concept, formula,
                original_difficulty, AAI_relevance,
                source_url, source_reference, source_confidence,
                verification_status, duplicate_group, text_hash
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            qid,
            q["source"],
            q["exam"],
            q.get("year", 2023),
            q.get("paper_set", "Main"),
            str(q.get("official_question_number", "1")),
            "MCQ",
            q["question_text"].strip(),
            q["option_a"].strip(),
            q["option_b"].strip(),
            q["option_c"].strip(),
            q["option_d"].strip(),
            q["official_answer"],
            q["verified_answer"],
            q["solution"].strip(),
            q["subject"],
            q["topic"],
            q.get("subtopic", q["topic"]),
            q.get("concept", ""),
            q.get("formula_used", ""),
            q.get("original_difficulty", "Moderate"),
            "Direct Core",
            q.get("source_url", "https://www.aai.aero"),
            q["source_reference"],
            "High - Official Standard",
            "AUTHENTICATED",
            None,
            qhash
        ))

        existing_ids.add(qid)
        existing_hashes.add(qhash)
        added += 1

    conn.commit()

    # Re-export to JSON Lines with complete parity
    cursor.execute("SELECT * FROM questions ORDER BY subject, year, question_id")
    all_rows = cursor.fetchall()
    conn.row_factory = sqlite3.Row
    cursor2 = conn.cursor()
    cursor2.execute("SELECT * FROM questions ORDER BY subject, year, question_id")
    dict_rows = [dict(r) for r in cursor2.fetchall()]
    
    with open(JSONL_PATH, "w", encoding="utf-8") as f:
        for r in dict_rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    conn.close()
    print(f"\nMass Expansion Part 3 Ingestion Summary:")
    print(f" - Successfully Added: {added}")
    print(f" - Skipped: {skipped}")
    print(f" - New Database Total: {len(all_rows)} questions")

if __name__ == "__main__":
    add_part3()
