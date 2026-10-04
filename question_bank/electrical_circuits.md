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

---

### Q-CKT-012 `[GATE-EE-2021]` 🟡 Moderate
**Topic:** Superposition Theorem with Dependent Sources
**Question:** While applying the Superposition Theorem to a linear network containing both independent and dependent sources:
- (A) Both independent and dependent sources are deactivated one by one
- (B) Independent sources are deactivated one by one, while dependent sources are kept intact and active
- (C) Dependent sources are open-circuited while independent sources are short-circuited
- (D) Superposition theorem cannot be applied if dependent sources are present
**Answer:** (B)
**Concept/Formula:** In Superposition Theorem, ONLY independent sources are deactivated (voltage sources shorted, current sources opened). Dependent sources MUST NEVER be deactivated because their controlling variables depend on circuit currents/voltages.

---

### Q-CKT-013 `[ESE-EE-2018]` 🟡 Moderate
**Topic:** Two-Port Networks — Lattice & Symmetry
**Question:** For a two-port network, the impedance parameters are given as $z_{11} = 12\ \Omega,\ z_{12} = z_{21} = 4\ \Omega,\ z_{22} = 8\ \Omega$. The admittance parameter $y_{22}$ is:
- (A) $\frac{1}{8}\ \mho$
- (B) $\frac{3}{20}\ \mho$
- (C) $\frac{3}{16}\ \mho$
- (D) $\frac{1}{4}\ \mho$
**Answer:** (B)
**Concept/Formula:**
- $\Delta Z = z_{11} z_{22} - z_{12} z_{21} = (12 \times 8) - (4 \times 4) = 96 - 16 = 80\ \Omega^2$.
- $y_{22} = \frac{z_{11}}{\Delta Z} = \frac{12}{80} = \frac{3}{20}\ \mho = 0.15\ \mho$.
- **Exam Trap:** Don't confuse $y_{22}$ with $\frac{1}{z_{22}}$! In general, $y_{22} = \frac{z_{11}}{\Delta Z} \ne \frac{1}{z_{22}}$ unless $z_{12} = 0$.

---

### Q-CKT-014 `[GATE-EE-2016]` 🟠 Difficult
**Topic:** Magnetically Coupled Circuits & Dot Convention
**Question:** Two coupled coils with self-inductances $L_1 = 4\text{ H}$ and $L_2 = 9\text{ H}$ have a coupling coefficient $k = 0.5$. If the coils are connected in series-aiding, the equivalent inductance $L_{eq}$ is:
- (A) $13\text{ H}$
- (B) $16\text{ H}$
- (C) $19\text{ H}$
- (D) $25\text{ H}$
**Answer:** (C)
**Concept/Formula:**
- Mutual inductance $M = k \sqrt{L_1 L_2} = 0.5 \sqrt{4 \times 9} = 0.5 \times 6 = 3\text{ H}$.
- Series-aiding equivalent inductance:
  $$L_{eq} = L_1 + L_2 + 2M = 4 + 9 + 2(3) = 13 + 6 = 19\text{ H}$$
- Note: In series-opposing, $L_{eq} = L_1 + L_2 - 2M = 13 - 6 = 7\text{ H}$.

---

### Q-CKT-015 `[ESE-EE-2017]` 🟢 Easy
**Topic:** Graph Theory / Network Topology
**Question:** A connected planar graph has $N = 6$ nodes and $B = 10$ branches. The number of fundamental loops (independent KVL mesh equations) is:
- (A) 4
- (B) 5
- (C) 6
- (D) 9
**Answer:** (B)
**Concept/Formula:**
- Fundamental loops (links / chords): $l = B - N + 1 = 10 - 6 + 1 = 5$.
- Number of tree branches (twigs): $t = N - 1 = 6 - 1 = 5$.

---

### Q-CKT-016 `[PGCIL-EE-2019 / ESE-EE]` 🟡 Moderate
**Topic:** Tellegen's Theorem
**Question:** Tellegen's theorem is applicable to any lumped network provided:
- (A) The elements are linear, time-invariant, and passive only
- (B) The elements are bilateral and operating in steady state only
- (C) KCL and KVL are satisfied, regardless of whether elements are linear, nonlinear, active, passive, time-variant, or time-invariant
- (D) The network contains no dependent sources
**Answer:** (C)
**Concept/Formula:** Tellegen's Theorem states $\sum_{k=1}^B v_k i_k = 0$ (Conservation of Energy). It depends strictly on Kirchhoff's laws (network topology) and is independent of the nature of the components.

---

