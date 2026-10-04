# AUTHENTIC QUESTION BANK: ELECTRICAL CIRCUITS & NETWORK THEORY
*Sources: AAI JE/Manager PYQs, ESE Prelims EE, GATE EE (1-mark/2-mark CBT style), ISRO EE, State AE/JE*

---

### Q-CKT-001 `[AAI-JE-EE-2018]` 🟢 Easy
**Topic:** Basic Laws & Energy Storage
**Question:** An inductor of $2\text{ H}$ carries a steady current of $4\text{ A}$. The energy stored in the magnetic field is:
- (A) $8\text{ J}$
- (B) $16\text{ J}$
- (C) $32\text{ J}$
- (D) $64\text{ J}$
**Answer:** (B)
**Concept/Formula:** $E = \frac{1}{2} L I^2 = \frac{1}{2} \times 2 \times 4^2 = 16\text{ J}$.
**Exam Trap:** Forgetting the factor of $1/2$ or squaring before multiplying.

---

### Q-CKT-002 `[ESE-EE-2019]` 🟡 Moderate
**Topic:** Thevenin's Theorem
**Question:** In the circuit shown below (or described), looking into terminals A and B: A voltage source of $20\text{ V}$ is in series with a $5\ \Omega$ resistor, and in parallel with a $20\ \Omega$ resistor. The Thevenin equivalent voltage ($V_{th}$) and Thevenin resistance ($R_{th}$) across AB are:
- (A) $V_{th} = 16\text{ V},\ R_{th} = 4\ \Omega$
- (B) $V_{th} = 20\text{ V},\ R_{th} = 25\ \Omega$
- (C) $V_{th} = 16\text{ V},\ R_{th} = 25\ \Omega$
- (D) $V_{th} = 4\text{ V},\ R_{th} = 4\ \Omega$
**Answer:** (A)
**Concept/Formula:** 
- Open-circuit voltage $V_{th} = 20 \times \frac{20}{5 + 20} = 20 \times \frac{20}{25} = 16\text{ V}$.
- Deactivating the $20\text{ V}$ voltage source (short circuit): $R_{th} = 5 \parallel 20 = \frac{5 \times 20}{5 + 20} = \frac{100}{25} = 4\ \Omega$.

---

### Q-CKT-003 `[GATE-EE-2017]` 🟡 Moderate
**Topic:** Maximum Power Transfer Theorem
**Question:** A practical DC voltage source provides an open-circuit voltage of $12\text{ V}$ and delivers a maximum power of $18\text{ W}$ to a variable resistive load $R_L$. The internal resistance $R_s$ of the source is:
- (A) $1\ \Omega$
- (B) $2\ \Omega$
- (C) $4\ \Omega$
- (D) $8\ \Omega$
**Answer:** (B)
**Concept/Formula:** 
- $P_{max} = \frac{V_{th}^2}{4 R_s} \implies 18 = \frac{12^2}{4 R_s} = \frac{144}{4 R_s} \implies 18 = \frac{36}{R_s} \implies R_s = 2\ \Omega$.

---

### Q-CKT-004 `[AAI-JE-EE-2016 / SSC-JE]` 🟡 Moderate
**Topic:** Series Resonance
**Question:** In a series $RLC$ circuit with $R = 10\ \Omega$, $L = 0.5\text{ H}$, and $C = 50\ \mu\text{F}$, connected to a variable-frequency AC source of $200\text{ V}$, the resonant frequency $\omega_0$ and the current at resonance are:
- (A) $\omega_0 = 200\text{ rad/s},\ I_0 = 20\text{ A}$
- (B) $\omega_0 = 100\text{ rad/s},\ I_0 = 10\text{ A}$
- (C) $\omega_0 = 200\text{ rad/s},\ I_0 = 10\text{ A}$
- (D) $\omega_0 = 100\text{ rad/s},\ I_0 = 20\text{ A}$
**Answer:** (A)
**Concept/Formula:**
- $\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{0.5 \times 50 \times 10^{-6}}} = \frac{1}{\sqrt{25 \times 10^{-6}}} = \frac{1}{5 \times 10^{-3}} = 200\text{ rad/s}$.
- At resonance, $Z = R = 10\ \Omega$.
- $I_0 = \frac{V}{R} = \frac{200}{10} = 20\text{ A}$.

---

### Q-CKT-005 `[ESE-EE-2021]` 🟡 Moderate
**Topic:** Quality Factor & Bandwidth
**Question:** A series $RLC$ circuit has a resonant frequency of $1000\text{ Hz}$ and a bandwidth of $100\text{ Hz}$. The quality factor ($Q$) of the circuit is:
- (A) $0.1$
- (B) $10$
- (C) $100$
- (D) $1000$
**Answer:** (B)
**Concept/Formula:** $Q = \frac{f_0}{\text{Bandwidth}} = \frac{1000}{100} = 10$.

---

