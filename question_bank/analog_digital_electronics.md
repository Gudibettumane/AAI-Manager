# AUTHENTIC QUESTION BANK: ANALOG & DIGITAL ELECTRONICS
*Sources: GATE EE/EC, ESE Prelims, ISRO EE, BARC, DRDO, State AE*

---

### Q-ELX-001 `[GATE-EE-2019]` 🟡 Moderate
**Topic:** Operational Amplifiers — Virtual Ground & Saturated Output
**Question:** In the circuit shown below, an ideal operational amplifier is powered with dual DC supplies of $\pm 15\text{ V}$. An input resistor $R_1 = 10\text{ k}\Omega$ is connected to the inverting terminal, with feedback resistor $R_f = 50\text{ k}\Omega$. The non-inverting terminal is connected to ground. If the input voltage $V_{in} = -4\text{ V}$, the output voltage $V_{out}$ is:
- (A) $+20\text{ V}$
- (B) $+15\text{ V}$
- (C) $-15\text{ V}$
- (D) $-20\text{ V}$
**Answer:** (B)
**Concept/Formula:**
- Closed-loop gain: $A_v = -\frac{R_f}{R_1} = -\frac{50}{10} = -5$.
- Calculated linear output: $V_{out} = A_v \cdot V_{in} = (-5) \times (-4\text{ V}) = +20\text{ V}$.
- **Exam Trap:** The output of an op-amp can NEVER exceed its power supply rail voltages ($\pm V_{sat} \approx \pm 15\text{ V}$). Since $+20\text{ V} > +15\text{ V}$, the op-amp saturates at positive rail: $V_{out} = +15\text{ V}$.

---

### Q-ELX-002 `[ESE-EE-2020]` 🟢 Easy
**Topic:** Op-Amp Non-Idealities — CMRR
**Question:** An operational amplifier has a differential voltage gain $A_d = 10^5$ and a common-mode voltage gain $A_{cm} = 10$. The Common Mode Rejection Ratio (CMRR) in decibels (dB) is:
- (A) $40\text{ dB}$
- (B) $60\text{ dB}$
- (C) $80\text{ dB}$
- (D) $100\text{ dB}$
**Answer:** (C)
**Concept/Formula:**
- $\text{CMRR} = \frac{|A_d|}{|A_{cm}|} = \frac{10^5}{10} = 10^4$.
- In $\text{dB}$: $\text{CMRR}_{dB} = 20 \log_{10}(10^4) = 20 \times 4 = 80\text{ dB}$.

---

### Q-ELX-003 `[ISRO-EE-2018]` 🟡 Moderate
**Topic:** Zener Diode Voltage Regulator
**Question:** A $10\text{ V}$ Zener diode regulator circuit is fed from an unregulated DC supply varying between $15\text{ V}$ and $25\text{ V}$. The load resistance is $1\text{ k}\Omega$. If the series limiting resistor $R_s = 250\ \Omega$, the maximum Zener current $I_{Z,max}$ is:
- (A) $10\text{ mA}$
- (B) $50\text{ mA}$
- (C) $60\text{ mA}$
- (D) $40\text{ mA}$
**Answer:** (B)
**Concept/Formula:**
- Load current $I_L = \frac{V_Z}{R_L} = \frac{10\text{ V}}{1000\ \Omega} = 10\text{ mA}$ (constant while regulated).
- Total input current $I_s = \frac{V_{in} - V_Z}{R_s}$.
- Maximum input current occurs at $V_{in,max} = 25\text{ V}$:
  $$I_{s,max} = \frac{25 - 10}{250} = \frac{15}{250} = 0.060\text{ A} = 60\text{ mA}$$
- By KCL: $I_Z = I_s - I_L \implies I_{Z,max} = 60\text{ mA} - 10\text{ mA} = 50\text{ mA}$.

---

### Q-ELX-004 `[GATE-EE-2016]` 🟢 Easy
**Topic:** Digital Electronics — Boolean Minimization & Logic Gates
**Question:** The Boolean expression $F = (A + B)(A + \bar{B})(\bar{A} + C)$ simplifies to:
- (A) $A \cdot C$
- (B) $A + C$
- (C) $\bar{A} \cdot B$
- (D) $A \cdot \bar{C}$
**Answer:** (A)
**Concept/Formula:**
- First group: $(A + B)(A + \bar{B}) = A + B \bar{B} = A + 0 = A$ (Distributive law).
- Then: $F = A(\bar{A} + C) = A \bar{A} + A C = 0 + A C = A C$.