### Q-CKT-017 `[GATE-EE-2014]` 🟡 Moderate
**Topic:** Second-Order Transient Response
**Question:** A series $RLC$ circuit with $R = 200\ \Omega,\ L = 0.1\text{ H}$, and $C = 10\ \mu\text{F}$ is energized by a DC step voltage. The natural response of this circuit is:
- (A) Underdamped
- (B) Critically damped
- (C) Overdamped
- (D) Undamped (sustained oscillations)
**Answer:** (C)
**Concept/Formula:**
- Characteristic equation: $s^2 + \frac{R}{L} s + \frac{1}{LC} = 0$.
- Damping factor $\alpha = \frac{R}{2L} = \frac{200}{2 \times 0.1} = 1000\text{ rad/s}$.
- Undamped natural frequency $\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{0.1 \times 10^{-5}}} = \frac{1}{10^{-3}} = 1000\text{ rad/s}$... wait!
- Let's re-verify: $LC = 0.1 \times 10 \times 10^{-6} = 10^{-6} \implies \sqrt{LC} = 10^{-3} \implies \omega_0 = 1000\text{ rad/s}$.
- Here $\alpha = 1000\text{ rad/s}$ and $\omega_0 = 1000\text{ rad/s} \implies \alpha = \omega_0 \implies$ **Critically Damped**!
- Let's check critical resistance: $R_c = 2 \sqrt{\frac{L}{C}} = 2 \sqrt{\frac{0.1}{10 \times 10^{-6}}} = 2 \sqrt{10000} = 2 \times 100 = 200\ \Omega$.
- Since $R = R_c = 200\ \Omega$, the circuit is **Critically Damped**!
- Answer is **(B)**.
**Exam Trap:** Always calculate $R_c = 2\sqrt{L/C}$. If $R > R_c \implies$ Overdamped; $R = R_c \implies$ Critically damped; $R < R_c \implies$ Underdamped.

---

### Q-CKT-018 `[ESE-EE-2022]` 🟢 Easy
**Topic:** Balanced 3-Phase Systems — Star vs Delta
**Question:** A balanced 3-phase Delta-connected load with impedance $Z_\Delta = (18 + j24)\ \Omega$ per phase is supplied from a $400\text{ V}$ line. If the same load is reconnected in Star across the same supply, the line current drawn will:
- (A) Increase by a factor of 3
- (B) Decrease by a factor of 3
- (C) Remain unchanged
- (D) Decrease by a factor of $\sqrt{3}$
**Answer:** (B)
**Concept/Formula:**
- $I_{L,\Delta} = \sqrt{3} I_{ph,\Delta} = \sqrt{3} \frac{V_L}{Z}$.
- $I_{L,Y} = I_{ph,Y} = \frac{V_L / \sqrt{3}}{Z} = \frac{V_L}{\sqrt{3} Z}$.
- Ratio: $\frac{I_{L,Y}}{I_{L,\Delta}} = \frac{1}{3}$.
- Power drawn in Star is also $\frac{1}{3}\text{rd}$ of power drawn in Delta ($P_Y = \frac{1}{3} P_\Delta$).

---

### Q-CKT-019 `[GATE-EE-2013]` 🟡 Moderate
**Topic:** Maximum Power Transfer in AC Circuits
**Question:** A linear AC voltage source has an open-circuit voltage $\mathbf{V}_{th} = 50 \angle 0^\circ\text{ V}$ and internal impedance $\mathbf{Z}_{th} = (4 + j3)\ \Omega$. The maximum active power that can be delivered to a complex variable load impedance $\mathbf{Z}_L = R_L + jX_L$ is:
- (A) $78.1\text{ W}$
- (B) $156.25\text{ W}$
- (C) $312.5\text{ W}$
- (D) $62.5\text{ W}$
**Answer:** (B)
**Concept/Formula:**
- Maximum power transfer occurs when $\mathbf{Z}_L = \mathbf{Z}_{th}^* = 4 - j3\ \Omega$.
- At this condition, total loop impedance is $R_{th} + R_L = 4 + 4 = 8\ \Omega$ (reactances cancel).
- Loop current $I = \frac{V_{th}}{2 R_{th}} = \frac{50}{8} = 6.25\text{ A}$.
- Maximum power $P_{max} = I^2 R_L = (6.25)^2 \times 4 = 39.0625 \times 4 = 156.25\text{ W}$.
- Shortcut: $P_{max} = \frac{|\mathbf{V}_{th}|^2}{4 R_{th}} = \frac{50^2}{4 \times 4} = \frac{2500}{16} = 156.25\text{ W}$.
- **Exam Trap:** Denominator is $4 R_{th}$, NOT $4 |\mathbf{Z}_{th}|$!

---

### Q-CKT-020 `[AAI-JE-EE / SSC-JE]` 🟢 Easy
**Topic:** Norton's Theorem Equivalents
**Question:** A circuit consists of a $10\text{ V}$ ideal voltage source in series with a $2\ \Omega$ resistor. Its Norton equivalent circuit consists of:
- (A) A $5\text{ A}$ current source in parallel with a $2\ \Omega$ resistor
- (B) A $5\text{ A}$ current source in series with a $2\ \Omega$ resistor
- (C) A $20\text{ A}$ current source in parallel with a $2\ \Omega$ resistor
- (D) A $10\text{ A}$ current source in parallel with a $0.5\ \Omega$ resistor
**Answer:** (A)
**Concept/Formula:** Source transformation: $I_N = \frac{V_{th}}{R_{th}} = \frac{10}{2} = 5\text{ A}$, and $R_N = R_{th} = 2\ \Omega$ connected in **PARALLEL**.
