# AUTHENTIC QUESTION BANK: ELECTRICAL MACHINES
*Sources: AAI JE/Manager PYQs, ESE Prelims EE, GATE EE, State AE, PGCIL, DMRC*

---

### Q-MCH-001 `[AAI-JE-EE-2018]` 🟢 Easy
**Topic:** Transformers — Maximum Efficiency
**Question:** In a transformer, maximum efficiency occurs when:
- (A) Copper loss = Twice the core loss
- (B) Variable copper loss = Constant core loss
- (C) Core loss is zero
- (D) Power factor is zero
**Answer:** (B)
**Concept/Formula:** Efficiency $\eta = \frac{x S \cos \phi}{x S \cos \phi + P_i + x^2 P_{cu,fl}}$. Maximizing with respect to loading fraction $x$ yields $x^2 P_{cu,fl} = P_i$.

---

### Q-MCH-002 `[ESE-EE-2020]` 🟡 Moderate
**Topic:** Auto-Transformers
**Question:** A 2-winding transformer rated at $10\text{ kVA},\ 400/200\text{ V}$ is reconnected as a step-up auto-transformer to supply $600\text{ V}$ from a $400\text{ V}$ supply. Its kVA rating as an auto-transformer is:
- (A) $15\text{ kVA}$
- (B) $20\text{ kVA}$
- (C) $30\text{ kVA}$
- (D) $50\text{ kVA}$
**Answer:** (C)
**Concept/Formula:**
- In 2-winding mode: $I_{LV} = \frac{10\text{ kVA}}{200\text{ V}} = 50\text{ A}$, $I_{HV} = \frac{10\text{ kVA}}{400\text{ V}} = 25\text{ A}$.
- Auto-transformer: Input = $400\text{ V}$, Output = $400 + 200 = 600\text{ V}$.
- Output current rating is limited by the $200\text{ V}$ series winding current = $50\text{ A}$.
- Auto-transformer rating = $V_{out} \times I_{out} = 600\text{ V} \times 50\text{ A} = 30\text{ kVA}$.
- Formula shortcut: $\text{kVA}_{auto} = \text{kVA}_{2w} \times \frac{V_{high}}{V_{high} - V_{low}} = 10 \times \frac{600}{600 - 400} = 10 \times 3 = 30\text{ kVA}$.

---

### Q-MCH-003 `[GATE-EE-2019]` 🟡 Moderate
**Topic:** DC Motor Speed Control
**Question:** A $220\text{ V}$ DC shunt motor runs at $1000\text{ rpm}$ while taking an armature current of $20\text{ A}$. The armature resistance is $0.5\ \Omega$. If a resistance of $4.5\ \Omega$ is added in series with the armature, the torque remaining constant, the new speed is:
- (A) $600\text{ rpm}$
- (B) $571.4\text{ rpm}$
- (C) $800\text{ rpm}$
- (D) $450\text{ rpm}$
**Answer:** (B)
**Concept/Formula:**
- $E_{b1} = V - I_a R_a = 220 - (20 \times 0.5) = 220 - 10 = 210\text{ V}$.
- Since torque $T \propto \phi I_a$ and $\phi$ is constant (shunt motor with constant field), constant torque implies $I_a$ remains $20\text{ A}$.
- $E_{b2} = V - I_a (R_a + R_{ext}) = 220 - 20(0.5 + 4.5) = 220 - 100 = 120\text{ V}$.
- $N \propto E_b \implies \frac{N_2}{N_1} = \frac{E_{b2}}{E_{b1}} \implies N_2 = 1000 \times \frac{120}{210} = 1000 \times \frac{4}{7} \approx 571.4\text{ rpm}$.

---