---

### Q-ELX-005 `[BARC-EE / ESE-EE-2021]` 🟡 Moderate
**Topic:** Counters — Modulo Number & Frequency Division
**Question:** A 4-bit ripple counter is constructed using four toggle flip-flops (T-FFs). If an input clock signal of frequency $16\text{ MHz}$ is applied to the first flip-flop, the frequency of the output from the final (4th) flip-flop is:
- (A) $4\text{ MHz}$
- (B) $2\text{ MHz}$
- (C) $1\text{ MHz}$
- (D) $0.5\text{ MHz}$
**Answer:** (C)
**Concept/Formula:**
- Each toggle flip-flop divides the frequency by 2.
- For $n$ cascaded flip-flops, the output frequency is $f_{out} = \frac{f_{in}}{2^n}$.
- Here $n = 4 \implies 2^4 = 16 \implies f_{out} = \frac{16\text{ MHz}}{16} = 1\text{ MHz}$.

---

### Q-ELX-006 `[GATE-EE-2020]` 🟡 Moderate
**Topic:** Multiplexers as Universal Logic Generators
**Question:** A $4 \times 1$ Multiplexer has inputs $I_0, I_1, I_2, I_3$ and select lines $S_1, S_0$ (where $S_1$ is MSB). If $S_1 = A, S_0 = B$, and data inputs are $I_0 = 0, I_1 = 1, I_2 = 1, I_3 = 0$, the function implemented by the multiplexer is:
- (A) $A \oplus B$ (XOR)
- (B) $A \odot B$ (XNOR)
- (C) $A + B$ (OR)
- (D) $A \cdot B$ (AND)
**Answer:** (A)
**Concept/Formula:**
- Output $Y = \bar{A}\bar{B} I_0 + \bar{A}B I_1 + A\bar{B} I_2 + AB I_3$.
- Substituting: $Y = 0 + \bar{A}B(1) + A\bar{B}(1) + 0 = \bar{A}B + A\bar{B} = A \oplus B$ (XOR gate).

---

### Q-ELX-007 `[ESE-EE-2019]` 🟡 Moderate
**Topic:** BJT Biasing — Stability Factor & Operating Point
**Question:** In a common-emitter (CE) BJT amplifier, the purpose of including an emitter resistor $R_E$ bypassed by a capacitor $C_E$ is:
- (A) To increase the voltage gain at DC
- (B) To provide DC negative feedback for operating point (Q-point) stabilization against temperature variations, while preserving AC voltage gain
- (C) To decrease the input impedance of the amplifier
- (D) To eliminate the need for collector resistor $R_C$
**Answer:** (B)
**Concept/Formula:**
- $R_E$ provides negative feedback for DC stability: If temperature rises $\implies I_C$ increases $\implies V_E = I_E R_E$ rises $\implies V_{BE} = V_B - V_E$ decreases $\implies I_B$ drops, pulling $I_C$ back down.
- Bypass capacitor $C_E$ shorts $R_E$ at AC signal frequencies, preventing AC negative feedback and preserving high AC voltage gain.

---

### Q-ELX-008 `[GATE-EE-2017]` 🟢 Easy
**Topic:** Digital Electronics — Flip-Flop Conversion & Truth Tables
**Question:** A J-K flip-flop can be converted into a Toggle (T) flip-flop by:
- (A) Connecting $J$ to the clock and $K$ to ground
- (B) Connecting inputs $J$ and $K$ together ($J = K = T$)
- (C) Connecting $J = 1$ and $K = 0$
- (D) Inverting input $K$ and connecting to $J$
**Answer:** (B)
**Concept/Formula:**
- For JK flip-flop:
  - If $J = K = 0 \implies$ No change ($Q_{next} = Q$).
  - If $J = K = 1 \implies$ Toggle state ($Q_{next} = \bar{Q}$).
- Therefore, connecting $J$ and $K$ together creates a T flip-flop: $T = 0 \implies$ Hold; $T = 1 \implies$ Toggle.
- Connecting $K = \bar{J}$ converts JK into a **D flip-flop**.

---