### Q-CKT-006 `[GATE-EE-2018]` 🟠 Difficult
**Topic:** First-Order DC Transients
**Question:** In an unenergized series $RL$ circuit with $R = 20\ \Omega$ and $L = 0.1\text{ H}$, a constant DC voltage $V = 100\text{ V}$ is applied at $t = 0$. The initial rate of rise of current $\left.\frac{di}{dt}\right|_{t=0^+}$ is:
- (A) $0\text{ A/s}$
- (B) $500\text{ A/s}$
- (C) $1000\text{ A/s}$
- (D) $2000\text{ A/s}$
**Answer:** (C)
**Concept/Formula:**
- Since inductor current cannot change instantaneously, $i(0^+) = i(0^-) = 0$.
- By KVL at $t = 0^+$: $V = R \cdot i(0^+) + L \left.\frac{di}{dt}\right|_{t=0^+} \implies 100 = 0 + 0.1 \left.\frac{di}{dt}\right|_{t=0^+}$.
- $\left.\frac{di}{dt}\right|_{t=0^+} = \frac{100}{0.1} = 1000\text{ A/s}$.

---

### Q-CKT-007 `[AAI-JE-EE-2018]` 🟢 Easy
**Topic:** 3-Phase Power Measurement (Two-Wattmeter Method)
**Question:** In the two-wattmeter method of measuring 3-phase balanced power, if one wattmeter reads zero and the other reads positive, the power factor of the load is:
- (A) $1.0$ (Unity)
- (B) $0.866$
- (C) $0.5$
- (D) $0.0$ (Zero)
**Answer:** (C)
**Concept/Formula:**
- $\tan \phi = \sqrt{3} \frac{W_1 - W_2}{W_1 + W_2}$.
- If $W_2 = 0$, $\tan \phi = \sqrt{3} \implies \phi = 60^\circ \implies \cos \phi = \cos 60^\circ = 0.5$.

---

### Q-CKT-008 `[ESE-EE-2020]` 🟡 Moderate
**Topic:** Two-Port Networks
**Question:** For a symmetrical and reciprocal two-port network, the conditions on the transmission parameters ($ABCD$) are:
- (A) $A = D$ and $AD - BC = 1$
- (B) $A = B$ and $AD - BC = 1$
- (C) $B = C$ and $AD - BC = 0$
- (D) $A = D$ and $AD - BC = 0$
**Answer:** (A)
**Concept/Formula:**
- Reciprocity condition: $AD - BC = 1$.
- Symmetry condition: $A = D$.

---

### Q-CKT-009 `[GATE-EE-2015]` 🟡 Moderate
**Topic:** Star-Delta Transformation
**Question:** Three identical resistors each of resistance $R$ are connected in Delta across a balanced 3-phase supply. If this Delta network is replaced by an equivalent Star network, the resistance of each Star branch must be:
- (A) $3R$
- (B) $R / 3$
- (C) $R / \sqrt{3}$
- (D) $\sqrt{3} R$
**Answer:** (B)
**Concept/Formula:** $R_Y = \frac{R_\Delta \times R_\Delta}{R_\Delta + R_\Delta + R_\Delta} = \frac{R^2}{3R} = \frac{R}{3}$.

---

### Q-CKT-010 `[PGCIL-EE-2021 / ESE-EE]` 🟡 Moderate
**Topic:** AC Circuits — Active & Reactive Power
**Question:** An AC voltage $v(t) = 100 \sqrt{2} \sin(100\pi t)\text{ V}$ is applied across an impedance $Z = (6 + j8)\ \Omega$. The active power ($P$) and reactive power ($Q$) supplied to the circuit are:
- (A) $P = 600\text{ W},\ Q = 800\text{ VAR}$
- (B) $P = 800\text{ W},\ Q = 600\text{ VAR}$
- (C) $P = 1200\text{ W},\ Q = 1600\text{ VAR}$
- (D) $P = 60\text{ W},\ Q = 80\text{ VAR}$
**Answer:** (A)
**Concept/Formula:**
- $V_{rms} = 100\text{ V}$.
- Magnitude $|Z| = \sqrt{6^2 + 8^2} = 10\ \Omega$.
- Current $I_{rms} = \frac{V_{rms}}{|Z|} = \frac{100}{10} = 10\text{ A}$.
- Active power $P = I^2 R = 10^2 \times 6 = 600\text{ W}$.
- Reactive power $Q = I^2 X = 10^2 \times 8 = 800\text{ VAR}$.

---

### Q-CKT-011 `[ISRO-EE-2020]` 🟠 Difficult
**Topic:** Parallel Resonance
**Question:** A practical parallel resonant circuit consists of a coil with resistance $R$ and inductance $L$ in parallel with a lossless capacitor $C$. The dynamic impedance $Z_d$ of the circuit at resonance is given by:
- (A) $\sqrt{\frac{L}{C}}$
- (B) $\frac{L}{CR}$
- (C) $\frac{C}{LR}$
- (D) $\frac{R}{\omega L}$
**Answer:** (B)
**Concept/Formula:**
- Dynamic resistance/impedance at anti-resonance: $Z_d = \frac{L}{CR}$.
- Note that unlike series resonance where impedance is minimum ($Z = R$), in parallel resonance impedance is maximum ($Z_d = \frac{L}{CR}$) and current is minimum.