### Q-MCH-004 `[AAI-JE-EE-2016]` 🟢 Easy
**Topic:** Induction Motor Slip & Frequency
**Question:** A 6-pole, $50\text{ Hz}$, 3-phase induction motor runs at $960\text{ rpm}$. The frequency of the rotor induced EMF is:
- (A) $50\text{ Hz}$
- (B) $2\text{ Hz}$
- (C) $4\text{ Hz}$
- (D) $5\text{ Hz}$
**Answer:** (B)
**Concept/Formula:**
- Synchronous speed $N_s = \frac{120 f}{P} = \frac{120 \times 50}{6} = 1000\text{ rpm}$.
- Slip $s = \frac{N_s - N_r}{N_s} = \frac{1000 - 960}{1000} = 0.04$.
- Rotor frequency $f_r = s \cdot f = 0.04 \times 50 = 2.0\text{ Hz}$.

---

### Q-MCH-005 `[ESE-EE-2018]` 🟡 Moderate
**Topic:** Induction Motor Maximum Torque
**Question:** In a 3-phase slip-ring induction motor, maximum torque is developed when the slip $s_{mT}$ is equal to:
- (A) $\frac{R_2}{X_2}$
- (B) $\frac{X_2}{R_2}$
- (C) $\sqrt{\frac{R_2}{X_2}}$
- (D) $R_2 \cdot X_2$
**Answer:** (A)
**Concept/Formula:**
- Maximum torque condition: $s_{mT} = \frac{R_2}{X_2}$.
- Crucial Exam Rule: Maximum torque magnitude $T_{max} = \frac{3}{2 \omega_s} \frac{V_1^2}{2 X_2}$ is INDEPENDENT of rotor resistance $R_2$, but the slip at which it occurs is directly proportional to $R_2$.

---

### Q-MCH-006 `[AAI-JE-EE-2018]` 🟢 Easy
**Topic:** Synchronous Motors & Power Factor
**Question:** A synchronous motor is operating as a "synchronous condenser" when it is:
- (A) Under-excited and carrying mechanical load
- (B) Over-excited and operating on no-load
- (C) Under-excited and operating on no-load
- (D) Normally excited and carrying full load
**Answer:** (B)
**Concept/Formula:** An over-excited synchronous motor on no load draws leading reactive power from the AC supply, behaving like a 3-phase capacitor (synchronous condenser) to improve system power factor.

---

### Q-MCH-007 `[GATE-EE-2016]` 🟠 Difficult
**Topic:** Synchronous Generator Power Angle Equation
**Question:** A 3-phase, cylindrical-rotor synchronous generator having synchronous reactance $X_s = 1.0\text{ pu}$ is connected to an infinite bus of $1.0\text{ pu}$ voltage. The internal excitation voltage is $E_f = 1.2\text{ pu}$. The steady-state power limit (maximum real power transfer) is:
- (A) $1.0\text{ pu}$
- (B) $1.2\text{ pu}$
- (C) $0.833\text{ pu}$
- (D) $2.2\text{ pu}$
**Answer:** (B)
**Concept/Formula:**
- $P = \frac{E_f V}{X_s} \sin \delta$.
- Maximum power occurs when $\delta = 90^\circ$: $P_{max} = \frac{E_f V}{X_s} = \frac{1.2 \times 1.0}{1.0} = 1.2\text{ pu}$.

---

### Q-MCH-008 `[NTPC-EE / ESE-EE-2019]` 🟡 Moderate
**Topic:** Transformer Open-Circuit & Short-Circuit Tests
**Question:** The open-circuit (OC) test on a transformer is conducted at rated voltage, usually on the low-voltage (LV) winding, to determine:
- (A) Full-load copper loss and equivalent resistance
- (B) Core loss and magnetizing branch parameters ($R_c, X_m$)
- (C) Equivalent leakage reactance only
- (D) Winding temperature rise
**Answer:** (B)
**Concept/Formula:**
- OC test is done at rated voltage and rated frequency to find core (iron) losses ($P_i = P_h + P_e$) and no-load shunt parameters ($R_c, X_m$). LV side is chosen for convenience and safety because rated LV voltage is easier to supply and no-load current is sufficiently large to read accurately.
- SC test is done at reduced voltage (5-10% rated) and rated current on HV side to determine series equivalent parameters ($R_{eq}, X_{eq}$) and full-load copper loss ($P_{cu,fl}$).

---

