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
