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

---

### Q-PEL-009 `[GATE-EE-2019]` 🟡 Moderate
**Topic:** DC-DC Boost Converter — Continuous Conduction Mode
**Question:** A boost converter is supplied from a $24\text{ V}$ DC source and delivers power to a $48\text{ V}$ DC load. Assuming ideal switching components and continuous conduction mode, what is the duty cycle $D$ of the switch?
- (A) $0.25$
- (B) $0.50$
- (C) $0.75$
- (D) $0.67$
**Answer:** (B)
**Concept/Formula:**
- For an ideal boost converter in CCM:
  $$V_o = \frac{V_s}{1 - D} \implies 48 = \frac{24}{1 - D} \implies 1 - D = \frac{24}{48} = 0.5 \implies D = 0.50$$
- Inductor peak-to-peak current ripple: $\Delta I_L = \frac{V_s D}{f_s L}$.

---

### Q-PEL-010 `[ESE-EE-2021]` 🟢 Easy
**Topic:** Controlled Rectifiers — Role of Freewheeling Diode (FD)
**Question:** In a single-phase half-controlled or full-controlled rectifier feeding a highly inductive $RL$ load, connecting a freewheeling diode across the load:
- (A) Causes the output voltage to become negative during part of the cycle
- (B) Prevents the load voltage from going negative, improves the input displacement power factor, and allows smooth decay of load current by circulating inductive energy through the diode
- (C) Increases the ripple factor of the output voltage
- (D) Increases the reverse recovery stress on the main thyristors
**Answer:** (B)
**Concept/Formula:**
- When the AC supply voltage reverses polarity, the induced EMF in the load inductor forward-biases the freewheeling diode ($D_{fw}$).
- Current commutates from the thyristors to $D_{fw}$, clamping the terminal voltage to $\approx 0\text{ V}$ and preventing negative voltage spikes.
- Reduces reactive power drawn from the AC source $\implies$ improves input power factor.

---

### Q-PEL-011 `[GATE-EE-2016]` 🟡 Moderate
**Topic:** Dual Converters — Firing Angle Relationship
**Question:** In a dual converter consisting of two back-to-back 3-phase full converters operating in the circulating-current mode, to ensure that the average DC output voltages of both converters are equal and opposite ($V_{dc1} = -V_{dc2}$), the firing angles $\alpha_1$ and $\alpha_2$ must satisfy:
- (A) $\alpha_1 + \alpha_2 = 180^\circ$
- (B) $\alpha_1 - \alpha_2 = 90^\circ$
- (C) $\alpha_1 + \alpha_2 = 90^\circ$
- (D) $\alpha_1 = \alpha_2$
**Answer:** (A)
**Concept/Formula:**
- For Converter 1: $V_{dc1} = V_{do} \cos \alpha_1$.
- For Converter 2: $V_{dc2} = V_{do} \cos \alpha_2$.
- For four-quadrant operation without short-circuiting the average DC levels:
  $$V_{dc1} = -V_{dc2} \implies \cos \alpha_1 = -\cos \alpha_2 = \cos(180^\circ - \alpha_2) \implies \alpha_1 + \alpha_2 = 180^\circ$$
- A current-limiting reactor is connected between the two converters to limit instantaneous circulating ripple current.

---

### Q-PEL-012 `[ESE-EE-2020]` 🟡 Moderate
**Topic:** Inverters — Sinusoidal Pulse Width Modulation (SPWM)
**Question:** In a single-phase full-bridge inverter controlled by Sinusoidal PWM, the peak amplitude of the reference modulating sine wave is $A_m = 4\text{ V}$ and the peak amplitude of the triangular carrier wave is $A_c = 5\text{ V}$. If the DC link voltage is $V_{dc} = 200\text{ V}$, the peak amplitude of the fundamental output phase voltage is:
- (A) $160\text{ V}$
- (B) $200\text{ V}$
- (C) $80\text{ V}$
- (D) $250\text{ V}$
**Answer:** (A)
**Concept/Formula:**
- Amplitude modulation index: $m_a = \frac{A_m}{A_c} = \frac{4}{5} = 0.8$.
- In the linear modulation range ($0 \le m_a \le 1$), the peak value of the fundamental output voltage is:
  $$\hat{V}_{o1} = m_a \cdot V_{dc} = 0.8 \times 200\text{ V} = 160\text{ V}$$
