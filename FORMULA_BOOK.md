# AAI MANAGER (ELECTRICAL) — CUMULATIVE FORMULA BOOK

**Official Notification:** Advt. No: 12/2026/CHQ/DR-CBT  
**Usage Rules:**
- Classified into `[Essential]` (must memorize without hesitation), `[Important]` (frequently needed for numericals), and `[Useful]` (shortcuts and rules of thumb).
- **3-Strike Penalty Box:** Any formula missed three times enters the Penalty Box and must be tested at the start of three consecutive sessions until 100% recalled.

---

## 0. FORMULA PENALTY BOX (Active Strikes)

| Formula ID | Concept / Equation | Subject | Strikes (1-3) | Penalty Status | Retest Sessions Left |
|---|---|---|---|---|---|
| *None currently in Penalty Box* | — | — | 0 | CLEAR | 0 |

---

## 1. Circuit Theory (CKT)

### [Essential]
- **KCL & KVL:** $\sum I_{node} = 0$, $\sum V_{loop} = 0$.
- **Graph Theory Relations:**
  - Nodes $= N$, Branches $= B$.
  - Number of Tree Branches (Twigs) $= N - 1$.
  - Number of Links (Chords / Fundamental Loops) $= L = B - N + 1$.
  - Rank of Incidence Matrix $= N - 1$.
- **Thevenin & Norton Equivalence:**
  - $V_{th} = V_{oc}$, $I_N = I_{sc}$, $R_{th} = R_N = \frac{V_{oc}}{I_{sc}}$ (for circuits with independent sources).
  - Maximum Power Transfer Theorem: $P_{max} = \frac{V_{th}^2}{4 R_L}$ when $R_L = R_{th}$ (DC) or $Z_L = Z_{th}^*$ (AC).
- **First-Order Transients:**
  - $x(t) = x(\infty) + [x(0^+) - x(\infty)] e^{-t/\tau}$.
  - RL Circuit: $\tau = \frac{L}{R}$, $i_L(0^-) = i_L(0^+)$.
  - RC Circuit: $\tau = R C$, $v_C(0^-) = v_C(0^+)$.
- **Resonance (Series RLC):**
  - $\omega_0 = \frac{1}{\sqrt{LC}}$, $f_0 = \frac{1}{2\pi\sqrt{LC}}$.
  - Quality Factor: $Q = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 C R} = \frac{1}{R}\sqrt{\frac{L}{C}}$.
  - Bandwidth: $BW = \frac{f_0}{Q} = \frac{R}{2\pi L}\text{ Hz} = \frac{R}{L}\text{ rad/s}$.
  - At resonance: Impedance is minimum ($Z = R$), current is maximum, power factor is unity.

### [Important]
- **Coupled Inductors:**
  - $v_1 = L_1 \frac{di_1}{dt} \pm M \frac{di_2}{dt}$, $v_2 = \pm M \frac{di_1}{dt} + L_2 \frac{di_2}{dt}$.
  - Coefficient of Coupling: $k = \frac{M}{\sqrt{L_1 L_2}}$, where $0 \le k \le 1$.
  - Series Aiding: $L_{eq} = L_1 + L_2 + 2M$. Series Opposing: $L_{eq} = L_1 + L_2 - 2M$.
- **Two-Port Network Parameters:**
  - **Z-Parameters:** $V_1 = Z_{11} I_1 + Z_{12} I_2$; $V_2 = Z_{21} I_1 + Z_{22} I_2$. (Reciprocal: $Z_{12} = Z_{21}$; Symmetric: $Z_{11} = Z_{22}$).
  - **Y-Parameters:** $I_1 = Y_{11} V_1 + Y_{12} V_2$; $I_2 = Y_{21} V_1 + Y_{22} V_2$. (Reciprocal: $Y_{12} = Y_{21}$; Symmetric: $Y_{11} = Y_{22}$).
  - **ABCD-Parameters:** $V_1 = A V_2 - B I_2$; $I_1 = C V_2 - D I_2$. (Reciprocal: $AD - BC = 1$; Symmetric: $A = D$).
  - **h-Parameters:** $V_1 = h_{11} I_1 + h_{12} V_2$; $I_2 = h_{21} I_1 + h_{22} V_2$. (Reciprocal: $h_{12} = -h_{21}$; Symmetric: $\Delta h = 1$).
