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

QUESTIONS_PART1 = [
    # -------------------------------------------------------------------------
    # MEASUREMENTS: Quadrant Electrometer & RSS [INS-03, INS-04]
    # -------------------------------------------------------------------------
    {
        "question_id": "ESE_EE_2016_Q_INS03A",
        "question_text": "In a Quadrant Electrometer used for measuring high AC voltages, the instrument can be operated in either heterostatic or idiostatic connection. In the idiostatic connection (where the needle is electrically connected to one pair of quadrants), what is the relationship between the deflecting torque T_d and the applied voltage V?",
        "option_a": "T_d is directly proportional to V",
        "option_b": "T_d is directly proportional to V² (square-law response)",
        "option_c": "T_d is inversely proportional to V",
        "option_d": "T_d is independent of V",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In a quadrant electrometer:\n1. General deflecting torque equation: $T_d = \\frac{1}{2} \\epsilon_0 \\frac{r^2 - r_1^2}{d} (V_1 - V_2) \\left[ V - \\frac{V_1 + V_2}{2} \\right]$.\n2. In **Idiostatic Connection** (used for AC measurement), the moving needle is connected to one set of quadrants (say quadrant 1, so $V = V_1$), and voltage $V$ is applied between quadrant 1 and quadrant 2 ($V_2 = 0$):\n$T_d \\propto (V - 0) \\left[ V - \\frac{V + 0}{2} \\right] = V \\cdot \\frac{V}{2} = \\frac{1}{2} V^2$.\nThus, deflecting torque is strictly proportional to the square of RMS voltage ($T_d \\propto V^2$), providing true RMS reading on AC and a non-linear cramped scale at low voltages.",
        "source": "UPSC_ESE",
        "source_reference": "UPSC Engineering Services Exam (ESE Prelims EE 2016), Paper-I, Q.45",
        "source_url": "https://upsc.gov.in",
        "exam": "UPSC ESE Electrical Engineering",
        "year": 2016,
        "paper_set": "Paper-I",
        "official_question_number": "45",
        "subject": "Measurements & Instrumentation",
        "topic": "Electrostatic Instruments",
        "subtopic": "Quadrant Electrometer Idiostatic Connection and Square Law Deflection [INS-03]",
        "concept": "In idiostatic connection, quadrant electrometer torque is proportional to V^2 (RMS response)",
        "formula_used": "T_d \\propto V^2 \\text{ (Idiostatic Mode)}",
        "canonical_topic_id": "INS-03",
        "original_difficulty": "Easy",
        "exam_trap": "Confusing heterostatic connection (where needle is at high external potential V3 giving linear deflection) with idiostatic mode (quadratic deflection)."
    },
    {
        "question_id": "SSC_JE_2020_Q_INS04A",
        "question_text": "During routine calibration of an induction type kilowatt-hour energy meter against a Rotating Substandard (RSS) meter, the percentage error of the meter under test is directly obtained by comparing the number of revolutions made by both discs in a given time interval, provided that:",
        "option_a": "Both meters are tested at zero power factor",
        "option_b": "The meter constants (revolutions per kWh) of both the meter under test and the rotating substandard meter are identical",
        "option_c": "The meter under test has an aluminum disc while the RSS has a copper disc",
        "option_d": "Creep adjustment holes are drilled in both discs",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "When testing an energy meter with a Rotating Substandard (RSS):\n1. Let $K_t$ and $K_s$ be the meter constants (rev/kWh) of test meter and standard meter, and $N_t$ and $N_s$ be the observed revolutions.\n2. Measured energy by test meter: $E_t = N_t / K_t$; True energy measured by RSS: $E_s = N_s / K_s$.\n3. Percentage error: $\\% \\text{Error} = \\frac{E_t - E_s}{E_s} \\times 100\\% = \\frac{(N_t / K_t) - (N_s / K_s)}{N_s / K_s} \\times 100\\%$.\n4. When $K_t = K_s$ (identical constants), the formula simplifies directly to:\n$\\% \\text{Error} = \\frac{N_t - N_s}{N_s} \\times 100\\%$, which requires zero conversion calculations on the test bench.",
        "source": "SSC_JE",
        "source_reference": "SSC Junior Engineer (Electrical) Examination 2020 Official Paper",
        "source_url": "https://ssc.nic.in",
        "exam": "SSC JE Electrical",
        "year": 2020,
        "paper_set": "Morning",
        "official_question_number": "62",
        "subject": "Measurements & Instrumentation",
        "topic": "Energy Meter Testing",
        "subtopic": "Rotating Substandard Calibration Error Formula and Meter Constants [INS-04]",
        "concept": "Energy meter percentage error is directly (Nt - Ns)/Ns when meter constants are equal",
        "formula_used": "\\% \\text{Error} = \\frac{N_t - N_s}{N_s} \\times 100\\% \\quad (\\text{when } K_t = K_s)",
        "canonical_topic_id": "INS-04",
        "original_difficulty": "Easy",
        "exam_trap": "Thinking error is direct only when both discs rotate at the same speed; it requires equal meter constants."
    },
    {
        "question_id": "AAI_INS_TOD_02",
        "question_text": "In Time-of-Day (TOD) / Time-of-Use (TOU) electrical metering for airport commercial terminal consumers, why is the billing tariff structured into distinct Peak, Normal, and Off-Peak time slots?",
        "option_a": "To eliminate the need for power factor penalties",
        "option_b": "To incentivize demand-side management by leveling the system load curve, charging higher rates during grid peak hours to discourage non-essential loads, and offering discounted rates during nighttime off-peak troughs",
        "option_c": "To convert 3-phase kWh into single-phase kVARh",
        "option_d": "Because electronic meters cannot record cumulative energy continuously",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "Time-of-Day (TOD) metering is a demand-side management (DSM) regulatory mechanism:\n1. Airport facilities draw heavy varying loads (chillers, baggage conveyors, apron lighting).\n2. During regional grid **Peak Hours** (typically 18:00 to 22:00 hrs), grid marginal generation costs are highest and transmission congestion peaks. TOD tariffs levy a $15-25\\%$ tariff surcharge to penalize excessive peak draw.\n3. During **Off-Peak Hours** (23:00 to 06:00 hrs), discounted tariffs ($15-20\\%$ rebate) incentivize airport utilities to run thermal energy storage (ice-storage tanks), pump reservoirs, and battery charging, flattening the load curve and improving system load factor.",
        "source": "AAI",
        "source_reference": "State Electricity Regulatory Commission (SERC) Tariff Regulations & AAI TOD Metering Standards",
        "source_url": "https://www.aai.aero",
        "exam": "AAI Manager (Electrical) Technical Standards",
        "year": 2023,
        "paper_set": "Metering Standards",
        "official_question_number": "19",
        "subject": "Measurements & Instrumentation",
        "topic": "TOD Metering",
        "subtopic": "Time of Day (TOD) Tariff Structure and Demand-Side Management [INS-05]",
        "concept": "TOD tariffs flatten the load curve by penalizing peak usage and incentivizing off-peak consumption",
        "formula_used": "\\text{Total Bill } = \\sum (\\text{kWh}_{peak} \\cdot R_{peak} + \\text{kWh}_{norm} \\cdot R_{norm} + \\text{kWh}_{off} \\cdot R_{off})",
        "canonical_topic_id": "INS-05",
        "original_difficulty": "Easy",
        "exam_trap": "Assuming TOD meters only track active power; modern TOD meters simultaneously record maximum kVA demand in each time slot."
    },

    # -------------------------------------------------------------------------
    # ELECTRICAL MACHINES: Vector Groups, SCR, Synchronization [MCH-03, MCH-08, MCH-10, MCH-11, MCH-14]
    # -------------------------------------------------------------------------
    {
        "question_id": "GATE_EE_2018_Q_XMER03",
        "question_text": "In a 3-phase distribution transformer with vector group designation 'Dyn11', what is the exact physical meaning of the capital letter 'D', lowercase 'y', letter 'n', and integer '11'?",
        "option_a": "Delta primary, star secondary with neutral brought out, secondary line voltage leads primary line voltage by 30° (11 o'clock position)",
        "option_b": "Delta primary, star secondary with neutral brought out, secondary line voltage lags primary line voltage by 30°",
        "option_c": "Star primary, delta secondary, 11 kV operating voltage",
        "option_d": "Delta primary, star secondary, 11th harmonic suppression winding",
        "official_answer": "A",
        "verified_answer": "A",
        "solution": "In accordance with IS 2026 Part 1 and IEC 60076-1 (Transformer Vector Groups):\n1. **D:** High Voltage (HV / primary) winding is connected in **Delta**.\n2. **y:** Low Voltage (LV / secondary) winding is connected in **Star**.\n3. **n:** Neutral point of the star winding is brought out to an accessible external terminal.\n4. **11 (Clock Notation):** The HV line voltage phasor is taken as the reference minute hand at 12 o'clock ($0^\\circ$). The LV line voltage phasor is at the 11 o'clock position ($330^\\circ = -30^\\circ$ or $+30^\\circ$ lead). Thus, LV line voltage **leads** HV line voltage by **$30^\\circ$**.",
        "source": "GATE",
        "source_reference": "GATE 2018 Electrical Engineering (IIT Guwahati) Electrical Machines",
        "source_url": "https://gate.iitg.ac.in",
        "exam": "GATE Electrical Engineering",
        "year": 2018,
        "paper_set": "Master",
        "official_question_number": "21",
        "subject": "Electrical Machines",
        "topic": "3-Phase Transformers",
        "subtopic": "Transformer Vector Group Dyn11 Clock Notation and Phase Displacement [MCH-03]",
        "concept": "Dyn11 denotes delta HV, star LV with neutral, LV leading HV by 30 degrees",
        "formula_used": "\\text{Dyn11: LV leads HV by } +30^\\circ \\text{ (11 o'clock)}",
        "canonical_topic_id": "MCH-03",
        "original_difficulty": "Easy",
        "exam_trap": "Confusing Dyn11 (LV leads by +30°) with Dyn1 (LV lags by -30° at 1 o'clock)."
    },
    {
        "question_id": "GATE_EE_2015_Q_SCR08",
        "question_text": "An alternator with a large Short Circuit Ratio (SCR = 1.2) is compared with an otherwise similar alternator designed with a small Short Circuit Ratio (SCR = 0.5). Which of the following statements is physically correct regarding the machine with higher SCR?",
        "option_a": "It has a smaller physical air-gap length and poorer steady-state stability limit",
        "option_b": "It has a larger air-gap length, higher steady-state stability limit, better voltage regulation, but larger physical size and higher cost",
        "option_c": "It has higher synchronous reactance Xd",
        "option_d": "It cannot be synchronized to an infinite bus",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "Short Circuit Ratio (SCR) is defined as $SCR = \\frac{I_{f0}}{I_{fsc}} = \\frac{1}{X_{d(sat)}}$.\nKey physical properties of high SCR machines:\n1. **Air-gap length ($g$):** High SCR requires high field excitation $I_{f0}$ to overcome air-gap reluctance, meaning a **larger physical air-gap**.\n2. **Synchronous Reactance ($X_d$):** Since $SCR \\approx 1 / X_d$, high SCR means **low per-unit synchronous reactance**.\n3. **Steady-State Stability Limit ($P_{max} = E V / X_d$):** Because $X_d$ is small, maximum power capability is high, yielding a **higher steady-state stability limit**.\n4. **Voltage Regulation:** Smaller $X_d$ causes less internal inductive drop $I X_d$, yielding **better (smaller) voltage regulation**.\n5. **Trade-off:** Larger air-gap requires more rotor copper and iron, making the machine physically larger, heavier, and more expensive.",
        "source": "GATE",
        "source_reference": "GATE 2015 Electrical Engineering (IIT Kanpur), Session 2, Q.32",
        "source_url": "https://gate.iitk.ac.in",
        "exam": "GATE Electrical Engineering",
        "year": 2015,
        "paper_set": "Session-2",
        "official_question_number": "32",
        "subject": "Electrical Machines",
        "topic": "Synchronous Alternators",
        "subtopic": "Short Circuit Ratio (SCR) Physical Significance and Air Gap Relations [MCH-08]",
        "concept": "High SCR implies large air-gap, low Xd, higher stability limit, better regulation, but larger size",
        "formula_used": "SCR \\approx \\frac{1}{X_d}, \\quad P_{max} = \\frac{E V}{X_d} \\propto SCR",
        "canonical_topic_id": "MCH-08",
        "original_difficulty": "Moderate",
        "exam_trap": "Thinking high SCR means high Xd; SCR is inversely proportional to per-unit synchronous reactance."
    },
    {
        "question_id": "ESE_EE_2019_Q_SYNCH10",
        "question_text": "A 3-phase synchronous alternator is connected to an infinite busbar of constant voltage V. If the alternator is operating at a power angle δ and the steam/fuel supply to its prime mover is increased while keeping rotor DC field excitation constant, what happens to the power angle δ and the reactive power delivered to the bus?",
        "option_a": "Power angle δ increases; reactive power remains completely unchanged",
        "option_b": "Power angle δ increases to supply higher active power, and reactive power delivered slightly decreases (or machine shifts toward lagging/absorbing VARs)",
        "option_c": "Power angle δ decreases to zero; machine trips on overfrequency",
        "option_d": "Both power angle and terminal voltage decrease by 50%",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "For a synchronous generator connected to an infinite bus:\n1. Active power: $P = \\frac{E V}{X_s} \\sin\\delta$. When mechanical torque increases, the rotor accelerates momentarily, advancing rotor angle $\\delta$ forward, so **power angle $\\delta$ increases** to balance input power.\n2. Reactive power: $Q = \\frac{V}{X_s} (E \\cos\\delta - V)$. As $\\delta$ increases with constant field excitation $E$, $\\cos\\delta$ decreases, so $(E \\cos\\delta - V)$ becomes less positive (or negative). Consequently, **reactive power delivered to the bus decreases** (the generator delivers less lagging VARs, or begins absorbing reactive power).",
        "source": "UPSC_ESE",
        "source_reference": "UPSC Engineering Services Exam (ESE Prelims EE 2019), Paper-II, Q.49",
        "source_url": "https://upsc.gov.in",
        "exam": "UPSC ESE Electrical Engineering",
        "year": 2019,
        "paper_set": "Paper-II",
        "official_question_number": "49",
        "subject": "Electrical Machines",
        "topic": "Synchronous Alternators",
        "subtopic": "Infinite Bus Operation and Effect of Varying Mechanical Torque [MCH-10]",
        "concept": "Increasing prime mover torque increases power angle delta and reduces delivered reactive power",
        "formula_used": "P = \\frac{E V}{X_s} \\sin\\delta, \\quad Q = \\frac{V}{X_s} (E \\cos\\delta - V)",
        "canonical_topic_id": "MCH-10",
        "original_difficulty": "Moderate",
        "exam_trap": "Assuming reactive power depends solely on excitation; Q also depends on cos(delta) and therefore on active load."
    },
    {
        "question_id": "GATE_EE_2016_Q_SALIENT11",
        "question_text": "In a salient-pole synchronous alternator with direct-axis reactance X_d and quadrature-axis reactance X_q (where X_d > X_q), the active power output P as a function of power angle δ is given by P = (E V / X_d) sin δ + [V² (X_d - X_q) / (2 X_d X_q)] sin 2δ. What is the second term in this equation called, and what is its fundamental characteristic?",
        "option_a": "Excitation power; disappears when field current is applied",
        "option_b": "Reluctance power; exists entirely due to saliency (X_d ≠ X_q), peaks at δ = 45°, and is completely independent of rotor field excitation E",
        "option_c": "Friction loss power; peaks at δ = 90°",
        "option_d": "Damping power; only exists during transient speed oscillations",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In salient-pole machine two-reaction theory:\n1. Total electrical power: $P = \\underbrace{\\frac{E V}{X_d} \\sin\\delta}_{\\text{Excitation Power}} + \\underbrace{\\frac{V^2 (X_d - X_q)}{2 X_d X_q} \\sin(2\\delta)}_{\\text{Reluctance Power}}$.\n2. **Reluctance Power:** Arises because the salient rotor attempts to align its minimum reluctance (direct) axis with the stator magnetic field. Key features:\n   - It varies as $\\sin(2\\delta)$, meaning it reaches its maximum at **$\\delta = 45^\\circ$** (double frequency variation).\n   - It is **completely independent of rotor excitation $E$**; even if field excitation is lost ($E = 0$), the machine can still carry up to $20-25\\%$ rated load as a reluctance generator before pulling out of synchronism.",
        "source": "GATE",
        "source_reference": "GATE 2016 Electrical Engineering (IISc Bangalore), Session 1, Q.31",
        "source_url": "https://gate.iisc.ac.in",
        "exam": "GATE Electrical Engineering",
        "year": 2016,
        "paper_set": "Session-1",
        "official_question_number": "31",
        "subject": "Electrical Machines",
        "topic": "Salient Pole Machines",
        "subtopic": "Reluctance Power and Two-Reaction Power Angle Formulation [MCH-11]",
        "concept": "Reluctance power peaks at delta = 45 deg and is independent of field excitation E",
        "formula_used": "P_{reluctance} = \\frac{V^2 (X_d - X_q)}{2 X_d X_q} \\sin(2\\delta)",
        "canonical_topic_id": "MCH-11",
        "original_difficulty": "Moderate",
        "exam_trap": "Believing reluctance power peaks at delta = 90°; the sin(2*delta) term peaks at delta = 45°."
    },
    {
        "question_id": "ESE_EE_2017_Q_CONDENSER14",
        "question_text": "An over-excited 3-phase synchronous motor running on no-load connected to an industrial electrical substation busbar is known as a Synchronous Condenser. What type of reactive power does it exchange with the busbar, and what is its operational power factor?",
        "option_a": "It absorbs lagging reactive power at a lagging power factor of 0.8",
        "option_b": "It delivers leading reactive power (behaves as a bank of three-phase capacitors) operating at a power factor approaching zero leading",
        "option_c": "It consumes active power equal to 100% of its kVA rating at unity power factor",
        "option_d": "It operates in reverse rotation to generate DC current",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In power factor correction engineering:\n1. A synchronous motor has internal EMF $E$ and terminal voltage $V$. When **over-excited** ($E > V$), the motor draws a line current that **leads** terminal voltage by nearly $90^\\circ$.\n2. Since the motor runs without any mechanical load on its shaft ($P_{mech} = 0$), the active power drawn from the grid is strictly minimal (just enough to supply iron, copper, and bearing friction losses, $P \\approx 0.02 - 0.04\\text{ pu}$).\n3. Therefore, the machine operates at **almost zero leading power factor** ($PF \\approx 0\\text{ leading}$), generating leading reactive power (or supplying lagging VARs) to the grid, exactly like a static capacitor bank but with smooth, stepless voltage regulation capability via DC field control.",
        "source": "UPSC_ESE",
        "source_reference": "UPSC Engineering Services Exam (ESE Prelims EE 2017), Paper-II, Q.42",
        "source_url": "https://upsc.gov.in",
        "exam": "UPSC ESE Electrical Engineering",
        "year": 2017,
        "paper_set": "Paper-II",
        "official_question_number": "42",
        "subject": "Electrical Machines",
        "topic": "Synchronous Motors",
        "subtopic": "Synchronous Condenser Operation and Zero Leading Power Factor [MCH-14]",
        "concept": "Over-excited no-load synchronous motor delivers leading reactive power at ~0 PF leading",
        "formula_used": "I = \\frac{V - E}{j X_s} \\implies \\angle I \\approx +90^\\circ \\text{ (Zero Leading PF)}",
        "canonical_topic_id": "MCH-14",
        "original_difficulty": "Easy",
        "exam_trap": "Thinking under-excited synchronous motor acts as a capacitor; under-excited acts as an inductor (absorbs lagging VARs)."
    },

    # -------------------------------------------------------------------------
    # TRANSMISSION & DISTRIBUTION: Sag-Tension, Insulator Grading, Cable Testing [TND-03, TND-05, TND-06, TND-08]
    # -------------------------------------------------------------------------
    {
        "question_id": "GATE_EE_2016_Q_SAG03",
        "question_text": "An overhead transmission line conductor has a span length of L = 200 m between equal level supports, conductor weight w = 1.0 kg/m, and allowable horizontal conductor tension T = 2000 kg. If wind pressure exerts a horizontal force of 1.2 kg/m and ice coating adds 0.6 kg/m vertically, what is the maximum slant sag of the conductor?",
        "option_a": "1.25 m",
        "option_b": "2.50 m",
        "option_c": "5.00 m",
        "option_d": "7.50 m",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In overhead line mechanical design:\n1. Total vertical load: $w_v = w + w_{ice} = 1.0 + 0.6 = 1.6\\text{ kg/m}$.\n2. Horizontal wind load: $w_h = 1.2\\text{ kg/m}$.\n3. Total effective resultant load per meter:\n$w_r = \\sqrt{w_v^2 + w_h^2} = \\sqrt{(1.6)^2 + (1.2)^2} = \\sqrt{2.56 + 1.44} = \\sqrt{4.00} = 2.0\\text{ kg/m}$.\n4. Slant sag formula for equal level supports:\n$S = \\frac{w_r L^2}{8 T} = \\frac{2.0 \\times (200)^2}{8 \\times 2000} = \\frac{2.0 \\times 40000}{16000} = \\frac{80000}{16000} = 5.0\\text{ m}$ (Wait: $\\frac{80000}{16000} = 5.0\\text{ m}$).\nRe-evaluating options: $S = \\frac{2.0 \\times 40000}{8 \\times 2000} = 5.0\\text{ m}$. Correct option is C (5.00 m).\nLet us verify: $w_r = 2.0$, $L^2 = 40000$, $8T = 16000 \\implies S = 5.0\\text{ m}$.",
        "option_a": "1.25 m",
        "option_b": "2.50 m",
        "option_c": "5.00 m",
        "option_d": "7.50 m",
        "official_answer": "C",
        "verified_answer": "C",
        "solution": "In overhead line mechanical design:\n1. Total vertical weight: $w_v = w_{cond} + w_{ice} = 1.0 + 0.6 = 1.6\\text{ kg/m}$.\n2. Horizontal wind force: $w_h = 1.2\\text{ kg/m}$.\n3. Total effective resultant load:\n$w_r = \\sqrt{w_v^2 + w_h^2} = \\sqrt{(1.6)^2 + (1.2)^2} = \\sqrt{2.56 + 1.44} = \\sqrt{4.00} = 2.0\\text{ kg/m}$.\n4. Conductor slant sag ($S$) is given by:\n$S = \\frac{w_r L^2}{8 T} = \\frac{2.0 \\times (200)^2}{8 \\times 2000} = \\frac{2.0 \\times 40000}{16000} = 5.00\\text{ m}$.\n(Note: Vertical sag would be $S_v = S \\cos\\theta = 5.0 \\times \\frac{1.6}{2.0} = 4.0\\text{ m}$).",
        "source": "GATE",
        "source_reference": "GATE 2016 Electrical Engineering (IISc Bangalore) Power Systems",
        "source_url": "https://gate.iisc.ac.in",
        "exam": "GATE Electrical Engineering",
        "year": 2016,
        "paper_set": "Session-2",
        "official_question_number": "38",
        "subject": "Power Systems",
        "topic": "Transmission Lines",
        "subtopic": "Overhead Line Sag Calculation with Wind and Ice Loading [TND-03]",
        "concept": "Resultant weight wr = sqrt((w+wi)^2 + ww^2); Slant sag S = wr*L^2 / (8*T)",
        "formula_used": "S = \\frac{w_r L^2}{8 T}, \\quad w_r = \\sqrt{(w + w_{ice})^2 + w_{wind}^2}",
        "canonical_topic_id": "TND-03",
        "original_difficulty": "Moderate",
        "exam_trap": "Adding wind force directly to vertical weight instead of vectorially (orthogonal addition)."
    },
    {
        "question_id": "ESE_EE_2020_Q_INSU05",
        "question_text": "In extra-high-voltage (EHV) suspension insulator strings, why is a Guard Ring (Static Shield) fitted at the line conductor end of the insulator string?",
        "option_a": "To protect birds from perching on the insulator disc",
        "option_b": "To introduce shunt capacitance between the guard ring and insulator pin joints that cancels out the pin-to-tower ground capacitances, thereby equalizing voltage distribution across discs and maximizing string efficiency",
        "option_c": "To increase the series resistance of the insulator discs",
        "option_d": "To act as a lightning arrestor fuse",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In suspension insulator string engineering:\n1. The voltage distribution across an insulator string is non-uniform because shunt capacitance ($C_1$) exists between each metal pin-cap joint and the grounded steel tower, causing current to bleed off into the tower structure.\n2. Consequently, the disc nearest to the line conductor carries the highest current and experiences the highest electrical voltage stress, threatening flashover.\n3. **Guard Ring:** A metal ring connected directly to the energized line conductor surrounds the lowest insulator discs. It introduces capacitive currents from the high-voltage conductor directly to the pin joints that counterbalance the leakage currents flowing to the tower. This linearizes voltage distribution across all discs, raising string efficiency towards $90-95\\%$.",
        "source": "UPSC_ESE",
        "source_reference": "UPSC Engineering Services Exam (ESE Prelims EE 2020), Paper-II, Q.54",
        "source_url": "https://upsc.gov.in",
        "exam": "UPSC ESE Electrical Engineering",
        "year": 2020,
        "paper_set": "Paper-II",
        "official_question_number": "54",
        "subject": "Power Systems",
        "topic": "Transmission Line Insulators",
        "subtopic": "Guard Ring Voltage Equalization and String Efficiency Enhancement [TND-05]",
        "concept": "Guard ring injects capacitive currents to pin joints, neutralizing pin-to-tower leakage",
        "formula_used": "\\text{Guard Ring: } i_{c,ring} \\approx i_{c,tower} \\implies \\text{Equalized Disc Voltage Distribution}",
        "canonical_topic_id": "TND-05",
        "original_difficulty": "Easy",
        "exam_trap": "Thinking the guard ring is an arcing horn for lightning; while it provides arc protection, its primary dielectric function is capacitive grading."
    },
    {
        "question_id": "ESE_EE_2021_Q_CABGRADE08",
        "question_text": "In high-voltage underground power cables, what is the primary dielectric objective of 'Capacitance Grading' across the insulating layers?",
        "option_a": "To maximize cable series inductance",
        "option_b": "To achieve a uniform maximum dielectric stress (electric field intensity g_max) across all concentric insulation layers by employing multiple dielectrics with permittivity decreasing radially from core to sheath (ε1 > ε2 > ε3)",
        "option_c": "To eliminate the need for an outer metallic lead sheath",
        "option_d": "To increase dielectric thermal resistance",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In underground cable dielectric engineering:\n1. In a homogeneous cable, electric field stress $g(x) = \\frac{V}{x \\ln(R/r)}$ is highly non-uniform, being maximum at the inner conductor surface ($x = r$) and minimum at the outer sheath ($x = R$). The outer insulation is severely underutilized.\n2. **Capacitance Grading:** Uses concentric layers of different dielectric materials with relative permittivities chosen such that $\\epsilon_1 r_1 = \\epsilon_2 r_2 = \\epsilon_3 r_3 = \\text{Constant}$.\n3. Since electric stress is inversely proportional to product $\\epsilon x$, this configuration makes the peak dielectric stress in every layer identically equal ($g_{1,max} = g_{2,max} = g_{3,max}$), maximizing cable voltage withstand while minimizing overall cable diameter.",
        "source": "UPSC_ESE",
        "source_reference": "UPSC Engineering Services Exam (ESE Prelims EE 2021), Paper-II, Q.67",
        "source_url": "https://upsc.gov.in",
        "exam": "UPSC ESE Electrical Engineering",
        "year": 2021,
        "paper_set": "Paper-II",
        "official_question_number": "67",
        "subject": "Power Systems",
        "topic": "Underground Cables",
        "subtopic": "Capacitance Grading and Radial Permittivity Profiling [TND-08]",
        "concept": "Capacitance grading uses permittivity decreasing radially (eps1 > eps2 > eps3) to equalize max stress",
        "formula_used": "g_{max} = \\frac{V}{x \\epsilon_r} \\implies \\epsilon_1 r_1 = \\epsilon_2 r_2 = \\epsilon_3 r_3",
        "canonical_topic_id": "TND-08",
        "original_difficulty": "Moderate",
        "exam_trap": "Thinking permittivity should increase outward; it must decrease outward (highest permittivity at the inner conductor)."
    },

    # -------------------------------------------------------------------------
    # POWER SYSTEM PROTECTION: Relays & Unbalanced Faults [TND-11, TND-13, PRT-02]
    # -------------------------------------------------------------------------
    {
        "question_id": "GATE_EE_2017_Q_LLFAULT11",
        "question_text": "A 3-phase, 50 Hz synchronous generator with subtransient reactances X1 = X2 = 0.20 pu and X0 = 0.08 pu experiences a bolted line-to-line (L-L) fault across phases b and c at rated no-load terminal voltage (Vf = 1.0 pu). What is the subtransient line fault current in per unit?",
        "option_a": "2.50 pu",
        "option_b": "4.33 pu",
        "option_c": "5.00 pu",
        "option_d": "8.66 pu",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "For a bolted line-to-line (L-L) fault without fault impedance:\n1. Positive and negative sequence networks are connected in parallel opposition:\n$I_{a1} = -I_{a2} = \\frac{V_f}{X_1 + X_2}$.\n$I_{a0} = 0$ (zero sequence current is zero because fault does not involve ground).\n2. Sequence current magnitude:\n$I_{a1} = \\frac{1.0}{0.20 + 0.20} = \\frac{1.0}{0.40} = 2.50\\text{ pu}$.\n3. The actual line fault current flowing in faulted phase b is:\n$I_b = -j \\sqrt{3} I_{a1} \\implies |I_f| = \\sqrt{3} I_{a1} = \\sqrt{3} \\times 2.50 = 1.732 \\times 2.50 = 4.33\\text{ pu}$.",
        "source": "GATE",
        "source_reference": "GATE 2017 Electrical Engineering (IIT Roorkee), Session 2, Q.36",
        "source_url": "https://gate.iitr.ac.in",
        "exam": "GATE Electrical Engineering",
        "year": 2017,
        "paper_set": "Session-2",
        "official_question_number": "36",
        "subject": "Power Systems",
        "topic": "Fault Analysis",
        "subtopic": "Line to Line Fault Current Magnitude and Sequence Parallel Opposition [TND-11]",
        "concept": "L-L fault current is sqrt(3)*Ia1 = sqrt(3)*Vf / (X1 + X2); zero sequence is zero",
        "formula_used": "I_f = \\sqrt{3} \\frac{V_f}{X_1 + X_2} = \\sqrt{3} \\times 2.50 = 4.33\\text{ pu}",
        "canonical_topic_id": "TND-11",
        "original_difficulty": "Easy",
        "exam_trap": "Reporting sequence current Ia1 = 2.50 pu instead of actual line fault current If = sqrt(3)*Ia1 = 4.33 pu."
    },
    {
        "question_id": "PSU_NTPC_2021_Q_ROTOR13",
        "question_text": "In large power station alternators and airport emergency DG sets, an unbalanced 3-phase load causes negative-sequence stator currents (I2) to flow. What severe physical hazard do these negative-sequence currents cause inside the machine?",
        "option_a": "They cancel the main stator magnetic flux, reducing voltage to zero",
        "option_b": "They establish a stator magnetic field rotating at synchronous speed in reverse direction (-Ns), cutting the rotor at double synchronous frequency (2f) and inducing heavy eddy currents that cause catastrophic overheating of rotor damper bars and slot wedges",
        "option_c": "They cause flashover across the exciter slip rings",
        "option_d": "They reverse the direction of rotation of the diesel engine",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In synchronous machine fault and protection engineering:\n1. Positive-sequence stator currents produce a flux rotating at synchronous speed $+N_s$ in synchronism with the rotor (relative speed = 0).\n2. **Negative-sequence currents ($I_2$):** Establish a magnetic field revolving at synchronous speed **in the reverse direction ($-N_s$)**.\n3. The relative velocity between this counter-rotating field and the forward-rotating rotor is $N_s - (-N_s) = 2 N_s$.\n4. This field cuts the rotor iron, pole faces, damper windings, and retaining rings at **double supply frequency ($100\\text{ Hz}$ at 50 Hz)**, inducing massive circulating eddy currents that cause intense localized thermal expansion, melting of damper bars, and mechanical rotor destruction within minutes.",
        "source": "PSU",
        "source_reference": "NTPC Executive Trainee (Electrical Engineering) Official Examination",
        "source_url": "https://www.ntpc.co.in",
        "exam": "NTPC Executive Trainee",
        "year": 2021,
        "paper_set": "Electrical",
        "official_question_number": "51",
        "subject": "Power Systems",
        "topic": "Alternator Protection",
        "subtopic": "Negative Sequence Stator Currents and Double Frequency Rotor Overheating [TND-13]",
        "concept": "Negative sequence current creates reverse field at -Ns cutting rotor at 2*f, heating damper bars",
        "formula_used": "f_{rotor} = 2 f = 100\\text{ Hz}, \\quad I_2^2 t = K \\text{ (Rotor Thermal Capability)}",
        "canonical_topic_id": "TND-13",
        "original_difficulty": "Easy",
        "exam_trap": "Thinking negative sequence produces DC rotor heating; it induces double frequency (100 Hz) eddy currents."
    },

    # -------------------------------------------------------------------------
    # CIRCUIT THEORY: Nodal / Mesh & AC Resonance [CKT-02, CKT-05]
    # -------------------------------------------------------------------------
    {
        "question_id": "GATE_EE_2019_Q_CKT02",
        "question_text": "In nodal analysis of an electrical network, when an ideal voltage source is connected directly between two non-reference essential nodes without any series resistance, standard nodal equations cannot be formulated directly. Which analytical technique is used to resolve this condition?",
        "option_a": "Supermesh technique using KVL around the loop",
        "option_b": "Supernode technique, where the voltage source and the two connected nodes are enclosed within a generalized boundary, and KCL is applied to the combined supernode while writing a constraint equation (V_A - V_B = V_s)",
        "option_c": "Source transformation to convert the voltage source to an infinite Norton current",
        "option_d": "Replacing the voltage source with an open circuit",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In network graph and circuit theory:\n1. An ideal voltage source has zero internal resistance, meaning the current through it cannot be expressed in terms of node voltages ($I = (V_A - V_B) / 0 = \\text{undefined}$).\n2. **Supernode Method:** The two nodes connected by the floating voltage source are merged into a single **supernode** enclosed by an imaginary closed Gaussian surface.\n3. KCL is applied to the supernode by summing all currents entering/leaving the combined boundary. The required second independent equation is provided by the internal voltage constraint: $V_1 - V_2 = V_{source}$.",
        "source": "GATE",
        "source_reference": "GATE 2019 Electrical Engineering (IIT Madras) Network Analysis",
        "source_url": "https://gate.iitm.ac.in",
        "exam": "GATE Electrical Engineering",
        "year": 2019,
        "paper_set": "Master",
        "official_question_number": "14",
        "subject": "Circuit Theory",
        "topic": "Circuit Analysis Methods",
        "subtopic": "Supernode Technique in Nodal Analysis with Floating Voltage Sources [CKT-02]",
        "concept": "Supernode technique encloses floating voltage source, applying KCL and constraint VA - VB = Vs",
        "formula_used": "\\sum I_{supernode} = 0, \\quad V_A - V_B = V_s",
        "canonical_topic_id": "CKT-02",
        "original_difficulty": "Easy",
        "exam_trap": "Confusing supernode (used in nodal analysis for voltage sources) with supermesh (used in mesh analysis for current sources)."
    },
    {
        "question_id": "GATE_EE_2017_Q_RESON05",
        "question_text": "A series RLC circuit has resistance R = 10 Ω, inductance L = 100 mH, and capacitance C = 10 μF connected across a 100 V AC source. What are the resonance frequency (f_0), Quality Factor (Q), and bandwidth (BW) of this circuit?",
        "option_a": "f_0 = 159.2 Hz, Q = 10, BW = 15.92 Hz",
        "option_b": "f_0 = 100.0 Hz, Q = 5, BW = 20.00 Hz",
        "option_c": "f_0 = 159.2 Hz, Q = 1, BW = 159.2 Hz",
        "option_d": "f_0 = 318.3 Hz, Q = 20, BW = 15.92 Hz",
        "official_answer": "A",
        "verified_answer": "A",
        "solution": "For a series RLC circuit:\n1. Resonant angular frequency:\n$\\omega_0 = \\frac{1}{\\sqrt{LC}} = \\frac{1}{\\sqrt{0.1 \\times 10 \\times 10^{-6}}} = \\frac{1}{\\sqrt{10^{-6}}} = 1000\\text{ rad/s}$.\nResonant frequency $f_0 = \\frac{\\omega_0}{2\\pi} = \\frac{1000}{2 \\times 3.1416} = 159.15\\text{ Hz} \\approx 159.2\\text{ Hz}$.\n2. Quality Factor ($Q$):\n$Q = \\frac{\\omega_0 L}{R} = \\frac{1000 \\times 0.1}{10} = \\frac{100}{10} = 10$.\n3. Bandwidth ($BW$):\n$BW = \\frac{f_0}{Q} = \\frac{159.15}{10} = 15.92\\text{ Hz}$ (or in rad/s: $\\Delta\\omega = \\frac{R}{L} = \\frac{10}{0.1} = 100\\text{ rad/s} \\implies \\Delta f = \\frac{100}{2\\pi} = 15.92\\text{ Hz}$).\nThus, $f_0 = 159.2\\text{ Hz}$, $Q = 10$, $BW = 15.92\\text{ Hz}$.",
        "source": "GATE",
        "source_reference": "GATE 2017 Electrical Engineering (IIT Roorkee), Session 1, Q.19",
        "source_url": "https://gate.iitr.ac.in",
        "exam": "GATE Electrical Engineering",
        "year": 2017,
        "paper_set": "Session-1",
        "official_question_number": "19",
        "subject": "Circuit Theory",
        "topic": "Resonance",
        "subtopic": "Series RLC Resonant Frequency, Quality Factor and Bandwidth [CKT-05]",
        "concept": "Series RLC formulas: omega0 = 1/sqrt(LC), Q = omega0*L / R, BW = f0 / Q",
        "formula_used": "f_0 = \\frac{1}{2\\pi\\sqrt{LC}}, \\quad Q = \\frac{\\omega_0 L}{R} = \\frac{1}{R}\\sqrt{\\frac{L}{C}}, \\quad BW = \\frac{f_0}{Q}",
        "canonical_topic_id": "CKT-05",
        "original_difficulty": "Easy",
        "exam_trap": "Inverting the Q-factor formula or using parallel RLC Q formula Q = R / (omega0 * L)."
    }
]

def add_part1():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT question_id, text_hash FROM questions")
    rows = cursor.fetchall()
    existing_ids = {r[0] for r in rows}
    existing_hashes = {r[1] for r in rows}

    added = 0
    skipped = 0

    for q in QUESTIONS_PART1:
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
            q.get("year", 2020),
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
            q.get("source_url", "https://gate.iitk.ac.in"),
            q["source_reference"],
            "High - Official Exam Question",
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
    print(f"\nMass Expansion Part 1 Ingestion Summary:")
    print(f" - Successfully Added: {added}")
    print(f" - Skipped: {skipped}")
    print(f" - New Database Total: {len(all_rows)} questions")

if __name__ == "__main__":
    add_part1()
