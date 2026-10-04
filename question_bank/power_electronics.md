# AUTHENTIC QUESTION BANK: POWER ELECTRONICS & DRIVES
*Sources: AAI JE/Manager PYQs, ESE Prelims EE, GATE EE, ISRO, PGCIL*

---

### Q-PEL-001 `[AAI-JE-EE-2018]` 🟢 Easy
**Topic:** SCR Ratings — Latching vs Holding Current
**Question:** In a Thyristor (SCR), the latching current is:
- (A) Associated with the turn-off process and is lower than the holding current
- (B) Associated with the turn-on process and is higher than the holding current
- (C) Exactly equal to the holding current
- (D) Independent of gate pulse duration
**Answer:** (B)
**Concept/Formula:** 
- Latching current ($I_L$): Minimum anode current that must be attained during turn-on before the gate trigger pulse is removed so that the SCR remains ON.
- Holding current ($I_H$): Minimum anode current below which the SCR turns OFF during commutation.
- Fundamental rule: $I_L > I_H$ (typically $I_L \approx 2 \text{ to } 3 \times I_H$).

---

### Q-PEL-002 `[ESE-EE-2020]` 🟡 Moderate
**Topic:** Single-Phase Full Converter
**Question:** A single-phase fully controlled bridge converter is fed from a $230\text{ V},\ 50\text{ Hz}$ AC source. If the firing angle $\alpha = 60^\circ$ and load current is continuous and ripple-free, the average DC output voltage is:
- (A) $103.5\text{ V}$
- (B) $207.1\text{ V}$
- (C) $146.4\text{ V}$
- (D) $230.0\text{ V}$
**Answer:** (A)
**Concept/Formula:**
- $V_{dc} = \frac{2 V_m}{\pi} \cos \alpha = \frac{2 \times (230 \sqrt{2})}{\pi} \cos 60^\circ$.
- $V_{dc} = \frac{2 \times 325.27}{\pi} \times 0.5 = \frac{325.27}{\pi} \approx 103.54\text{ V}$.

---

### Q-PEL-003 `[GATE-EE-2017]` 🟡 Moderate
**Topic:** DC-DC Choppers
**Question:** A step-down DC chopper operates from a $100\text{ V}$ DC supply and feeds an $RL$ load. The switching frequency is $1\text{ kHz}$ and the duty cycle $D = 0.4$. The average output voltage is:
- (A) $40\text{ V}$
- (B) $60\text{ V}$
- (C) $250\text{ V}$
- (D) $100\text{ V}$
**Answer:** (A)
**Concept/Formula:**
- Buck / Step-down chopper: $V_{o,avg} = D \times V_s = 0.4 \times 100\text{ V} = 40\text{ V}$.
- For boost / step-up chopper: $V_{o,avg} = \frac{V_s}{1 - D}$.

---

### Q-PEL-004 `[ESE-EE-2019]` 🟢 Easy
**Topic:** Inverters — Output Harmonics & PWM
**Question:** In single-pulse width modulation (PWM) of a single-phase voltage source inverter, to completely eliminate the $n$-th harmonic from the output voltage waveform, the pulse width $2d$ must be chosen such that:
- (A) $2d = \frac{180^\circ}{n}$
- (B) $2d = \frac{360^\circ}{n}$
- (C) $2d = n \times 180^\circ$
- (D) $2d = \frac{90^\circ}{n}$
**Answer:** (B)
**Concept/Formula:**
- The $n$-th harmonic amplitude in single-pulse PWM is proportional to $\sin(n d)$.
- To eliminate the $n$-th harmonic: $\sin(n d) = 0 \implies n d = 180^\circ \implies d = \frac{180^\circ}{n}$.
- Therefore, the full pulse width $2d = \frac{360^\circ}{n}$.
- Example: To eliminate the 3rd harmonic ($n=3$), pulse width $2d = \frac{360^\circ}{3} = 120^\circ$.

---