### Q-MCH-009 `[GATE-EE-2018]` 🟠 Difficult
**Topic:** 3-Phase Induction Motor — Rotor Power Relations
**Question:** A 3-phase, $415\text{ V},\ 50\text{ Hz}$, 4-pole induction motor develops an electromagnetic torque of $200\text{ Nm}$ while operating at a slip of $4\%$. The rotor ohmic (copper) loss in watts is:
- (A) $1256.6\text{ W}$
- (B) $628.3\text{ W}$
- (C) $314.2\text{ W}$
- (D) $2513.2\text{ W}$
**Answer:** (A)
**Concept/Formula:**
- Synchronous speed $\omega_s = \frac{2\pi N_s}{60} = \frac{2\pi \times 1500}{60} = 50\pi \approx 157.08\text{ rad/s}$.
- Air-gap power $P_g = T_e \times \omega_s = 200 \times 157.08 = 31415.9\text{ W}$.
- Rotor copper loss $P_{cu} = s \times P_g = 0.04 \times 31415.9 = 1256.6\text{ W}$.
- Shortcut: $P_{cu} = s \times T_e \times \frac{4\pi f}{P} = 0.04 \times 200 \times \frac{4\pi \times 50}{4} = 8 \times 50\pi = 400\pi \approx 1256.64\text{ W}$.

---

### Q-MCH-010 `[BHEL-EE / ESE-EE-2021]` 🟡 Moderate
**Topic:** Synchronous Machine — Voltage Regulation Methods
**Question:** Among the following methods used to determine the voltage regulation of a synchronous alternator, which method is known as the **optimistic method** (yields lower than actual regulation) and which is the **pessimistic method** (yields higher than actual regulation)?
- (A) Optimistic: EMF method; Pessimistic: MMF method
- (B) Optimistic: MMF method; Pessimistic: EMF method
- (C) Optimistic: Potier method; Pessimistic: MMF method
- (D) Optimistic: EMF method; Pessimistic: Potier method
**Answer:** (B)
**Concept/Formula:**
- **EMF (Synchronous Impedance) Method:** Treats saturation as negligible and assumes $X_s$ is constant (unsaturated value), yielding larger voltage drop and HIGHER regulation $\implies$ **Pessimistic method**.
- **MMF (Ampere-Turn) Method:** Considers saturation and adds field MMFs linearly, yielding LOWER regulation $\implies$ **Optimistic method**.
- **Potier (Zero Power Factor / ZPF) Method:** Accurately separates armature leakage reactance and armature reaction $\implies$ **Most accurate method**.

---

### Q-MCH-011 `[GATE-EE-2015]` 🟡 Moderate
**Topic:** Transformer All-Day Efficiency
**Question:** Distribution transformers are designed to have:
- (A) Maximum efficiency at 100% full load
- (B) Maximum efficiency at around 50% to 70% of full load
- (C) Core losses greater than full-load copper losses
- (D) Low leakage reactance and high magnetizing current
**Answer:** (B)
**Concept/Formula:**
- Distribution transformers remain energized 24 hours a day, but supply residential/commercial loads that average only about 50% to 70% of rated capacity.
- To maximize **all-day efficiency** ($\frac{\text{Output in kWh}}{\text{Input in kWh}}$), core losses (incurred 24 hours) are made very small relative to copper losses, so maximum efficiency occurs around 50–70% load ($x = \sqrt{P_i / P_{cu,fl}} \approx 0.5 \text{ to } 0.7$).
- In contrast, **power transformers** operate near 100% full load continuously and are designed for maximum efficiency at or near full load.

---

