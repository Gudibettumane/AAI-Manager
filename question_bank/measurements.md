# AUTHENTIC QUESTION BANK: MEASUREMENTS & INSTRUMENTATION
*Sources: AAI JE/Manager PYQs, ESE Prelims EE, GATE EE, ISRO, SSC JE*

---

### Q-MSM-001 `[AAI-JE-EE-2018]` 🟢 Easy
**Topic:** Indicating Instruments — Comparison
**Question:** A Moving Iron (MI) instrument can be used for measuring:
- (A) DC only
- (B) AC only
- (C) Both DC and AC
- (D) High frequencies above $100\text{ kHz}$ only
**Answer:** (C)
**Concept/Formula:** Deflecting torque in MI instruments is $T_d = \frac{1}{2} I^2 \frac{dL}{d\theta}$. Since $T_d \propto I^2$, the deflection is in the same direction regardless of current polarity, and it reads RMS values on AC. Scale is non-linear (cramped at the beginning).

---

### Q-MSM-002 `[ESE-EE-2019]` 🟡 Moderate
**Topic:** Ammeter Shunt Calculation
**Question:** A galvanometer with a coil resistance of $50\ \Omega$ has a full-scale deflection of $1\text{ mA}$. To convert it into an ammeter reading up to $10\text{ A}$, the required shunt resistance is approximately:
- (A) $0.005\ \Omega$
- (B) $0.05\ \Omega$
- (C) $0.5\ \Omega$
- (D) $5.0\ \Omega$
**Answer:** (A)
**Concept/Formula:**
- Multiplying power $m = \frac{I}{I_m} = \frac{10\text{ A}}{1 \times 10^{-3}\text{ A}} = 10000$.
- $R_{sh} = \frac{R_m}{m - 1} = \frac{50}{10000 - 1} \approx \frac{50}{10000} = 0.005\ \Omega$.

---

### Q-MSM-003 `[GATE-EE-2017]` 🟢 Easy
**Topic:** AC Bridges for Inductance
**Topic Note:** High-Q vs Medium-Q vs Low-Q
**Question:** Hay's bridge is most suitable for measuring:
- (A) Inductance of high-Q coils ($Q > 10$)
- (B) Inductance of low-Q coils ($Q < 1$)
- (C) Capacitance
- (D) Resistance below $1\ \Omega$
**Answer:** (A)
**Concept/Formula:**
- Hay's bridge uses a capacitor in series with resistance in the standard arm, making it suitable for high-Q coils ($Q > 10$).
- Maxwell's bridge uses parallel RC arm and is suitable for medium-Q coils ($1 < Q < 10$).
- Anderson bridge is best for low-Q coils ($Q < 1$).
- Kelvin Double Bridge is for low resistance ($< 1\ \Omega$).
- Schering Bridge is for capacitance and dielectric loss / dissipation factor ($\tan \delta$).

---

### Q-MSM-004 `[AAI-JE-EE-2018]` 🟡 Moderate
**Topic:** Electrodynamometer Wattmeter Errors
**Question:** When a wattmeter is connected with its pressure coil (voltage coil) connected on the load side, the error in measurement is due to:
- (A) Power loss in the current coil
- (B) Power loss in the pressure coil
- (C) Inductance of the current coil
- (D) Mutual inductance between coils
**Answer:** (B)
**Concept/Formula:**
- When pressure coil is connected on the load side: Wattmeter reading = Load Power + Power loss in Pressure Coil ($V^2 / R_p$).
- When pressure coil is connected on the supply side: Wattmeter reading = Load Power + Power loss in Current Coil ($I^2 R_c$).

---

### Q-MSM-005 `[ESE-EE-2020]` 🟢 Easy
**Topic:** CRO — Lissajous Figures
**Question:** If the Lissajous pattern displayed on a Cathode Ray Oscilloscope (CRO) is a straight line passing through the first and third quadrants at an angle of $45^\circ$, the phase difference between the two sinusoidal input signals of equal frequency is:
- (A) $0^\circ$
- (B) $90^\circ$
- (C) $180^\circ$
- (D) $270^\circ$
**Answer:** (A)
**Concept/Formula:**
- Phase difference $\phi = 0^\circ$ or $360^\circ$: Straight line with positive slope (1st and 3rd quadrants).
- $\phi = 90^\circ$ or $270^\circ$: Circle (if equal amplitudes) or Ellipse with major/minor axes along the coordinate axes.
- $\phi = 180^\circ$: Straight line with negative slope (2nd and 4th quadrants).

---

