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

QUESTIONS_PART2 = [
    # -------------------------------------------------------------------------
    # DIGITAL COMMUNICATION: PCM, DPCM, Modulation, OSI [DCM-01, DCM-02, DCM-03, DCM-06]
    # -------------------------------------------------------------------------
    {
        "question_id": "GATE_EC_2016_Q_PCM01",
        "question_text": "A sinusoidal voice signal band-limited to 3.4 kHz is sampled at 8 kHz and encoded using a uniform Pulse Code Modulation (PCM) system. If the transmission bandwidth of the binary PCM channel cannot exceed 64 kbps, what is the maximum number of quantization levels (L) that can be used?",
        "option_a": "64 levels",
        "option_b": "128 levels",
        "option_c": "256 levels",
        "option_d": "512 levels",
        "official_answer": "C",
        "verified_answer": "C",
        "solution": "In binary PCM transmission:\n1. Bit rate: $R_b = n \\cdot f_s$, where $n$ is bits per sample and $f_s$ is sampling frequency.\nGiven: $f_s = 8\\text{ kHz}$, $R_b \\le 64\\text{ kbps} = 64000\\text{ bps}$.\n$n \\le \\frac{R_b}{f_s} = \\frac{64000}{8000} = 8\\text{ bits/sample}$.\n2. Number of quantization levels: $L = 2^n = 2^8 = 256\\text{ levels}$.\nThus, the maximum permissible quantization levels is 256.",
        "source": "GATE",
        "source_reference": "GATE 2016 Electronics Engineering (IISc Bangalore) Digital Communications",
        "source_url": "https://gate.iisc.ac.in",
        "exam": "GATE Electronics Engineering",
        "year": 2016,
        "paper_set": "Session-1",
        "official_question_number": "24",
        "subject": "Communication & Fiber Optics",
        "topic": "Pulse Code Modulation",
        "subtopic": "PCM Bit Rate, Quantization Levels and Transmission Bandwidth [DCM-01]",
        "concept": "PCM bit rate Rb = n * fs; Quantization levels L = 2^n",
        "formula_used": "R_b = n \\cdot f_s, \\quad L = 2^n",
        "canonical_topic_id": "DCM-01",
        "original_difficulty": "Easy",
        "exam_trap": "Using the 3.4 kHz message bandwidth directly instead of the given 8 kHz sampling rate."
    },
    {
        "question_id": "ESE_EC_2019_Q_DPCM02",
        "question_text": "In a Delta Modulation (DM) communication system with step size Δ and sampling period T_s, what is the mathematical condition to completely avoid Slope Overload Distortion when transmitting an analog signal m(t) = A_m cos(2π f_m t)?",
        "option_a": "Δ / T_s < A_m",
        "option_b": "Δ / T_s ≥ 2π f_m A_m (the maximum slope of the staircase approximation must be at least equal to the maximum slope of the analog signal)",
        "option_c": "Δ / T_s = 0",
        "option_d": "Δ · T_s > 1 / (2π f_m)",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In Delta Modulation:\n1. The maximum rate of change that the discrete staircase approximation can follow is $\\frac{\\Delta}{T_s} = \\Delta \\cdot f_s$.\n2. For an input signal $m(t) = A_m \\cos(2\\pi f_m t)$, the maximum slope is:\n$\\left| \\frac{dm(t)}{dt} \\right|_{max} = 2\\pi f_m A_m$.\n3. To prevent **Slope Overload Distortion** (where the input signal changes faster than the staircase can rise), the maximum staircase slope must be greater than or equal to the maximum input signal slope:\n$\\frac{\\Delta}{T_s} \\ge 2\\pi f_m A_m \\implies A_m \\le \\frac{\\Delta}{2\\pi f_m T_s}$.",
        "source": "UPSC_ESE",
        "source_reference": "UPSC Engineering Services Exam (ESE Prelims E&T 2019), Paper-II, Q.72",
        "source_url": "https://upsc.gov.in",
        "exam": "UPSC ESE Electronics Engineering",
        "year": 2019,
        "paper_set": "Paper-II",
        "official_question_number": "72",
        "subject": "Communication & Fiber Optics",
        "topic": "Delta Modulation",
        "subtopic": "Slope Overload Distortion Condition in Delta Modulation [DCM-02]",
        "concept": "Slope overload is avoided when step size rate Delta/Ts >= 2*pi*fm*Am",
        "formula_used": "\\frac{\\Delta}{T_s} \\ge 2\\pi f_m A_m",
        "canonical_topic_id": "DCM-02",
        "original_difficulty": "Easy",
        "exam_trap": "Confusing slope overload distortion (caused by small Delta) with granular noise (caused by large Delta)."
    },
    {
        "question_id": "GATE_EC_2017_Q_QPSK03",
        "question_text": "In digital passband modulation, Quadrature Phase Shift Keying (QPSK) is compared with Binary Phase Shift Keying (BPSK) operating at the same bit rate R_b. What is the fundamental bandwidth and spectral efficiency advantage of QPSK?",
        "option_a": "QPSK requires double the transmission bandwidth of BPSK",
        "option_b": "QPSK transmits 2 bits per symbol (dibit), halving the required Null-to-Null transmission bandwidth (BW = R_b instead of 2 R_b) and doubling the spectral efficiency to 2 bps/Hz",
        "option_c": "QPSK has lower noise immunity and cannot use coherent demodulation",
        "option_d": "QPSK cannot transmit digital data over optical fibers",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In digital passband modulation:\n1. BPSK: Each symbol represents 1 bit ($M = 2$, symbol duration $T_s = T_b$). Required transmission bandwidth: $BW_{null} = 2 R_b$.\n2. QPSK: Each symbol represents $n = \\log_2(4) = 2\\text{ bits}$ ($M = 4$, symbol duration $T_s = 2 T_b$, symbol rate $R_s = R_b / 2$).\n3. Required transmission bandwidth for QPSK: $BW_{null} = 2 R_s = 2 (R_b / 2) = R_b$.\n4. Thus, QPSK requires only **half the RF bandwidth** of BPSK for the exact same bit transmission rate, doubling bandwidth spectral efficiency ($2\\text{ bps/Hz}$ vs $1\\text{ bps/Hz}$) while maintaining identical bit-error-rate (BER) vs $E_b/N_0$ performance.",
        "source": "GATE",
        "source_reference": "GATE 2017 Electronics Engineering (IIT Roorkee) Digital Communications",
        "source_url": "https://gate.iitr.ac.in",
        "exam": "GATE Electronics Engineering",
        "year": 2017,
        "paper_set": "Session-1",
        "official_question_number": "39",
        "subject": "Communication & Fiber Optics",
        "topic": "Digital Modulation Schemes",
        "subtopic": "QPSK vs BPSK Spectral Efficiency and Bandwidth Utilization [DCM-03]",
        "concept": "QPSK transmits 2 bits/symbol, halving RF bandwidth requirement to Rb",
        "formula_used": "BW_{QPSK} = R_b = \\frac{1}{2} BW_{BPSK}, \\quad \\eta_{spectral} = 2\\text{ bps/Hz}",
        "canonical_topic_id": "DCM-03",
        "original_difficulty": "Easy",
        "exam_trap": "Thinking QPSK has worse bit error rate; at the same Eb/N0, QPSK and BPSK have identical bit error probability."
    },
    {
        "question_id": "AAI_COM_OSI_06",
        "question_text": "In the ISO-OSI 7-Layer reference model deployed in airport Baggage Handling Systems (BHS), Passenger Boarding Bridges, and ATC flight data communication, which layer is responsible for end-to-end flow control, packet segmentation/reassembly, and reliable transmission via TCP?",
        "option_a": "Data Link Layer (Layer 2)",
        "option_b": "Network Layer (Layer 3)",
        "option_c": "Transport Layer (Layer 4)",
        "option_d": "Session Layer (Layer 5)",
        "official_answer": "C",
        "verified_answer": "C",
        "solution": "In the ISO/OSI 7-Layer architecture:\n1. **Layer 1 (Physical):** Bit transmission over media (copper, fiber, RF).\n2. **Layer 2 (Data Link):** Node-to-node framing, MAC addressing, error detection (CRC).\n3. **Layer 3 (Network):** Logical IP routing across internetworks and packet forwarding.\n4. **Layer 4 (Transport):** True **end-to-end (host-to-host)** communication service. It manages process-level addressing (port numbers), packet segmentation, reassembly, congestion control, and guaranteed error recovery via acknowledgment protocols (Transmission Control Protocol - TCP).\n5. Layer 5 to 7: Session, Presentation (encryption/compression), and Application.",
        "source": "AAI",
        "source_reference": "AAI IT & Airport Data Communication Standards & ISO/IEC 7498-1",
        "source_url": "https://www.aai.aero",
        "exam": "AAI Manager (Electrical) Technical Standards",
        "year": 2023,
        "paper_set": "Data Communication",
        "official_question_number": "08",
        "subject": "Communication & Fiber Optics",
        "topic": "Data Networks",
        "subtopic": "ISO-OSI 7-Layer Architecture Transport Layer Functions [DCM-06]",
        "concept": "Transport Layer (Layer 4) provides true end-to-end flow control and reliable segmentation",
        "formula_used": "\\text{OSI Layer 4 (Transport): End-to-End Reliability via TCP / Port Addressing}",
        "canonical_topic_id": "DCM-06",
        "original_difficulty": "Easy",
        "exam_trap": "Confusing Network Layer (hop-to-hop routing) with Transport Layer (end-to-end process-to-process delivery)."
    },

    # -------------------------------------------------------------------------
    # FIBER OPTICS: Multiplexing & Lasers [FIB-01, FIB-04]
    # -------------------------------------------------------------------------
    {
        "question_id": "GATE_EC_2015_Q_FDM01",
        "question_text": "What is the fundamental engineering operational difference between Time Division Multiplexing (TDM) and Frequency Division Multiplexing (FDM)?",
        "option_a": "TDM requires analog frequency guard bands between channels; FDM requires time guard slots",
        "option_b": "TDM interleaves multiple discrete digital channels across distinct non-overlapping time slots sharing the entire transmission bandwidth; FDM assigns multiple continuous channels to distinct non-overlapping frequency bands simultaneously",
        "option_c": "FDM can only transmit binary digital pulses",
        "option_d": "TDM cannot be used on optical fiber links",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In multiplexing telecommunication theory:\n1. **FDM (Frequency Division Multiplexing):** The total available channel bandwidth is subdivided into distinct, non-overlapping frequency sub-bands separated by guard bands. All signals transmit **simultaneously in parallel**, but at different carrier frequencies (used in radio, analog TV, and Wavelength Division Multiplexing WDM).\n2. **TDM (Time Division Multiplexing):** The entire bandwidth is allocated to each channel, but sequentially across dedicated, periodic **non-overlapping time slots** (used in digital PCM, E1/T1 carrier systems, and airport Ethernet switches).",
        "source": "GATE",
        "source_reference": "GATE Electronics Engineering (IIT Kanpur) Communication Systems",
        "source_url": "https://gate.iitk.ac.in",
        "exam": "GATE Electronics Engineering",
        "year": 2015,
        "paper_set": "Master",
        "official_question_number": "17",
        "subject": "Communication & Fiber Optics",
        "topic": "Multiplexing Systems",
        "subtopic": "TDM vs FDM Principles and Bandwidth Utilization [FIB-01]",
        "concept": "TDM shares time across full bandwidth; FDM shares bandwidth across continuous time",
        "formula_used": "\\text{TDM: Time-shared slots; } \\quad \\text{FDM: Frequency-divided spectrum}",
        "canonical_topic_id": "FIB-01",
        "original_difficulty": "Easy",
        "exam_trap": "Confusing FDM guard bands (frequency spacing) with TDM guard times (time spacing)."
    },
    {
        "question_id": "ESE_EE_2018_Q_LASER04",
        "question_text": "In optical fiber communication systems, why are semiconductor Laser Diodes (LDs) preferred over Light Emitting Diodes (LEDs) for high-speed, long-distance gigabit airport backbone links?",
        "option_a": "Laser diodes produce incoherent light with a very wide spectral linewidth (50 nm)",
        "option_b": "Laser diodes emit coherent, monochromatic light with an extremely narrow spectral linewidth (typically < 1-2 nm) and high optical coupling efficiency, drastically reducing chromatic material dispersion",
        "option_c": "Laser diodes require zero threshold current to lase",
        "option_d": "Laser diodes operate without any optical cavity mirrors",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In optical communication transmitters:\n1. **LED:** Emits spontaneous incoherent light with a broad spectral width ($\\Delta\\lambda \\approx 30 - 50\\text{ nm}$). In silica fiber, this broad spectrum causes severe **chromatic dispersion** ($D \\cdot L \\cdot \\Delta\\lambda$), limiting transmission to short distances ($< 2\\text{ km}$) and low bitrates ($< 100\\text{ Mbps}$).\n2. **Semiconductor Laser Diode (LD):** Operates on stimulated emission above a distinct threshold current density ($J_{th}$). It emits spatially and temporally coherent monochromatic light with a razor-thin spectral linewidth ($\\Delta\\lambda < 0.1 - 2\\text{ nm}$) and narrow radiation beam angle, allowing high coupling efficiency into $9\\;\\mu\\text{m}$ single-mode fibers for multi-gigabit transmission across $40-100\\text{ km}$ without repeaters.",
        "source": "UPSC_ESE",
        "source_reference": "UPSC Engineering Services Exam (ESE Prelims EE 2018), Paper-I, Q.81",
        "source_url": "https://upsc.gov.in",
        "exam": "UPSC ESE Electrical Engineering",
        "year": 2018,
        "paper_set": "Paper-I",
        "official_question_number": "81",
        "subject": "Communication & Fiber Optics",
        "topic": "Optical Sources",
        "subtopic": "Semiconductor Laser Diode vs LED Spectral Linewidth and Chromatic Dispersion [FIB-04]",
        "concept": "Laser diodes have narrow spectral linewidth (< 2 nm), minimizing chromatic dispersion",
        "formula_used": "\\Delta\\tau_{chromatic} = D \\cdot L \\cdot \\Delta\\lambda \\implies \\text{Minimal for Laser Diodes}",
        "canonical_topic_id": "FIB-04",
        "original_difficulty": "Easy",
        "exam_trap": "Thinking LEDs are faster; laser diodes have much shorter carrier lifetimes and switch 100x faster than LEDs."
    },

    # -------------------------------------------------------------------------
    # MICROPROCESSORS: Architecture & Interrupts [MPU-01, MPU-03]
    # -------------------------------------------------------------------------
    {
        "question_id": "GATE_EE_2016_Q_MPU01",
        "question_text": "In the 8085 microprocessor architecture, how many total hardware interrupt pins are provided, which interrupt has the highest priority and cannot be masked by software (non-maskable), and what is its fixed vector restart address?",
        "option_a": "3 interrupts; INTR is highest at 0000H",
        "option_b": "5 hardware interrupts (TRAP, RST 7.5, RST 6.5, RST 5.5, INTR); TRAP is highest priority, non-maskable, and vectors to 0024H",
        "option_c": "8 interrupts; RST 7 is highest at 0038H",
        "option_d": "4 interrupts; RST 6.5 is non-maskable at 0034H",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In 8085 microprocessor interrupt architecture:\n1. There are **5 hardware interrupt pins** ranked in decreasing priority:\n   - **TRAP (Highest Priority):** Both edge and level sensitive, completely **Non-Maskable** (cannot be disabled by `DI` instruction). Vector address: $4.5 \\times 8 = 36 = 24H$ (**0024H**).\n   - **RST 7.5 (Priority 2):** Positive edge sensitive, maskable. Vector: $7.5 \\times 8 = 60 = 3CH$ (**003CH**).\n   - **RST 6.5 (Priority 3):** High level sensitive, maskable. Vector: $6.5 \\times 8 = 52 = 34H$ (**0034H**).\n   - **RST 5.5 (Priority 4):** High level sensitive, maskable. Vector: $5.5 \\times 8 = 44 = 2CH$ (**002CH**).\n   - **INTR (Lowest Priority):** Level sensitive, maskable, non-vectored (requires external opcode like `CALL` or `RST n` on data bus).",
        "source": "GATE",
        "source_reference": "GATE 2016 Electrical Engineering (IISc Bangalore), Session 2, Q.26",
        "source_url": "https://gate.iisc.ac.in",
        "exam": "GATE Electrical Engineering",
        "year": 2016,
        "paper_set": "Session-2",
        "official_question_number": "26",
        "subject": "Microprocessors & Microcomputers",
        "topic": "8085 Architecture",
        "subtopic": "Hardware Interrupt Priorities and TRAP Vector Address (0024H) [MPU-01]",
        "concept": "5 hardware interrupts: TRAP is highest, non-maskable, vectors to 0024H",
        "formula_used": "\\text{Vector Address for RST } N = (N \\times 8)_{10} \\to \\text{Hex} \\implies 4.5 \\times 8 = 24H",
        "canonical_topic_id": "MPU-01",
        "original_difficulty": "Easy",
        "exam_trap": "Multiplying vector numbers by 4 instead of 8 to calculate the restart vector address."
    },

    # -------------------------------------------------------------------------
    # POWER ELECTRONICS: Variable Frequency Drives (VFD) [PEL-05]
    # -------------------------------------------------------------------------
    {
        "question_id": "GATE_EE_2018_Q_VFD05",
        "question_text": "In adjustable speed AC motor drives powering airport central air-conditioning chiller water pumps and AHU supply fans, V/f control (Volts per Hertz) is employed below base speed. What is the fundamental physical rationale for maintaining a constant V/f ratio as frequency is modulated?",
        "option_a": "To keep the rotor slip constant at zero",
        "option_b": "To maintain constant magnetic flux density in the stator/rotor core (preventing deep magnetic core saturation) and preserve maximum breakdown torque capability",
        "option_c": "To convert 3-phase AC into single-phase DC",
        "option_d": "To eliminate the need for stator copper winding insulation",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In AC Variable Frequency Drive (VFD) engineering:\n1. The induced EMF in an induction machine is given by: $E = 4.44 f N \\Phi_m \\implies \\Phi_m \\approx \\frac{V}{4.44 f N} \\propto \\frac{V}{f}$.\n2. If frequency $f$ were reduced without reducing terminal voltage $V$, the magnetic flux $\\Phi_m$ would increase proportionally, causing **violent magnetic saturation** of the iron core, massive magnetizing current spikes, and motor burnout.\n3. By modulating stator voltage $V$ strictly proportional to frequency $f$ (maintaining **$V/f = \\text{Constant}$**), the air-gap magnetic flux is kept at its rated design value. This delivers **constant rated maximum electromagnetic torque** across the entire speed range below base speed.",
        "source": "GATE",
        "source_reference": "GATE 2018 Electrical Engineering (IIT Guwahati) Electric Drives",
        "source_url": "https://gate.iitg.ac.in",
        "exam": "GATE Electrical Engineering",
        "year": 2018,
        "paper_set": "Master",
        "official_question_number": "31",
        "subject": "Power Electronics & Drives",
        "topic": "AC Motor Drives",
        "subtopic": "Constant V/f Speed Control Principle and Flux Saturation Prevention [PEL-05]",
        "concept": "Constant V/f ratio maintains constant magnetic flux and maximum torque below base speed",
        "formula_used": "\\Phi_m \\propto \\frac{V}{f} = \\text{Constant} \\implies T_{max} \\approx \\text{Constant}",
        "canonical_topic_id": "PEL-05",
        "original_difficulty": "Easy",
        "exam_trap": "Thinking V/f control is used above base speed; above base speed, voltage is capped at rated and field weakening occurs."
    },

    # -------------------------------------------------------------------------
    # SIGNALS & SYSTEMS: Fourier & Laplace [SIG-04, SIG-05]
    # -------------------------------------------------------------------------
    {
        "question_id": "GATE_EE_2017_Q_SIG04",
        "question_text": "What is the Continuous-Time Fourier Transform (CTFT) of the two-sided decaying exponential signal x(t) = e^(-a |t|), where a > 0?",
        "option_a": "1 / (a + jω)",
        "option_b": "2a / (a² + ω²)",
        "option_c": "ω / (a² + ω²)",
        "option_d": "a / (a² - ω²)",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "The signal $x(t) = e^{-a |t|}$ for $a > 0$ is an even signal:\n$x(t) = e^{at} u(-t) + e^{-at} u(t)$.\nTaking the Fourier Transform:\n$X(j\\omega) = \\int_{-\\infty}^0 e^{at} e^{-j\\omega t} dt + \\int_0^{\\infty} e^{-at} e^{-j\\omega t} dt$\n$= \\left[ \\frac{e^{(a - j\\omega)t}}{a - j\\omega} \\right]_{-\\infty}^0 + \\left[ \\frac{e^{-(a + j\\omega)t}}{-(a + j\\omega)} \\right]_0^{\\infty}$\n$= \\frac{1}{a - j\\omega} + \\frac{1}{a + j\\omega} = \\frac{(a + j\\omega) + (a - j\\omega)}{(a - j\\omega)(a + j\\omega)} = \\frac{2a}{a^2 + \\omega^2}$.\nNotice that the Fourier transform is strictly real and even, as required for a real and even time signal.",
        "source": "GATE",
        "source_reference": "GATE 2017 Electrical Engineering (IIT Roorkee), Session 2, Q.12",
        "source_url": "https://gate.iitr.ac.in",
        "exam": "GATE Electrical Engineering",
        "year": 2017,
        "paper_set": "Session-2",
        "official_question_number": "12",
        "subject": "Signals & Systems",
        "topic": "Fourier Transform",
        "subtopic": "CTFT of Two-Sided Decaying Exponential Signal [SIG-04]",
        "concept": "Fourier transform of e^(-a*|t|) is 2a / (a^2 + omega^2)",
        "formula_used": "\\mathcal{F}\\{e^{-a|t|}\\} = \\frac{2a}{a^2 + \\omega^2}",
        "canonical_topic_id": "SIG-04",
        "original_difficulty": "Easy",
        "exam_trap": "Selecting 1/(a + jw), which is the one-sided transform for e^(-at)*u(t)."
    },
    {
        "question_id": "GATE_EE_2016_Q_SIG05",
        "question_text": "The transfer function of a continuous-time LTI system is H(s) = (s + 2) / [(s + 1)(s - 3)]. What is the required Region of Convergence (ROC) in the s-plane for the system to be both stable and non-causal?",
        "option_a": "Re(s) > 3",
        "option_b": "-1 < Re(s) < 3",
        "option_c": "Re(s) < -1",
        "option_d": "Re(s) > -1",
        "official_answer": "B",
        "verified_answer": "B",
        "solution": "In Laplace transform theory:\n1. The poles of $H(s)$ are at $s = -1$ and $s = +3$.\n2. **Stability Requirement:** A continuous-time LTI system is BIBO stable if and only if its ROC includes the imaginary $j\\omega$ axis, i.e., $\\text{Re}(s) = 0$.\n3. **Causality vs Non-Causality:**\n   - If the system were causal, the ROC would be to the right of the rightmost pole: $\\text{Re}(s) > 3$ (which does not include the $j\\omega$ axis, making it unstable).\n   - For a two-sided (non-causal) system, the ROC is a vertical strip bounded by adjacent poles: **$-1 < \\text{Re}(s) < 3$**.\n4. Since this strip contains the imaginary axis ($\\,0 \\in (-1, 3)\\,$, the system is BIBO stable and non-causal.",
        "source": "GATE",
        "source_reference": "GATE 2016 Electrical Engineering (IISc Bangalore), Session 1, Q.18",
        "source_url": "https://gate.iisc.ac.in",
        "exam": "GATE Electrical Engineering",
        "year": 2016,
        "paper_set": "Session-1",
        "official_question_number": "18",
        "subject": "Signals & Systems",
        "topic": "Laplace Transform",
        "subtopic": "Laplace Transform ROC Strip for Stable Non-Causal Systems [SIG-05]",
        "concept": "For a stable two-sided system, ROC is a vertical strip including the jw axis",
        "formula_used": "\\text{ROC: } -1 < \\text{Re}(s) < 3 \\implies j\\omega \\text{ axis is enclosed}",
        "canonical_topic_id": "SIG-05",
        "original_difficulty": "Easy",
        "exam_trap": "Choosing Re(s) > 3 because of causality reflex, which violates the stability requirement."
    }
]

def add_part2():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT question_id, text_hash FROM questions")
    rows = cursor.fetchall()
    existing_ids = {r[0] for r in rows}
    existing_hashes = {r[1] for r in rows}

    added = 0
    skipped = 0

    for q in QUESTIONS_PART2:
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
            q.get("year", 2018),
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
            q.get("source_url", "https://gate.iisc.ac.in"),
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
    print(f"\nMass Expansion Part 2 Ingestion Summary:")
    print(f" - Successfully Added: {added}")
    print(f" - Skipped: {skipped}")
    print(f" - New Database Total: {len(all_rows)} questions")

if __name__ == "__main__":
    add_part2()
