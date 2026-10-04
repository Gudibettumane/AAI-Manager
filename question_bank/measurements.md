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