- **Balanced 3-Phase Circuits:**
  - Star (Y): $V_L = \sqrt{3} V_{ph} \angle 30^\circ$, $I_L = I_{ph}$.
  - Delta ($\Delta$): $V_L = V_{ph}$, $I_L = \sqrt{3} I_{ph} \angle -30^\circ$.
  - Total Power: $P = \sqrt{3} V_L I_L \cos\phi = 3 V_{ph} I_{ph} \cos\phi$.
  - Two-Wattmeter Method: $W_1 = V_L I_L \cos(30^\circ - \phi)$, $W_2 = V_L I_L \cos(30^\circ + \phi)$.
  - Total Power $P = W_1 + W_2$, $\tan\phi = \sqrt{3} \frac{W_1 - W_2}{W_1 + W_2}$.

---

## 2. Electrical Machines (MCH & SPM)

### [Essential]
- **Transformer EMF Equation:**
  - $E_1 = 4.44 f N_1 \Phi_m$, $E_2 = 4.44 f N_2 \Phi_m$.
- **Transformer Voltage Regulation:**
  - $\%VR = \frac{I_2 R_{eq2} \cos\phi_2 \pm I_2 X_{eq2} \sin\phi_2}{V_2} \times 100\%$ ($+$ for lagging, $-$ for leading).
  - Zero regulation occurs at leading pf: $\tan\phi_2 = -\frac{R_{eq2}}{X_{eq2}}$.
- **Maximum Efficiency Condition:**
  - $P_{cu} = P_{core} \implies x = \sqrt{\frac{P_{core}}{P_{cu,FL}}}$.
- **Scott Connection (3-ph to 2-ph):**
  - Teaser transformer turn ratio: $N_{teaser} = \frac{\sqrt{3}}{2} N_{main} \approx 0.866 N_{main}$.
  - Teaser tapping on main transformer: $50\%$ midpoint.
- **Induction Motor Synchronous Speed & Slip:**
  - $N_s = \frac{120 f}{P}\text{ rpm}$, $s = \frac{N_s - N_r}{N_s}$.
  - Rotor frequency: $f_r = s f$.
  - Power Flow: $P_{gap} : P_{cu,rotor} : P_{mech} = 1 : s : (1 - s)$.
  - Maximum Torque Slip: $s_{max} = \frac{R_2}{X_2}$, $T_{max} \propto \frac{V^2}{2 X_2}$ (independent of $R_2$).
- **Alternator & Synchronous Motor:**
  - Synchronous Speed: $N_s = \frac{120 f}{P}$.
  - Short Circuit Ratio: $SCR = \frac{1}{X_{s,saturated} (pu)}$.
  - High SCR $\implies$ Larger air gap, larger size/cost, higher stability limit, lower voltage regulation.
  - Salient Pole Power Angle Equation (Two-Reaction Theory):
    $P = \frac{E V}{X_d} \sin\delta + \frac{V^2}{2} \left(\frac{1}{X_q} - \frac{1}{X_d}\right) \sin(2\delta)$.

---

## 3. Transmission & Distribution (TND & PRT)

### [Essential]
- **Inductance & Capacitance of 3-Phase Transposed Lines:**
  - $L = 2 \times 10^{-7} \ln\left(\frac{GMD}{GMR_L}\right)\text{ H/m/phase}$.
  - $C = \frac{2\pi \varepsilon_0}{\ln(GMD / GMR_C)}\text{ F/m/phase}$.
- **Surge Impedance & Surge Impedance Loading (SIL):**
  - $Z_c = \sqrt{\frac{L}{C}}$ (Lossless line: $\approx 400\ \Omega$ for overhead lines, $\approx 40\ \Omega$ for cables).
  - $SIL = \frac{V_L^2}{Z_c}\text{ MW}$.
- **String Efficiency:**
  - $\eta_{string} = \frac{V_{total}}{n \times V_{bottom\ disc}} \times 100\%$.