### Q-MCH-012 `[ESE-EE-2018]` 🟡 Moderate
**Topic:** 3-Phase Transformer Vector Groups
**Question:** In a 3-phase, Delta-Star (Dy11) connected transformer, the secondary line voltage:
- (A) Lags the primary line voltage by $30^\circ$
- (B) Leads the primary line voltage by $30^\circ$
- (C) Is in phase with the primary line voltage
- (D) Leads the primary line voltage by $180^\circ$
**Answer:** (B)
**Concept/Formula:**
- Clock convention: Primary line voltage is at 12 o'clock ($0^\circ$).
- Dy11: The secondary line voltage is at 11 o'clock.
- In a clock face, each hour represents $30^\circ$. 11 o'clock is $30^\circ$ counter-clockwise (ahead / leading) relative to 12 o'clock.
- Therefore, secondary voltage **leads** primary by $+30^\circ$.
- For Dy1: Secondary is at 1 o'clock $\implies$ **lags** primary by $30^\circ$ ($-30^\circ$).

---

### Q-MCH-013 `[ISRO-EE-2019]` 🟢 Easy
**Topic:** DC Generator — Armature Reaction
**Question:** In a DC generator, the effect of armature reaction under load is:
- (A) Demagnetizing and cross-magnetizing
- (B) Magnetizing only
- (C) Demagnetizing only
- (D) Cross-magnetizing only without any demagnetizing effect
**Answer:** (A)
**Concept/Formula:**
- Armature reaction causes distortion of the main magnetic field (cross-magnetization), shifting the Magnetic Neutral Axis (MNA) in the direction of rotation.
- Due to magnetic saturation of the pole tips, the reduction in flux under the weakened pole tip is greater than the increase under the strengthened tip, resulting in a net decrease in total flux (demagnetizing effect).

---

### Q-MCH-014 `[GATE-EE-2021]` 🟡 Moderate
**Topic:** DC Motor Starters & Back EMF
**Question:** A $240\text{ V}$ DC shunt motor has an armature resistance of $0.4\ \Omega$. If connected directly to the supply at standstill ($N = 0$) without a starter, the initial armature starting current will be:
- (A) $60\text{ A}$
- (B) $240\text{ A}$
- (C) $600\text{ A}$
- (D) $24\text{ A}$
**Answer:** (C)
**Concept/Formula:**
- At starting, $N = 0 \implies$ Back EMF $E_b = 0$.
- Starting current $I_{a,start} = \frac{V - E_b}{R_a} = \frac{240 - 0}{0.4} = 600\text{ A}$!
- This is 10 to 15 times rated current, which would destroy the commutator and burn the winding. Hence, a starter (3-point or 4-point) is essential to insert temporary series resistance.

---

### Q-MCH-015 `[ESE-EE-2017]` 🟢 Easy
**Topic:** Induction Motor Cogging & Crawling
**Question:** "Crawling" in a 3-phase squirrel cage induction motor is caused primarily by:
- (A) High slip under full load
- (B) Space harmonics produced by stator winding distribution (primarily 7th harmonic)
- (C) Time harmonics present in the supply voltage
- (D) Unequal air gap between stator and rotor
**Answer:** (B)
**Concept/Formula:**
- Stator winding distributes space harmonics of orders $n = 6k \pm 1$.
- The **7th space harmonic** rotates in the forward direction at synchronous speed $N_{s7} = N_s / 7$. It creates a small forward torque dip that causes the motor to run steadily at a fraction (about $\frac{1}{7}\text{th}$) of normal speed $\implies$ **Crawling**.
- The 5th harmonic rotates backwards ($N_{s5} = -N_s/5$) and provides braking torque.
- **Cogging (magnetic locking)** occurs when the number of stator slots equals or is an integral multiple of rotor slots.

---

### Q-MCH-016 `[GATE-EE-2014]` 🟡 Moderate
**Topic:** 3-Phase Induction Motor — Starting vs Maximum Torque
**Question:** A 3-phase induction motor has a starting torque equal to the full-load torque ($T_{st} = T_{fl}$) and a maximum torque equal to twice the full-load torque ($T_{max} = 2 T_{fl}$). The slip at maximum torque $s_{mT}$ is:
- (A) $0.268$
- (B) $0.500$
- (C) $0.150$
- (D) $0.050$
**Answer:** (A)
**Concept/Formula:**
- $\frac{T_{st}}{T_{max}} = \frac{2 s_{mT}}{s_{mT}^2 + 1}$.
- Given $T_{st} = T_{fl}$ and $T_{max} = 2 T_{fl} \implies \frac{T_{st}}{T_{max}} = \frac{1}{2} = 0.5$.
- $\frac{2 s_{mT}}{s_{mT}^2 + 1} = 0.5 \implies s_{mT}^2 + 1 = 4 s_{mT} \implies s_{mT}^2 - 4 s_{mT} + 1 = 0$.
- Solving quadratic equation: $s_{mT} = \frac{4 \pm \sqrt{16 - 4}}{2} = \frac{4 \pm \sqrt{12}}{2} = 2 - \sqrt{3} \approx 2 - 1.732 = 0.268$.
- (The root $2 + \sqrt{3} = 3.732 > 1$ is unphysical for motor operation).

