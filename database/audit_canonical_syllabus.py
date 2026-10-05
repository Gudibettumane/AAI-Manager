import os
import re
import json
import sqlite3
from collections import defaultdict, Counter

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(ROOT_DIR, "database", "question_database.db")
SYLLABUS_PATH = os.path.join(ROOT_DIR, "SYLLABUS_MASTER.md")

def parse_syllabus_topics():
    topics = {}
    current_subject = "General"
    
    with open(SYLLABUS_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("### ") or line.startswith("## PART-"):
                m = re.search(r'###\s+\d*\.?\s*(.+)', line)
                if m:
                    current_subject = m.group(1).strip()
            
            m_row = re.search(r'\|\s*\*\*([A-Z0-9\-]+)\*\*\s*\|\s*([^\|]+)\|', line)
            if m_row:
                topic_id = m_row.group(1).strip()
                topic_name = m_row.group(2).strip()
                topics[topic_id] = {
                    "topic_id": topic_id,
                    "topic_name": topic_name,
                    "subject": current_subject
                }
    return topics

def map_questions_to_topics(topics):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions")
    questions = [dict(r) for r in cursor.fetchall()]
    conn.close()

    topic_mapping = defaultdict(list)
    uncertain_relevance = []
    unmapped_questions = []

    for q in questions:
        text = (q["question_text"] + " " + q.get("topic", "") + " " + q.get("subtopic", "") + " " + q.get("concept", "")).lower()
        subj = q["subject"].lower()
        matched = None

        # 1. Control Systems (Allied EE / Uncertain Relevance to AAI Manager EE Advt 12/2026 syllabus)
        if "control system" in subj or subj == "control systems":
            uncertain_relevance.append({
                "question_id": q["question_id"],
                "subject": q["subject"],
                "topic": q.get("topic", ""),
                "concept": q.get("concept", ""),
                "source": q["source"],
                "reason": "Control Systems (Routh-Hurwitz, Nyquist, Bode, State Space, Root Locus, PID) is a core GATE/ESE EE subject but is NOT listed as an independent section in AAI Manager (EE) Advertisement No: 12/2026/CHQ/DR-CBT."
            })
            continue

        # Check for explicit canonical topic ID in topic, subtopic, concept, or question_id
        raw_metadata = (q.get("subtopic", "") + " " + q.get("topic", "") + " " + q.get("concept", "") + " " + q.get("question_id", "")).upper()
        m_id = re.search(r'\b([A-Z]{3}-\d{2})\b', raw_metadata)
        if m_id and m_id.group(1) in topics:
            matched = m_id.group(1)

        # 2. Power Electronics & Drives (Prioritized before general 'electronic')
        elif "power electronic" in subj or "drive" in subj:
            if any(k in text for k in ["scr", "thyristor", "triac", "gto", "mosfet", "igbt", "diode"]) and any(k in text for k in ["rating", "characteristic", "device", "construction"]):
                matched = "PEL-01"
            elif any(k in text for k in ["latching", "holding", "commutation", "turn-off", "triggering", "snubber", "dv/dt", "di/dt"]):
                matched = "PEL-02"
            elif any(k in text for k in ["rectifier", "controlled", "converter", "semi-converter", "firing angle", "freewheeling"]):
                matched = "PEL-03"
            elif any(k in text for k in ["buck", "boost", "chopper", "inverter", "spwm", "pwm", "vsi", "csi", "duty cycle"]):
                matched = "PEL-04"
            elif any(k in text for k in ["drive", "v/f", "speed control", "slip power", "kramer", "scherbius"]):
                matched = "PEL-05"
            else:
                matched = "PEL-01"

        # 3. Circuit Theory
        elif "circuit" in subj:
            if any(k in text for k in ["graph", "tree", "twig", "link", "tie-set", "cut-set", "kcl", "kvl", "incidence"]):
                matched = "CKT-01"
            elif any(k in text for k in ["nodal", "mesh", "node voltage", "mesh current"]):
                matched = "CKT-02"
            elif any(k in text for k in ["thevenin", "norton", "superposition", "maximum power", "millman", "tellegen", "reciprocity"]):
                matched = "CKT-03"
            elif any(k in text for k in ["transient", "time constant", "damping", "critically damped", "overdamped", "rlc", "step response"]):
                matched = "CKT-04"
            elif any(k in text for k in ["resonance", "resonant", "q-factor", "quality factor", "bandwidth", "tank circuit"]):
                matched = "CKT-05"
            elif any(k in text for k in ["coupled", "dot convention", "mutual inductance", "coupling coefficient"]):
                matched = "CKT-06"
            elif any(k in text for k in ["two-port", "z-parameter", "y-parameter", "abcd", "h-parameter", "hybrid parameter", "3-phase", "three-phase", "delta", "star"]):
                matched = "CKT-07"
            else:
                matched = "CKT-03"

        # 4. Signals & Systems
        elif "signal" in subj:
            if any(k in text for k in ["shift", "scaling", "time reversal", "even", "odd", "energy", "power signal"]):
                matched = "SIG-02"
            elif any(k in text for k in ["lti", "convolution", "impulse response", "causal", "stability"]):
                matched = "SIG-03"
            elif any(k in text for k in ["fourier", "ctft", "dtft", "fse"]):
                matched = "SIG-04"
            elif any(k in text for k in ["laplace", "s-plane"]):
                matched = "SIG-05"
            elif any(k in text for k in ["z-transform", "z-plane"]):
                matched = "SIG-06"
            else:
                matched = "SIG-01"

        # 5. Measurements & Instrumentation
        elif "measurement" in subj or "instrument" in subj:
            if any(k in text for k in ["megger", "insulation resistance", "earth resistance", "earth tester", "fall of potential", "soil resistivity"]):
                matched = "INS-01"
            elif any(k in text for k in ["kelvin", "double bridge", "wheatstone", "schering", "hay", "maxwell", "anderson", "wien"]):
                matched = "INS-02"
            elif any(k in text for k in ["quadrant", "electrometer", "electrostatic voltmeter"]):
                matched = "INS-03"
            elif any(k in text for k in ["rotating substandard", "rss", "phantom loading", "energy meter calibration", "creep"]):
                matched = "INS-04"
            elif any(k in text for k in ["tod", "time of day", "tariff", "tri-vector", "maximum demand"]):
                matched = "INS-05"
            elif any(k in text for k in ["pmmc", "moving iron", "dynamometer", "wattmeter", "instrument transformer", "ct", "pt"]):
                matched = "INS-04"
            else:
                matched = "INS-01"

        # 6. Electrical Machines & Single Phase Motors
        elif "machine" in subj:
            if any(k in text for k in ["single phase induction", "shaded pole", "split phase", "capacitor start", "capacitor run", "double revolving"]):
                if "shaded" in text:
                    matched = "SPM-03"
                elif "split" in text or "capacitor" in text:
                    matched = "SPM-02"
                else:
                    matched = "SPM-01"
            elif any(k in text for k in ["scott connection", "tee connection"]):
                matched = "MCH-04"
            elif any(k in text for k in ["3-phase transformer", "three phase transformer", "vector group", "dy11", "yd11", "tertiary"]):
                matched = "MCH-03"
            elif any(k in text for k in ["efficiency", "regulation", "oc test", "sc test", "all day efficiency", "open circuit test", "short circuit test", "equivalent circuit"]):
                matched = "MCH-02"
            elif any(k in text for k in ["transformer"]):
                matched = "MCH-01"
            elif any(k in text for k in ["induction motor"]):
                if any(k in text for k in ["speed control", "v/f", "starting", "star-delta", "autotransformer starter"]):
                    matched = "MCH-06"
                else:
                    matched = "MCH-05"
            elif any(k in text for k in ["synchronous", "alternator"]):
                if any(k in text for k in ["v curve", "inverted v", "excitation"]):
                    matched = "MCH-13"
                elif any(k in text for k in ["synchronous condenser", "power factor"]):
                    matched = "MCH-14"
                elif any(k in text for k in ["synchronous motor", "damper"]):
                    matched = "MCH-12"
                elif any(k in text for k in ["power angle", "reluctance power"]):
                    matched = "MCH-11"
                elif any(k in text for k in ["synchronization", "infinite bus", "dark lamp"]):
                    matched = "MCH-10"
                elif any(k in text for k in ["phasor", "two reaction", "salient", "xd", "xq"]):
                    matched = "MCH-09"
                elif any(k in text for k in ["scr", "short circuit ratio"]):
                    matched = "MCH-08"
                else:
                    matched = "MCH-07"
            elif any(k in text for k in ["dc machine", "dc motor", "dc generator", "shunt", "series motor", "ward-leonard", "dummy coil"]):
                matched = "MCH-06"
            else:
                matched = "MCH-01"

        # 7. Power Systems & Protection
        elif "power system" in subj:
            if any(k in text for k in ["buchholz", "differential relay", "distance relay", "mho", "reactance relay", "overcurrent", "directional", "pilot wire"]):
                matched = "PRT-01"
            elif any(k in text for k in ["numerical relay", "solid state relay", "microprocessor relay"]):
                matched = "PRT-02"
            elif any(k in text for k in ["dsp", "digital signal processing", "filtering"]):
                matched = "PRT-04"
            elif any(k in text for k in ["circuit breaker", "sf6", "vacuum", "air blast", "making capacity", "breaking capacity", "restriking", "rrr"]):
                matched = "TND-15"
            elif any(k in text for k in ["gmd", "gmr", "inductance", "capacitance", "skin effect", "proximity"]):
                matched = "TND-01"
            elif any(k in text for k in ["abcd", "ferranti", "surge impedance", "sil", "overhead", "bundled", "corona"]):
                matched = "TND-02"
            elif any(k in text for k in ["sag", "tension", "span", "catenary", "wind pressure", "ice"]):
                matched = "TND-03"
            elif any(k in text for k in ["tuned power line", "quarter wave", "half wave"]):
                matched = "TND-04"
            elif any(k in text for k in ["insulator", "string efficiency", "guard ring", "suspension"]):
                matched = "TND-05"
            elif any(k in text for k in ["cable", "underground", "capacitance grading", "belted", "sheath"]):
                matched = "TND-07"
            elif any(k in text for k in ["symmetrical fault", "3-phase fault", "short circuit mva"]):
                matched = "TND-09"
            elif any(k in text for k in ["symmetrical components", "sequence", "zero sequence", "positive sequence"]):
                matched = "TND-10"
            elif any(k in text for k in ["unbalanced", "l-g", "l-l", "l-l-g"]):
                matched = "TND-11"
            elif any(k in text for k in ["petersen", "earthing", "arcing ground"]):
                matched = "ERT-01"
            else:
                matched = "TND-02"

        # 8. Analog & Digital Electronics
        elif "analog" in subj or "digital" in subj or "electronic" in subj:
            if any(k in text for k in ["op-amp", "operational amplifier", "virtual ground", "slew rate", "instrumentation amplifier", "cmrr"]):
                matched = "ELX-03"
            elif any(k in text for k in ["555", "timer", "monostable", "astable"]):
                matched = "ELX-04"
            elif any(k in text for k in ["multiplexer", "mux", "demux", "decoder", "k-map", "boolean", "logic gate"]):
                matched = "ELX-05"
            elif any(k in text for k in ["flip-flop", "jk", "master-slave", "counter", "setup time", "hold time", "shift register"]):
                matched = "ELX-06"
            elif any(k in text for k in ["schmitt", "hysteresis"]):
                matched = "ELX-07"
            elif any(k in text for k in ["dac", "adc", "flash", "dual-slope", "resolution", "sar"]):
                matched = "ELX-08"
            elif any(k in text for k in ["feedback amplifier", "oscillator", "hartley", "colpitts", "wien bridge oscillator"]):
                matched = "ELX-02"
            elif any(k in text for k in ["cmos", "bjt", "mosfet", "diode", "zener"]):
                matched = "ELX-01"
            else:
                matched = "ELX-01"

        # 9. Microprocessors & Microcomputers
        elif "microprocessor" in subj:
            if any(k in text for k in ["instruction", "addressing", "call", "push", "pop", "mov", "lda"]):
                matched = "MPU-02"
            elif any(k in text for k in ["machine cycle", "t-state", "timing diagram", "opcode fetch"]):
                matched = "MPU-03"
            elif any(k in text for k in ["interrupt", "trap", "rst 7.5", "rst 6.5", "intr"]):
                matched = "MPU-04"
            elif any(k in text for k in ["dma", "hold", "hlda", "8257", "8237"]):
                matched = "MPU-05"
            elif any(k in text for k in ["8255", "ppi", "8254", "8259", "interfacing"]):
                matched = "MPU-06"
            elif any(k in text for k in ["8085", "8086", "architecture", "bus", "segment", "flag"]):
                matched = "MPU-01"
            else:
                matched = "MPU-01"

        # 10. Communication & Fiber Optics
        elif "communication" in subj or "fiber" in subj:
            if any(k in text for k in ["numerical aperture", "core", "cladding", "refractive index", "acceptance angle", "optical fiber"]):
                matched = "FIB-03"
            elif any(k in text for k in ["attenuation", "dispersion", "intermodal", "single mode", "multimode"]):
                matched = "FIB-02"
            elif any(k in text for k in ["laser", "photodetector", "pin diode", "avalanche"]):
                matched = "FIB-04"
            elif any(k in text for k in ["tdm", "fdm"]):
                matched = "FIB-01"
            elif any(k in text for k in ["delta modulation", "slope overload"]):
                matched = "DCM-02"
            elif any(k in text for k in ["pcm", "quantization", "companding", "sampling theorem"]):
                matched = "DCM-01"
            elif any(k in text for k in ["ask", "psk", "fsk", "bpsk", "qpsk"]):
                matched = "DCM-03"
            elif any(k in text for k in ["hamming", "parity", "block code"]):
                matched = "DCM-04"
            elif any(k in text for k in ["convolutional", "entropy", "shannon"]):
                matched = "DCM-05"
            elif any(k in text for k in ["osi", "layer", "tcp/ip", "packet"]):
                matched = "DCM-06"
            else:
                matched = "FIB-03"

        # 11. HVAC & Refrigeration
        elif "hvac" in subj or "refrigeration" in subj:
            if any(k in text for k in ["boiler", "hot water", "heating"]):
                matched = "HVC-01"
            elif any(k in text for k in ["chiller", "cop", "kw/tr", "centrifugal chiller", "screw chiller", "condenser"]):
                matched = "HVC-02"
            elif any(k in text for k in ["vrv", "vrf", "variable refrigerant"]):
                matched = "HVC-03"
            elif any(k in text for k in ["window", "split", "cassette"]):
                matched = "HVC-04"
            elif any(k in text for k in ["cooling tower", "ahu", "approach", "range", "psychrometric", "pac", "precision"]):
                matched = "HVC-05"
            else:
                matched = "HVC-02"

        # 12. Pumps & Fluid Mechanics
        elif "pump" in subj or "fluid" in subj:
            if any(k in text for k in ["positive displacement", "reciprocating"]):
                matched = "PMP-01"
            elif any(k in text for k in ["centrifugal pump", "impeller", "affinity laws", "specific speed"]):
                matched = "PMP-02"
            elif any(k in text for k in ["npsh", "cavitation"]):
                matched = "PMP-03"
            elif any(k in text for k in ["bernoulli", "continuity", "euler", "velocity potential"]):
                matched = "PMP-04"
            elif any(k in text for k in ["darcy", "head loss", "friction factor", "pipe"]):
                matched = "PMP-06"
            elif any(k in text for k in ["hydro-pneumatic", "booster"]):
                matched = "WTR-01"
            elif any(k in text for k in ["sewage", "stp", "ro plant", "water treatment"]):
                matched = "WTR-02"
            else:
                matched = "PMP-02"

        # 13. Airport Substation, DG & UPS
        elif "substation" in subj or "dg" in subj or "ups" in subj:
            if any(k in text for k in ["amf", "auto mains failure", "dg set", "governor", "droop"]):
                matched = "DGU-01"
            elif any(k in text for k in ["ups", "static switch", "inverter", "battery", "ah rating"]):
                matched = "DGU-03"
            elif any(k in text for k in ["scada", "power management", "pms"]):
                matched = "DGU-04"
            elif any(k in text for k in ["bus duct", "busbar", "apfc", "capacitor bank"]):
                matched = "SUB-03"
            elif any(k in text for k in ["lt switchboard", "air circuit breaker"]):
                matched = "SUB-02"
            elif any(k in text for k in ["transformer", "ccr", "constant current", "gpu", "aerobridge", "switchyard", "gravel"]):
                matched = "SUB-01"
            elif any(k in text for k in ["solar", "photovoltaic", "rooftop"]):
                matched = "REN-02"
            else:
                matched = "SUB-01"

        # 14. Fire Safety, Lifts & BMS
        elif "fire" in subj or "lift" in subj or "bms" in subj:
            if any(k in text for k in ["lift", "elevator", "safety gear", "overspeed", "counterweight", "ard"]):
                matched = "LFT-01"
            elif any(k in text for k in ["escalator", "inclination", "moving walk"]):
                matched = "LFT-02"
            elif any(k in text for k in ["bacnet", "modbus", "ddc", "bms", "ibms"]):
                matched = "BMS-01"
            elif any(k in text for k in ["sprinkler", "quartzoid", "bulb", "68 deg"]):
                matched = "FIR-03"
            elif any(k in text for k in ["clean agent", "fm-200", "novec", "gas suppression", "deluge"]):
                matched = "FIR-04"
            elif any(k in text for k in ["fire alarm", "smoke detector", "heat detector", "addressable"]):
                matched = "FIR-01"
            elif any(k in text for k in ["hydrant", "wet riser", "jockey pump"]):
                matched = "FIR-02"
            elif any(k in text for k in ["cctv", "camera", "nvr"]):
                matched = "SEC-01"
            elif any(k in text for k in ["public address", "pa system", "100v line"]):
                matched = "SEC-02"
            else:
                matched = "FIR-03"

        # 15. Contract Management & Safety Codes
        elif "contract" in subj or "safety" in subj:
            if any(k in text for k in ["tender", "nit", "emd", "earnest money", "security deposit", "pbg", "epc", "turnkey", "liquidated damages", "defect liability"]):
                matched = "CON-01"
            elif any(k in text for k in ["cpm", "pert", "critical path", "float", "total float", "free float", "crashing", "variance", "std dev"]):
                matched = "CON-02"
            elif any(k in text for k in ["is:732", "is 732", "cea", "regulation 34", "insulation resistance", "safety code", "ie rules"]):
                matched = "CON-05"
            elif any(k in text for k in ["breakdown", "preventive maintenance", "logbook"]):
                matched = "CON-04"
            else:
                matched = "CON-01"

        # 16. Utilization & Illumination
        elif "utilization" in subj or "illumination" in subj:
            if any(k in text for k in ["earthing", "is:3043", "pipe electrode", "plate electrode"]):
                matched = "ERT-01"
            elif any(k in text for k in ["lightning", "faraday cage", "early streamer", "is/iec 62305"]):
                matched = "ERT-02"
            elif any(k in text for k in ["ecbc", "energy conservation act", "bee"]):
                matched = "ECM-01"
            elif any(k in text for k in ["wiring", "conduit", "sub-circuit"]):
                matched = "ELE-01"
            elif any(k in text for k in ["mcb", "rccb", "rcbo", "elcb"]):
                matched = "ELE-02"
            elif any(k in text for k in ["lux", "lumen", "candela", "inverse square", "lambert", "maintenance factor", "runway light", "taxiway light", "papi"]):
                matched = "ELE-03"
            elif any(k in text for k in ["traction", "dielectric heating", "induction heating"]):
                matched = "ELE-03"
            else:
                matched = "ELE-03"

        # 17. General Non-Technical
        elif "general" in subj:
            if any(k in text for k in ["aai act", "icao", "dgca", "aviation"]):
                matched = "NTC-04"
            elif any(k in text for k in ["syllogism", "coding", "series", "reasoning", "analogy"]):
                matched = "NTC-02"
            elif any(k in text for k in ["work", "speed", "profit", "loss", "ratio", "arithmetic", "math"]):
                matched = "NTC-03"
            else:
                matched = "NTC-01"

        if matched and matched in topics:
            topic_mapping[matched].append(q["question_id"])
        else:
            unmapped_questions.append((q["question_id"], q["subject"], q.get("topic", "")))

    return topic_mapping, uncertain_relevance, unmapped_questions

def main():
    topics = parse_syllabus_topics()
    mapping, uncertain_relevance, unmapped = map_questions_to_topics(topics)
    
    verified_topics = {}
    limited_topics = {}
    zero_topics = {}

    for tid, tinfo in topics.items():
        q_count = len(mapping.get(tid, []))
        entry = {
            "topic_id": tid,
            "topic_name": tinfo["topic_name"],
            "subject": tinfo["subject"],
            "question_count": q_count,
            "sample_question_ids": mapping.get(tid, [])[:5]
        }
        if q_count >= 5:
            verified_topics[tid] = entry
        elif 1 <= q_count < 5:
            limited_topics[tid] = entry
        else:
            zero_topics[tid] = entry

    total_questions = sum(len(v) for v in mapping.values()) + len(uncertain_relevance) + len(unmapped)
    report_data = {
        "total_canonical_topics": len(topics),
        "total_questions_in_db": total_questions,
        "mapped_questions_count": sum(len(v) for v in mapping.values()),
        "uncertain_relevance_count": len(uncertain_relevance),
        "unmapped_questions_count": len(unmapped),
        "verified_coverage_topics_count": len(verified_topics),
        "limited_coverage_topics_count": len(limited_topics),
        "zero_coverage_topics_count": len(zero_topics),
        "verified_topics": verified_topics,
        "limited_topics": limited_topics,
        "zero_topics": zero_topics,
        "uncertain_relevance_questions": uncertain_relevance,
        "unmapped_questions": unmapped
    }

    with open(os.path.join(ROOT_DIR, "database", "syllabus_topic_audit.json"), "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=2)

    print("Refined syllabus audit data successfully saved to database/syllabus_topic_audit.json")
    print(f"Verified Topics: {len(verified_topics)} ({len(verified_topics)/len(topics)*100:.1f}%)")
    print(f"Limited Topics: {len(limited_topics)} ({len(limited_topics)/len(topics)*100:.1f}%)")
    print(f"Zero Topics: {len(zero_topics)} ({len(zero_topics)/len(topics)*100:.1f}%)")
    print(f"Uncertain Relevance Questions: {len(uncertain_relevance)}")

if __name__ == "__main__":
    main()