### Q-PEL-005 `[GATE-EE-2018]` 🟡 Moderate
**Topic:** 3-Phase Voltage Source Inverter — Conduction Modes
**Question:** In a 3-phase Voltage Source Inverter (VSI) operating in $180^\circ$ conduction mode with a DC link voltage $V_{dc}$, the RMS value of the fundamental line-to-line voltage is:
- (A) $\frac{\sqrt{6}}{\pi} V_{dc} \approx 0.78 V_{dc}$
- (B) $\frac{\sqrt{2}}{\pi} V_{dc} \approx 0.45 V_{dc}$
- (C) $\frac{2}{\pi} V_{dc} \approx 0.636 V_{dc}$
- (D) $\frac{\sqrt{3}}{\pi} V_{dc} \approx 0.55 V_{dc}$
**Answer:** (A)
**Concept/Formula:**
- For $180^\circ$ conduction VSI:
  - RMS fundamental phase voltage $V_{ph1,rms} = \frac{\sqrt{2}}{\pi} V_{dc} \approx 0.45 V_{dc}$.
  - RMS fundamental line voltage $V_{L1,rms} = \sqrt{3} V_{ph1,rms} = \frac{\sqrt{6}}{\pi} V_{dc} \approx 0.7797 V_{dc} \approx 0.78 V_{dc}$.
  - Total RMS line voltage $V_{L,rms} = \sqrt{\frac{2}{3}} V_{dc} \approx 0.8165 V_{dc}$.

---

### Q-PEL-006 `[ESE-EE-2020]` 🟢 Easy
**Topic:** Snubber Circuit Protection
**Question:** An RC snubber circuit connected in parallel across an SCR is used to protect the device against:
- (A) High rate of rise of current ($di/dt$)
- (B) High rate of rise of voltage ($dv/dt$)
- (C) Steady-state overcurrent
- (D) Low gate voltage
**Answer:** (B)
**Concept/Formula:**
- $dv/dt$ protection $\implies$ **RC snubber circuit** connected in parallel with the SCR.
- $di/dt$ protection $\implies$ **Small series inductor** ($L$) connected in series with the SCR.
- Overvoltage protection $\implies$ **Varistor (MOV)** across the device.
- Overcurrent protection $\implies$ **Fast-acting semiconductor fuse**.

---

### Q-PEL-007 `[GATE-EE-2015]` 🟡 Moderate
**Topic:** 3-Phase Full Converter (6-Pulse)
**Question:** A 3-phase fully controlled 6-pulse bridge converter is fed from a $400\text{ V},\ 50\text{ Hz}$ supply. For a firing angle $\alpha = 30^\circ$, the average output DC voltage (assuming continuous load current) is:
- (A) $270\text{ V}$
- (B) $467.6\text{ V}$
- (C) $540\text{ V}$
- (D) $380\text{ V}$
**Answer:** (B)
**Concept/Formula:**
- $V_{dc} = \frac{3 V_{ml}}{\pi} \cos \alpha = \frac{3 \times (400 \sqrt{2})}{\pi} \cos 30^\circ$.
- $V_{dc} = \frac{3 \times 565.68}{\pi} \times \frac{\sqrt{3}}{2} = \frac{1697.05}{\pi} \times 0.866 \approx 540.19 \times 0.866 \approx 467.8\text{ V}$.

---

### Q-PEL-008 `[ISRO-EE-2020]` 🟢 Easy
**Topic:** Power Switching Devices — Comparison
**Question:** Which power semiconductor device has the highest switching speed and lowest gate drive power requirement, making it ideal for high-frequency low-to-medium power converters ($> 100\text{ kHz}$)?
- (A) Power BJT
- (B) GTO
- (C) Power MOSFET
- (D) IGBT
**Answer:** (C)
**Concept/Formula:**
- Power MOSFET is a majority carrier, voltage-controlled device.
- Does not suffer from minority carrier storage delay $\implies$ fastest switching speeds (up to several MHz) with negligible gate drive power.
- IGBT combines the low on-state conduction loss of a BJT with the high input impedance of a MOSFET, but switches slower than a MOSFET (typically up to 20–50 kHz).
