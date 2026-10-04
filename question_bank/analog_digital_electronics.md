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