- RMS value of the fundamental output: $V_{o1,rms} = \frac{160}{\sqrt{2}} \approx 113.1\text{ V}$.

---

### Q-PEL-013 `[AAI-Manager-EE / PGCIL]` 🟢 Easy
**Topic:** AC Drives — V/f Control of 3-Phase Induction Motors
**Question:** In Variable Frequency Drives (VFDs) controlling chilled water pumps and AHU fans, the ratio of stator voltage to supply frequency ($V/f$) is held constant below rated base speed primarily to:
- (A) Keep the air-gap magnetic flux ($\Phi_m$) constant and prevent magnetic core saturation
- (B) Maximize rotor copper loss
- (C) Keep the motor running at synchronous speed
- (D) Eliminate slip completely
**Answer:** (A)
**Concept/Formula:**
- Induced stator EMF is given by: $E_1 \approx V_1 \approx 4.44 f N_1 \Phi_m K_{w1} \implies \Phi_m \propto \frac{V}{f}$.
- If frequency is reduced while keeping voltage constant, $V/f$ shoots up, driving the magnetic core into deep saturation, causing excessive magnetizing current, distorted waveform, and catastrophic overheating.
- Holding $V/f$ constant maintains rated maximum torque capability across the entire low-speed operating band (constant torque region).

---

### Q-PEL-014 `[ESE-EE-2018]` 🟡 Moderate
**Topic:** Frequency Converters — Cycloconverters
**Question:** A naturally commutated, line-synchronized thyristor cycloconverter converting 3-phase $50\text{ Hz}$ AC power directly to variable-frequency AC power is practically limited to an output frequency ($f_o$) range of:
- (A) $f_o \le \frac{1}{3} \text{ to } \frac{1}{2}$ of input supply frequency ($0\text{ to } 15\text{–}20\text{ Hz}$)
- (B) $f_o \ge 500\text{ Hz}$
- (C) $f_o$ between $100\text{ Hz}$ and $200\text{ Hz}$ only
- (D) Infinite frequency
**Answer:** (A)
**Concept/Formula:**
- Naturally commutated cycloconverters rely on the AC line voltage zero-crossings for thyristor turn-off.
- To maintain acceptable output waveform quality and avoid excessive sub-harmonics, the output frequency is constrained to $f_o \le \frac{1}{3} f_{in}$ (i.e. $\le 16.7\text{ Hz}$ for $50\text{ Hz}$ input).
- Widely employed in heavy, high-power, low-speed direct drives such as cement kilns, rolling mills, and mine winders.

---

### Q-PEL-015 `[PGCIL-EE / GATE-EE]` 🟡 Moderate
**Topic:** FACTS & Power Quality — STATCOM vs SVC
**Question:** A Static Synchronous Compensator (STATCOM) is superior to a conventional Static VAR Compensator (SVC) for dynamic reactive power compensation in power systems because:
- (A) At depressed line voltages during power system faults, STATCOM maintains a constant maximum capacitive reactive output current ($I_q$), whereas an SVC's reactive power injection degrades quadratically ($Q \propto V^2$)
- (B) STATCOM uses giant mechanical capacitors only
- (C) STATCOM consumes active power continuously
- (D) STATCOM cannot operate in leading power factor mode
**Answer:** (A)
**Concept/Formula:**
- **SVC (TCR/TSC):** Acts as a variable admittance ($B$). Reactive current $I = B \cdot V \implies Q = B \cdot V^2$. When grid voltage drops to $0.7\text{ p.u.}$, SVC output collapses to $0.49\text{ p.u.}$.
- **STATCOM (VSC based):** Acts as a controllable voltage source behind a coupling reactance. Its maximum output current is independent of system voltage: $I_{max} = \text{constant} \implies Q \propto V$. Thus, at $0.7\text{ p.u.}$ voltage, it still delivers $0.7\text{ p.u.}$ reactive power, providing vastly superior transient voltage support.