---

### Q-MCH-017 `[ESE-EE-2020]` 🟡 Moderate
**Topic:** Synchronous Machine — Salient Pole Theory
**Question:** In a salient-pole synchronous machine, the direct-axis synchronous reactance ($X_d$) and quadrature-axis synchronous reactance ($X_q$) satisfy the relation:
- (A) $X_d < X_q$
- (B) $X_d = X_q$
- (C) $X_d > X_q$
- (D) $X_q = 0$
**Answer:** (C)
**Concept/Formula:**
- Direct axis (d-axis) coincides with the magnetic pole axis where the air gap is minimum $\implies$ reluctance is minimum $\implies$ permeance and inductance are maximum $\implies X_d$ is large.
- Quadrature axis (q-axis) lies between the poles where the air gap is maximum $\implies$ reluctance is maximum $\implies$ inductance is small $\implies X_q$ is smaller.
- Therefore: $X_d > X_q$ (typically $X_q \approx 0.6 \text{ to } 0.7 X_d$).

---

### Q-MCH-018 `[PGCIL-EE-2021]` 🟢 Easy
**Topic:** Synchronous Machine — Hunting & Damper Windings
**Question:** Damper windings in a 3-phase synchronous alternator serve the purpose of:
- (A) Increasing the generated EMF
- (B) Suppressing hunting oscillations during sudden load changes
- (C) Improving the excitation voltage
- (D) Reducing core losses in the rotor poles
**Answer:** (B)
**Concept/Formula:**
- During steady-state synchronous operation, rotor and stator field rotate at the same speed $\implies$ no relative motion $\implies$ zero induced current in damper bars.
- When load changes suddenly, the rotor oscillates around its equilibrium load angle ($\delta$) $\implies$ relative motion induces currents in damper bars, creating an induction torque that damps out the oscillation $\implies$ **Eliminates Hunting**.
- In synchronous motors, damper windings also provide starting torque as a squirrel cage induction motor!

---

### Q-MCH-019 `[GATE-EE-2017]` 🟢 Easy
**Topic:** Single-Phase Motors — Applications
**Question:** Which of the following single-phase motors is universally used in domestic vacuum cleaners, food mixers, and portable hand drilling machines?
- (A) Shaded-pole motor
- (B) Capacitor-start capacitor-run motor
- (C) AC Universal motor (Series motor)
- (D) Split-phase induction motor
**Answer:** (C)
**Concept/Formula:**
- Universal motor is a series-wound motor that operates on both AC and DC.
- Features: High starting torque, extremely high operating speeds (up to 15,000–25,000 rpm), high power-to-weight ratio.
- Widely used in mixers, blenders, vacuum cleaners, and power drills.

---

### Q-MCH-020 `[ESE-EE-2019]` 🟢 Easy
**Topic:** Stepper Motors
**Question:** A stepper motor has a step angle of $1.8^\circ$. The number of steps required for the rotor to make 5 complete revolutions is:
- (A) 200
- (B) 1000
- (C) 500
- (D) 360
**Answer:** (B)
**Concept/Formula:**
- Steps per revolution = $\frac{360^\circ}{\text{Step angle}} = \frac{360^\circ}{1.8^\circ} = 200\text{ steps/rev}$.
- For 5 complete revolutions: Total steps = $5 \times 200 = 1000\text{ steps}$.