- **Cable Capacitance & Stress:**
  - $C = \frac{2\pi \varepsilon_0 \varepsilon_r}{\ln(R/r)}\text{ F/m}$.
  - Maximum stress at inner conductor surface: $g_{max} = \frac{V}{r \ln(R/r)}$.
  - Minimum stress at outer sheath: $g_{min} = \frac{V}{R \ln(R/r)}$.
  - Most economical core radius: $r = \frac{R}{e} \approx \frac{R}{2.718}$.
- **Symmetrical Components & Fault Currents:**
  - Sequence Transformation: $V_a = V_{a0} + V_{a1} + V_{a2}$.
  - Symmetrical 3-Phase Fault: $I_f = \frac{E_a}{Z_1}$.
  - Single Line-to-Ground (SLG) Fault: $I_f = 3 I_{a1} = \frac{3 E_a}{Z_1 + Z_2 + Z_0 + 3 Z_f}$.
  - Line-to-Line (LL) Fault: $I_f = \sqrt{3} I_{a1} = \frac{\sqrt{3} E_a}{Z_1 + Z_2 + Z_f}$.
  - Double Line-to-Ground (LLG) Fault: $I_{a1} = \frac{E_a}{Z_1 + \frac{Z_2 (Z_0 + 3 Z_f)}{Z_2 + Z_0 + 3 Z_f}}$.

---

## 4. Instrumentation & Earthing (INS & EAR)

### [Essential]
- **Kelvin's Double Bridge:**
  - $R = \frac{P}{Q} S + \frac{q r}{p + q + r} \left(\frac{P}{Q} - \frac{p}{q}\right)$.
  - When $\frac{P}{Q} = \frac{p}{q} \implies R = \frac{P}{Q} S$ (exact balance eliminating lead resistance).
- **Megger & Earth Testing:**
  - Earth electrode resistance measurement: Fall-of-Potential method.
  - Current electrode at distance $D$, Potential electrode at $61.8\% D$.
- **IS 3043 Permissible Earth Resistance:**
  - Generating Stations / Major Substation: $\le 0.5\ \Omega$.
  - Major Substation (33/11 kV): $\le 1.0\ \Omega$.
  - Small Substation / Airport Distribution: $\le 2.0\ \Omega$.
  - Domestic / Commercial Buildings: $\le 5.0\ \Omega$.

---

## 5. Airport MEP, HVAC & Fluid Mechanics (MEP, HVC, PUM)

### [Essential]
- **Pumps Affinity Laws:**
  - Flow rate: $\frac{Q_1}{Q_2} = \left(\frac{N_1}{N_2}\right) \left(\frac{D_1}{D_2}\right)$.
  - Head: $\frac{H_1}{H_2} = \left(\frac{N_1}{N_2}\right)^2 \left(\frac{D_1}{D_2}\right)^2$.
  - Power: $\frac{P_1}{P_2} = \left(\frac{N_1}{N_2}\right)^3 \left(\frac{D_1}{D_2}\right)^5$.
- **Specific Speed of Pumps:**
  - $N_s = \frac{N \sqrt{Q}}{H^{3/4}}$ (where $N$ in rpm, $Q$ in $\text{m}^3/\text{s}$, $H$ in m).
- **Net Positive Suction Head (NPSH):**
  - $NPSH_A = \frac{P_{atm}}{\rho g} \pm h_s - h_f - \frac{P_{vap}}{\rho g}$.
  - Cavitation prevention: $NPSH_A > NPSH_R$ by at least $0.5\text{–}1.0\text{ m}$.
- **Cooling Tower Performance:**
  - Range $= T_{hw,in} - T_{cw,out}$.
  - Approach $= T_{cw,out} - T_{wb}$ (Wet-bulb temperature).
  - Effectiveness $= \frac{\text{Range}}{\text{Range} + \text{Approach}} = \frac{T_{hw,in} - T_{cw,out}}{T_{hw,in} - T_{wb}}$.
- **Escalators (IS 4591):**
  - Standard angle of inclination $= 30^\circ$.
  - Permissible up to $35^\circ$ if rise $\le 6\text{ m}$ and rated speed $\le 0.5\text{ m/s}$.
  - Travelator (Moving Walkway) angle $= 0^\circ\text{ to }12^\circ$.