### Q-MSM-006 `[GATE-EE-2018]` 🟡 Moderate
**Topic:** Induction Type Energy Meter — Creeping & Braking
**Question:** "Creeping" in a single-phase induction energy meter refers to the slow, continuous rotation of the disc under:
- (A) Full load at zero power factor
- (B) No-load when voltage is applied across the pressure coil
- (C) Heavy overloads with lagging power factor
- (D) Complete de-energization of both coils
**Answer:** (B)
**Concept/Formula:**
- Creeping is the rotation of the disc when ONLY voltage is applied to the pressure coil and NO current flows through the current coil ($I = 0$).
- Causes: Overcompensation for friction (excess friction-compensating torque), excessive supply voltage, stray magnetic fields, vibrations.
- Prevention: Drilling two diametrically opposite holes in the aluminum disc.

---

### Q-MSM-007 `[ESE-EE-2021]` 🟡 Moderate
**Topic:** Current Transformers (CT) — Ratio & Phase Angle Error
**Question:** In a Current Transformer (CT), the phase angle error $\theta$ is primarily caused by:
- (A) Secondary winding copper loss
- (B) The core loss component of the exciting current ($I_c$)
- (C) The magnetizing component of the exciting current ($I_m$)
- (D) The primary leakage reactance
**Answer:** (B)
**Concept/Formula:**
- Phase angle error $\theta \approx \frac{I_m \cos \delta - I_c \sin \delta}{n I_s} \text{ rad}$. For a purely resistive secondary burden ($\delta = 0$), $\theta \approx \frac{I_m}{n I_s}$. But when considering ratio error:
  - Ratio error is governed mainly by the magnetizing current $I_m$ (for lagging burden) and core loss current $I_c$.
  - Phase angle error is governed mainly by $I_m$ and $I_c$. In inductive burden, the core loss component $I_c$ directly shifts the phase relationship.
- **Crucial Rule:** The secondary of an energized CT must **NEVER be open-circuited**, because all primary current becomes magnetizing current, producing dangerous high voltage across secondary terminals and severe core saturation/heating.

---

### Q-MSM-008 `[GATE-EE-2019]` 🟢 Easy
**Topic:** Transducers — LVDT
**Question:** A Linear Variable Differential Transformer (LVDT) is an inductive transducer used for the measurement of:
- (A) Temperature
- (B) Linear displacement
- (C) Rotational acceleration
- (D) Light intensity
**Answer:** (B)
**Concept/Formula:**
- LVDT converts linear mechanical displacement of a magnetic core into a differential AC voltage ($V_{out} = V_{s1} - V_{s2}$).
- At null position: $V_{s1} = V_{s2} \implies V_{out} = 0$.
- High linearity, wide dynamic range, and frictionless operation.

---

### Q-MSM-009 `[ESE-EE-2020]` 🟡 Moderate
**Topic:** Digital Voltmeter (DVM) — Dual-Slope Integration
**Question:** A Dual-Slope Integrating Digital Voltmeter is preferred over ramp-type DVMs because:
- (A) It has the fastest conversion speed
- (B) Its conversion accuracy is independent of both clock frequency and integrator resistance/capacitance values ($R$ and $C$)
- (C) It requires no reference voltage
- (D) It directly measures frequency instead of voltage
**Answer:** (B)
**Concept/Formula:**
- In dual-slope DVM: $V_{in} \cdot T_1 = V_{ref} \cdot T_2 \implies T_2 = T_1 \frac{V_{in}}{V_{ref}}$.
- Count $N = T_2 \cdot f_{clk} = (N_1 \frac{1}{f_{clk}}) \frac{V_{in}}{V_{ref}} f_{clk} = N_1 \frac{V_{in}}{V_{ref}}$.
- The final count is completely independent of integrator values $R, C$ and clock frequency $f_{clk}$!
- Excellent noise rejection (especially $50\text{ Hz}$ power line noise if $T_1$ is set to multiples of $20\text{ ms}$).

---

### Q-MSM-010 `[ISRO-EE-2020]` 🟢 Easy
**Topic:** AC Bridges — Wien Bridge
**Question:** A Wien bridge is uniquely used for the accurate measurement of:
- (A) Very high resistance ($> 100\text{ M}\Omega$)
- (B) Audio frequency
- (C) Self-inductance of low-Q coils
- (D) Mutual inductance
**Answer:** (B)
**Concept/Formula:**
- Wien bridge balance condition: $f = \frac{1}{2\pi \sqrt{R_1 R_2 C_1 C_2}}$.
- If $R_1 = R_2 = R$ and $C_1 = C_2 = C$, then $f = \frac{1}{2\pi R C}$.
- Extensively used as a frequency-determining network in audio frequency oscillators and distortion analyzers.