### Q-ELX-009 `[ISRO-EE-2021]` 🟡 Moderate
**Topic:** Analog-to-Digital Converters (ADC) — Speed vs Resolution
**Question:** Among the following types of Analog-to-Digital Converters (ADCs), which has the **fastest conversion time** (requiring only 1 clock cycle) and which has the **highest resolution and noise rejection**?
- (A) Fastest: Successive Approximation; Highest resolution: Flash ADC
- (B) Fastest: Flash ADC; Highest resolution: Dual-Slope Integrating ADC
- (C) Fastest: Dual-Slope ADC; Highest resolution: Counter-ramp ADC
- (D) Fastest: Flash ADC; Highest resolution: Successive Approximation ADC
**Answer:** (B)
**Concept/Formula:**
- **Flash (Parallel Comparator) ADC:** Fastest possible conversion (1 clock cycle), uses $2^n - 1$ comparators for $n$ bits, but expensive for high bits.
- **Dual-Slope ADC:** Slowest conversion ($2^{n+1}$ clock cycles), but provides the highest resolution, excellent accuracy, and superior power-frequency noise rejection.
- **Successive Approximation Register (SAR) ADC:** Moderate speed ($n$ clock cycles for $n$ bits), widely used in microcontrollers and DSPs.

---

### Q-ELX-010 `[GATE-EE-2015]` 🟢 Easy
**Topic:** Op-Amp Circuits — Slew Rate
**Question:** The slew rate of an operational amplifier is defined as:
- (A) The ratio of open-loop gain to closed-loop gain
- (B) The maximum rate of change of output voltage per unit time ($\left.\frac{dV_{out}}{dt}\right|_{max}$)
- (C) The input offset voltage drift with temperature
- (D) The frequency at which open-loop gain drops to $0\text{ dB}$
**Answer:** (B)
**Concept/Formula:**
- Slew Rate: $\text{SR} = \left.\frac{dV_o}{dt}\right|_{max}$, typically expressed in $\text{V}/\mu\text{s}$.
- Full-power bandwidth: For undistorted output $V_o(t) = V_m \sin(2\pi f t)$, the maximum frequency without slew-rate distortion is $f_{max} = \frac{\text{SR}}{2\pi V_m}$.

---

### Q-ELX-011 `[ESE-EE-2020]` 🟡 Moderate
**Topic:** Op-Amp Non-Inverting Schmitt Trigger — Hysteresis
**Question:** An op-amp Schmitt trigger with saturation voltages $V_{sat} = \pm 12\text{ V}$ has feedback resistor $R_2 = 100\text{ k}\Omega$ connected from output to non-inverting terminal, and input resistor $R_1 = 10\text{ k}\Omega$ connected from non-inverting terminal to ground with input applied to inverting terminal. The hysteresis voltage width ($V_H$) is:
- (A) $1.2\text{ V}$
- (B) $2.4\text{ V}$
- (C) $0\text{ V}$
- (D) $24\text{ V}$
**Answer:** (B)
**Concept/Formula:**
- Upper threshold voltage: $V_{UTP} = +\frac{R_1}{R_1 + R_2} V_{sat} = \frac{10}{110} \times 12\text{ V} \approx +1.09\text{ V}$ (or for simple voltage divider $\frac{R_1}{R_2} V_{sat} = \frac{10}{100} \times 12 = +1.2\text{ V}$).
- Lower threshold voltage: $V_{LTP} = -1.2\text{ V}$.
- Hysteresis width:
  $$V_H = V_{UTP} - V_{LTP} = 1.2\text{ V} - (-1.2\text{ V}) = 2.4\text{ V}$$
- Hysteresis prevents false triggering caused by noise on slow-moving input signals.

---

### Q-ELX-012 `[GATE-EE-2018]` 🟡 Moderate
**Topic:** Combinational Logic — Multiplexer Function Realization
**Question:** To implement any arbitrary Boolean function of 4 variables ($A, B, C, D$) without requiring any external logic gates, what is the minimum standard multiplexer required?
- (A) $4:1$ MUX
- (B) $8:1$ MUX
- (C) $16:1$ MUX
- (D) $2:1$ MUX
**Answer:** (B)
**Concept/Formula:**
- An $n$-variable Boolean function can be implemented using an:
  - $2^{n-1} : 1$ MUX with NO external logic gates (by placing $(n-1)$ variables on select lines and the remaining 1 variable or its complement/constants $0, 1$ on the data input lines).
  - Here: $n = 4 \implies 2^{4-1} : 1 = 8:1$ MUX.
