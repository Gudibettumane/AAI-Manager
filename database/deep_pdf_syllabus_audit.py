import sqlite3
import json
import re
import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(ROOT_DIR, "database", "question_database.db")

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute('SELECT question_id, subject, topic, subtopic, concept, question_text FROM questions')
all_q = [dict(r) for r in c.fetchall()]
conn.close()

# Specific syllabus terms extracted directly from the 4-page official PDF
pdf_syllabus_topics = [
    # Part-B Section 1: Circuit Theory
    ('Circuit Theory', 'network graphs (trees, twigs, links, cut-sets, incidence)', ['graph', 'tree', 'twig', 'cut-set', 'tie-set', 'incidence']),
    ('Circuit Theory', 'coupled circuits & dot convention', ['coupled', 'dot convention', 'mutual inductance']),
    ('Circuit Theory', 'balanced 3-phase circuits & two-port networks', ['two-port', 'z-parameter', 'y-parameter', 'abcd', 'h-parameter', '3-phase']),
    
    # Part-B Section 3: Instrumentation
    ('Measurements', 'Quadrant electrometer', ['quadrant electrometer', 'quadrant']),
    ('Measurements', 'Rotating substandard (RSS) & phantom loading', ['rotating substandard', 'rss']),
    ('Measurements', 'TOD meter (Time of Day metering)', ['tod', 'time of day']),
    
    # Part-B Section 4: Electrical Machines
    ('Electrical Machines', 'Scott connection of transformers', ['scott connection', 'tee connection']),
    ('Electrical Machines', 'short circuit ratio (SCR) and importance', ['short circuit ratio', 'scr']),
    ('Electrical Machines', 'round rotor vs salient pole phasor diagrams (Xd, Xq)', ['salient', 'two reaction', 'xd', 'xq']),
    ('Electrical Machines', 'synchronous condensers & V-curves', ['synchronous condenser', 'v curve', 'inverted v']),
    
    # Part-B Section 6: Transmission & Distribution
    ('Power Systems', 'Tuned Power Lines (quarter wave, half wave lines)', ['tuned power line', 'quarter wave', 'half wave line']),
    ('Power Systems', 'Insulator potential distribution & string efficiency', ['string efficiency', 'suspension insulator', 'guard ring']),
    ('Power Systems', 'Cable grading (capacitance & intersheath grading)', ['capacitance grading', 'intersheath grading', 'grading of cable']),
    ('Power Systems', 'Cable testing & power frequency withstand tests', ['withstand test', 'testing of cable', 'cable capacitance']),
    ('Power Systems', 'Protection against loss of excitation & prime mover failure', ['loss of excitation', 'reverse power', 'prime mover failure']),
    ('Power Systems', 'Circuit Breakers (Air-blast, Minimum oil, SF6, DC CB)', ['air-blast', 'minimum oil', 'sf6', 'dc circuit breaker']),
    
    # Part-B Section 8 & 9: Microprocessors & Electronics
    ('Microprocessors', 'Programmable peripheral devices (8255 PPI, 8254, 8259)', ['8255', 'ppi', '8254', '8259', 'peripheral']),
    ('Electronics', 'VCOs (Voltage Controlled Oscillators)', ['vco', 'voltage controlled oscillator']),
    ('Electronics', 'Sample and Hold circuits', ['sample and hold', 'sample-and-hold']),
    
    # Part-B Section 11 & 12: Communication & Fiber
    ('Communication', 'Lasers and optoelectronics materials', ['laser', 'photodetector', 'pin diode', 'avalanche']),
    ('Communication', 'Differential PCM (DPCM) & Delta Modulation (DM)', ['dpcm', 'delta modulation', 'slope overload']),
    ('Communication', 'Linear block codes & Convolution codes', ['block code', 'convolution code', 'hamming code']),
    
    # Part-B Section 13: HVAC
    ('HVAC', 'Heating Plant (Boilers / Hot Water Generators)', ['boiler', 'hot water generator']),
    ('HVAC', 'Precision Air Conditioning (PAC) for server/ATC rooms', ['precision air', 'pac']),
    ('HVAC', 'Unitary AC (Window, Split, Cassette, Tower AC)', ['cassette', 'tower ac', 'split ac', 'window ac']),
    ('HVAC', 'Cooling towers (Range & Approach, Drift loss)', ['cooling tower', 'approach', 'range', 'drift loss']),
    
    # Part-B Section 14: Pumps & Hydraulics
    ('Pumps', 'Specific speed of pumps & affinity laws', ['specific speed', 'affinity law']),
    ('Pumps', 'Kinematics of fluid flow & Euler equation', ['euler', 'continuity equation', 'streamline']),
    ('Pumps', 'Open channel flow & hydraulic jump energy loss', ['open channel', 'hydraulic jump']),
    ('Pumps', 'Measurement of discharge in pipes & open channels (Venturimeter, Orifice)', ['venturimeter', 'orifice', 'discharge measurement']),
    
    # Additional Topics Section 1: Contract Management
    ('Contracts', 'WBS, Milestones, Bar charts and CPM basics', ['work breakdown structure', 'wbs', 'bar chart', 'milestone', 'cpm', 'pert']),
    ('Contracts', 'Site management, manpower planning, inspection & quality control', ['site management', 'manpower', 'quality control', 'inspection']),
    ('Contracts', 'Breakdown & Preventive Maintenance schedule & electrical store', ['preventive maintenance', 'breakdown maintenance', 'electrical store', 'inventory']),
    
    # Additional Topics Section 2 & 3: Substation, DG & UPS
    ('Substation', 'HT overhead Lines & HT cables', ['ht cable', 'ht overhead', '11 kv cable', '33 kv cable']),
    ('Substation', 'Bus Duct, APFC Capacitor panels, Cable Trench & Cable Trays', ['bus duct', 'capacitor panel', 'apfc', 'cable trench', 'cable tray']),
    ('DG/UPS', 'AMF Panel & Auto-transfer switching', ['amf', 'auto mains failure']),
    ('DG/UPS', 'SCADA & Power Supply Management System in airport terminal', ['scada', 'power management system', 'pms', 'iec 61850']),
    
    # Additional Topics Section 4 to 11: MEP Facilities
    ('MEP', 'Lifts: Safety gear, overspeed governor, counterweight, ARD', ['safety gear', 'overspeed governor', 'counterweight', 'ard']),
    ('MEP', 'Escalators: Inclination angles (30/35 deg), safety switches', ['escalator', 'travelator', 'moving walk']),
    ('MEP', 'BMS / IBMS (Building Management System DDC controllers, BACnet)', ['bms', 'ibms', 'bacnet', 'ddc']),
    ('MEP', 'Water Supply: STP, WTP, RO Plant effluent recycling', ['stp', 'wtp', 'ro plant', 'sewage treatment']),
    ('MEP', 'Fire Safety: Wet Riser, Down Comer, Sprinklers, Clean Agent FM-200', ['wet riser', 'down comer', 'sprinkler', 'clean agent', 'fm-200', 'novec']),
    ('MEP', 'External Lighting: Street light poles, High Mast Towers', ['street light', 'high mast', 'lighting pole']),
    ('MEP', 'CCTV & Public Address (PA) Systems (100V line, NVR, cameras)', ['cctv', 'public address', 'pa system', '100v line'])
]

print("=== EXACT AUDIT OF 4-PAGE OFFICIAL SYLLABUS TOPICS ===")
header = f"{'Subject':<16} | {'Official Syllabus Item':<60} | {'Count':<6}"
print(header)
print("-" * len(header))

low_coverage_items = []
for subj, item_name, keywords in pdf_syllabus_topics:
    matching_ids = []
    for q in all_q:
        qtext = (q['question_text'] + ' ' + q.get('topic','') + ' ' + q.get('subtopic','') + ' ' + q.get('concept','')).lower()
        if any(kw in qtext for kw in keywords):
            matching_ids.append(q['question_id'])
    count = len(matching_ids)
    print(f"{subj:<16} | {item_name[:58]:<60} | {count:<6}")
    if count < 3:
        low_coverage_items.append((subj, item_name, count, keywords))

print("\nTotal audited syllabus focal items:", len(pdf_syllabus_topics))
print("Items with fewer than 3 questions (Need expansion):", len(low_coverage_items))
print("\nItems with < 3 questions:")
for subj, item_name, count, _ in low_coverage_items:
    print(f"  - [{subj}] {item_name}: Only {count} question(s)")