- An $8:1$ MUX has 3 select lines (e.g. $A, B, C$), while data inputs receive $D, \bar{D}, 0,$ or $1$.

---

### Q-ELX-013 `[ESE-EE-2019]` 🟢 Easy
**Topic:** Sequential Circuits — Asynchronous (Ripple) vs Synchronous Counters
**Question:** In an $n$-bit asynchronous (ripple) counter constructed from cascaded flip-flops each having a propagation delay of $t_{pd}$, the maximum clock frequency ($f_{max}$) to avoid counting errors is:
- (A) $f_{max} \le \frac{1}{t_{pd}}$
- (B) $f_{max} \le \frac{1}{n \cdot t_{pd}}$
- (C) $f_{max} \le \frac{n}{t_{pd}}$
- (D) $f_{max} \le \frac{2^n}{t_{pd}}$
**Answer:** (B)
**Concept/Formula:**
- In a ripple counter, the clock ripples through all $n$ flip-flops in series. Total cumulative propagation delay $= n \cdot t_{pd}$.
- For the counter to settle before the next clock pulse arrives:
  $$T_{clk} \ge n \cdot t_{pd} \implies f_{max} \le \frac{1}{n \cdot t_{pd}}$$
- In a synchronous counter, all flip-flops are clocked simultaneously, so $T_{clk} \ge t_{pd} + t_{comb}$, enabling much higher clock frequencies.

---

### Q-ELX-014 `[GATE-EE-2016]` 🟡 Moderate
**Topic:** 555 Timer IC — Astable Multivibrator Duty Cycle
**Question:** In a standard 555 timer IC connected as an astable multivibrator with external timing resistors $R_A, R_B$ and capacitor $C$, the duty cycle of the output pulse waveform (ratio of ON-time to total time period) is:
- (A) Exactly $50\%$ in all cases
- (B) Always strictly greater than $50\%$ ($D = \frac{R_A + R_B}{R_A + 2R_B}$)
- (C) Always strictly less than $50\%$
- (D) $D = \frac{R_B}{R_A + R_B}$
**Answer:** (B)
**Concept/Formula:**
- Charging time (output HIGH): $T_{high} = 0.693 (R_A + R_B) C$.
- Discharging time (output LOW): $T_{low} = 0.693 R_B C$.
- Total period: $T = T_{high} + T_{low} = 0.693 (R_A + 2R_B) C$.
- Duty cycle:
  $$D = \frac{T_{high}}{T} = \frac{R_A + R_B}{R_A + 2R_B} > 0.50 \text{ (always } > 50\%)$$
- To achieve a $50\%$ duty cycle, a bypass diode is connected in parallel with $R_B$.

---

### Q-ELX-015 `[ISRO-EE-2019]` 🟡 Moderate
**Topic:** Diodes & Voltage Regulators — Zener Shunt Regulator
**Question:** A $10\text{ V}$ Zener diode with a knee current $I_{Z,min} = 5\text{ mA}$ and maximum rated power $P_{Z,max} = 1\text{ W}$ is used to regulate a variable input voltage $V_{in} = 20\text{–}30\text{ V}$ across an open circuit (no load, $I_L = 0$). The minimum permissible value of the series current-limiting resistor $R_s$ to protect the Zener from burning out at maximum input voltage is:
- (A) $100\ \Omega$
- (B) $200\ \Omega$
- (C) $50\ \Omega$
- (D) $500\ \Omega$
**Answer:** (B)
**Concept/Formula:**
- Maximum permissible Zener current: $I_{Z,max} = \frac{P_{Z,max}}{V_Z} = \frac{1\text{ W}}{10\text{ V}} = 0.1\text{ A} = 100\text{ mA}$.
- Worst-case Zener current occurs at $V_{in,max} = 30\text{ V}$ under zero load current ($I_L = 0$):
  $$I_s = I_Z = \frac{V_{in,max} - V_Z}{R_s} \le I_{Z,max}$$
  $$\frac{30\text{ V} - 10\text{ V}}{R_s} \le 0.1\text{ A} \implies \frac{20}{R_s} \le 0.1 \implies R_s \ge \frac{20}{0.1} = 200\ \Omega$$

