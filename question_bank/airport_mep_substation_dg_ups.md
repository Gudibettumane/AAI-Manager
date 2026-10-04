# AUTHENTIC QUESTION BANK: AIRPORT MEP, SUBSTATION, DG SETS, UPS & SOLAR
*Sources: AAI Manager/JE (Electrical) PYQs, CPWD Electrical General Specifications, CEA Regulations, BEE*

---

### Q-SUB-001 `[AAI-JE/Manager-EE-2018]` 🟢 Easy
**Topic:** Substation — Auto Mains Failure (AMF) Panel Operation
**Question:** In an airport emergency power supply system, the primary function of an AMF (Auto Mains Failure) panel is:
- (A) To step down 11 kV to 415 V
- (B) To automatically detect grid power supply failure, initiate cranking of the DG set, transfer critical airport loads to the generator within a specified time (e.g. $< 15\text{ seconds}$), and switch back when mains power is restored
- (C) To control the reactive power of synchronous motors
- (D) To measure earth electrode resistance
**Answer:** (B)
**Concept/Formula:** AMF panels use voltage sensing relays (under-voltage, phase failure, frequency drift). Upon grid outage, it sends a start signal to the DG engine, waits until voltage and frequency stabilize, operates motorized circuit breakers / changeover contactors, and later shuts down the DG set after a cool-down period following mains restoration.

---

### Q-SUB-002 `[CPWD-EE-2021]` 🟡 Moderate
**Topic:** Power Factor Correction — APFC Panels
**Question:** An Automatic Power Factor Correction (APFC) panel uses a microprocessor-based controller to switch capacitor banks in stages based on:
- (A) Voltage fluctuations only
- (B) Measurement of active and reactive current (or phase angle between voltage and current) via a Current Transformer (CT) on the main incomer
- (C) Transformer oil temperature
- (D) Ambient air temperature
**Answer:** (B)
**Concept/Formula:** The APFC relay measures $\cos \phi$ and reactive current $I \sin \phi$ continuously from incoming CT and PT signals. When power factor drops below a preset setpoint (e.g., $0.98\text{ lag}$), it energizes contactors or thyristor switches in steps (e.g., $10, 25, 50\text{ kVAR}$) to maintain near-unity power factor and avoid DISCOM low-pf penalties.

---

### Q-SUB-003 `[AAI-EE-PYQ]` 🟢 Easy
**Topic:** Uninterruptible Power Supply (UPS) — Online vs Offline
**Question:** For mission-critical airport loads such as Air Traffic Control (ATC) consoles, Instrument Landing Systems (ILS), and Runway Visual Range (RVR) equipment, which UPS topology is mandatory?
- (A) Offline / Standby UPS
- (B) Line-Interactive UPS
- (C) Online Double Conversion (True Online) UPS
- (D) Ferro-resonant UPS
**Answer:** (C)
**Concept/Formula:** Online double conversion UPS converts incoming AC to DC (rectifier/charger) and continuously inverts DC back to regulated AC (inverter). It offers **ZERO transfer time ($0\text{ ms}$)** upon mains failure, total galvanic isolation, and complete protection against voltage sags, surges, harmonics, and frequency drifts.

---

### Q-SUB-004 `[CEA-Reg-2020 / ESE-EE]` 🟡 Moderate
**Topic:** HT Cables — Termination & Stress Cones
**Question:** In high-voltage XLPE cable terminations ($11\text{ kV} / 33\text{ kV}$), stress relief cones or stress control heat-shrink tubes are installed at the screen cutback point primarily to:
- (A) Prevent moisture ingress into the conductor
- (B) Relieve longitudinal electrical stress concentration and prevent dielectric puncture at the metallic sheath termination
- (C) Increase the ampacity of the cable
- (D) Provide mechanical support to the lugs
**Answer:** (B)
**Concept/Formula:** Abrupt termination of the grounded metallic screen creates an intense radial and longitudinal electric field gradient at the edge. A stress cone gradually increases insulation thickness or uses high-permittivity materials to smooth the equipotential lines, preventing electrical breakdown and tracking.

---

### Q-SUB-005 `[BEE-Energy-Auditor / AAI-EE]` 🟢 Easy
**Topic:** Energy Conservation Measures & BEE Star Ratings
**Question:** According to Bureau of Energy Efficiency (BEE) standards and ECBC (Energy Conservation Building Code), using Variable Frequency Drives (VFDs) on centrifugal chilled-water pumps and AHU supply fans yields dramatic energy savings because according to the Affinity Laws, pump/fan power consumption ($P$) varies with speed ($N$) as:
- (A) $P \propto N$
- (B) $P \propto N^2$
- (C) $P \propto N^3$ (Cubic power relationship)
- (D) $P \propto \sqrt{N}$
**Answer:** (C)
**Concept/Formula:**
- Affinity Laws:
  - Discharge $Q \propto N$
  - Head $H \propto N^2$
  - Power $P \propto N^3$
- Reducing fan or pump speed by just $20\%$ ($N = 0.8$) cuts power consumption by nearly $50\%$ ($P = (0.8)^3 = 0.512$ or $51.2\%$).

---

### Q-SUB-006 `[MNRE-Solar-2021]` 🟢 Easy
**Topic:** Solar PV Systems — Statutory Guidelines & Net Metering
**Question:** In grid-interactive rooftop solar power plants installed at airport terminal facilities, an "Anti-Islanding" protection feature in the solar grid-tie inverter is mandatory to:
- (A) Increase inverter maximum power point tracking (MPPT) efficiency
- (B) Automatically disconnect the solar inverter within milliseconds if the main utility grid fails, preventing power injection into dead utility lines and protecting maintenance personnel from electrocution
- (C) Store excess solar energy in underground cables
- (D) Convert DC directly into mechanical energy
**Answer:** (B)
**Concept/Formula:** IEEE 1547 and CEA regulations mandate anti-islanding. If the utility grid trips, the inverter must immediately trip (typically $< 2\text{ seconds}$) to prevent creating an uncontrolled, ungrounded electrical island that poses a lethal hazard to grid linemen.

---

### Q-SUB-007 `[ESE-EE-2020 / PGCIL]` 🟡 Moderate
**Topic:** Distribution Transformers — Loading & Maximum Efficiency
**Question:** A $1000\text{ kVA},\ 11\text{ kV} / 433\text{ V}$ dry-type airport indoor transformer has a core (iron) loss of $2\text{ kW}$ and a full-load copper loss of $8\text{ kW}$. At what fraction of full-load kVA does the transformer operate at its maximum efficiency?
- (A) $50\%$ load ($500\text{ kVA}$)
- (B) $70.7\%$ load ($707\text{ kVA}$)
- (C) $25\%$ load ($250\text{ kVA}$)
- (D) $100\%$ load ($1000\text{ kVA}$)
**Answer:** (A)
**Concept/Formula:**
- Condition for maximum efficiency:
  $$\text{Variable Loss} = \text{Constant Loss} \implies x^2 P_{cu,fl} = P_i$$
  $$x = \sqrt{\frac{P_i}{P_{cu,fl}}} = \sqrt{\frac{2\text{ kW}}{8\text{ kW}}} = \sqrt{\frac{1}{4}} = 0.50 \text{ (or } 50\% \text{ load)}$$
- Standard distribution transformers are deliberately designed to achieve peak efficiency at $50\%\text{ to } 75\%$ load because they run on partial loading throughout the 24-hour cycle.

---

### Q-SUB-008 `[CPWD-Specifications / AAI-MEP]` 🟡 Moderate
**Topic:** LT Power Distribution — Sandwich Busbar Trunking (BBT) vs Multi-run Cables
**Question:** In large airport terminal risers and main switchboard interconnections carrying heavy currents ($\ge 2000\text{ A}$), Sandwich-type Compact Busbar Trunking Systems (BBT) are preferred over multiple parallel XLPE power cables because:
- (A) BBT has lower inductive reactance, significantly lower voltage drop, higher short-circuit fault withstand capacity, and compact space footprint
- (B) BBT is made of PVC only
- (C) BBT requires no structural support
- (D) BBT eliminates the need for circuit breakers
**Answer:** (A)
**Concept/Formula:**
- Sandwich construction eliminates air gaps between phase conductors, resulting in extremely low inductive reactance ($X$).
- Reduced skin effect, superior heat dissipation through the aluminum enclosure, high fault withstand ($50\text{ kA}$ or $65\text{ kA}$ for $1\text{ sec}$), and elimination of uneven current sharing that plagues parallel cable runs.

---

### Q-SUB-009 `[AAI-Manager-EE / NTPC]` 🟡 Moderate
**Topic:** Standby Diesel Generators — Electronic Governor Operation Modes
**Question:** When a standby DG set supplies an isolated airport emergency essential bus during a complete grid blackout, the electronic engine governor operates in:
- (A) Droop mode ($4\%$ to $5\%$ droop)
- (B) Isochronous mode (Zero speed droop, constant 50 Hz frequency regardless of load)
- (C) Constant fuel injection mode
- (D) Power factor control mode
**Answer:** (B)
**Concept/Formula:**
- **Isochronous Mode ($0\%$ Droop):** Used when a single DG set (or master generator in a parallel islanded scheme) supplies an isolated load. The electronic governor adjusts fuel racks instantaneously to hold the frequency rock steady at exactly $50.0\text{ Hz}$ across $0\%$ to $100\%$ load variations.
- **Droop Mode ($3\text{–}5\%$ Droop):** Required when multiple generators operate in parallel or connect to a stiff utility grid to ensure stable, proportional active power sharing.

---

### Q-SUB-010 `[ISO-8528 / ISO-3046 / AAI-EE]` 🟢 Easy
**Topic:** Diesel Generating Sets — Environmental Derating
**Question:** Standard DG set prime power ratings are specified under standard reference conditions (typically $25^\circ\text{C}$ ambient and $100\text{ m}$ above sea level). In hot airport environments (e.g. ambient $45^\circ\text{C}$) or high-altitude airports (e.g. Leh at $3250\text{ m}$), the DG set capacity must be:
- (A) Increased by 20%
- (B) Derated according to ISO 3046 / IS 10000 curves due to reduced ambient air density and lower mass flow of oxygen entering the turbocharger cylinders
- (C) Maintained without change
- (D) Operated at double speed
**Answer:** (B)
**Concept/Formula:**
- Lower air density at high ambient temperatures and elevations reduces the mass of combustion air per cylinder charge, leading to incomplete combustion, high exhaust gas temperatures, and engine overheating.
- Standard derating rule-of-thumb: $\approx 1\%$ derate per $5.5^\circ\text{C}$ above $25^\circ\text{C}$, and $\approx 3.5\%$ derate per $300\text{ m}$ altitude above $100\text{ m}$.

---

### Q-SUB-011 `[IEEE-519 / CEA-Grid-Code]` 🟡 Moderate
**Topic:** Power Quality — Active Harmonic Filters (AHF) vs Detuned APFC
**Question:** Airport terminals have extensive non-linear loads (Variable Frequency Drives on chillers/fans, LED lighting drivers, UPS systems, and X-ray baggage scanners). To comply with IEEE 519 (Total Harmonic Distortion $THD_I < 8\%$ and $THD_V < 5\%$), an Active Harmonic Filter (AHF) functions by:
- (A) Inserting a large resistor in series with the load
- (B) Continuously monitoring the load harmonic currents and injecting an equal and opposite harmonic compensation current in real-time ($180^\circ$ anti-phase) via an IGBT inverter
- (C) Switching off the power supply
- (D) Stepping up the voltage by $10\%$
**Answer:** (B)
**Concept/Formula:**
- An AHF acts as a dynamic controlled current source connected in shunt. By injecting anti-phase harmonic currents ($I_h$), the source utility only supplies pure $50\text{ Hz}$ fundamental sinusoidal current.
- Unlike passive LC filters, AHFs cannot be overloaded and do not cause resonance with the supply transformer impedance.

---

### Q-SUB-012 `[AAI-MEP / CPWD-UPS]` 🟢 Easy
**Topic:** Uninterruptible Power Supply (UPS) — Battery Storage Technologies
**Question:** For high-reliability airport ATC and IT data centers, Valve Regulated Lead-Acid (VRLA) batteries are typically rated for an autonomy (backup time) at a discharge rate of:
- (A) $C_{10}$ or $C_{20}$ rate (10-hour or 20-hour rate)
- (B) $C_{1}$ or $C_{0.5}$ rate for 15 to 30 minutes emergency bridging time until the standby DG set synchronizes
- (C) 1 week continuous discharge
- (D) Infinite rate
**Answer:** (B)
**Concept/Formula:**
- In critical airport facilities equipped with Auto Mains Failure (AMF) DG sets that kick in within $15\text{ seconds}$, UPS batteries are engineered for **$15\text{ to } 30\text{ minutes}$** autonomy (bridging reserve).
- High-rate discharge performance ($C_1$ or $15\text{-minute}$ rate) is governed by **Peukert's Law** ($I^n t = C$), where high discharge currents reduce the usable ampere-hour capacity compared to the nominal $C_{10}$ rating.

---

### Q-SUB-013 `[IEEE-80 / IS-3043]` 🟡 Moderate
**Topic:** Substation Safety — Switchyard Surfacing & Touch/Step Potential
**Question:** According to IEEE 80 and IS:3043, why is a $100\text{ to }150\text{ mm}$ layer of washed crushed gravel/rock spread over the surface of an outdoor electrical substation switchyard?
- (A) To stop the growth of weed only
- (B) To provide a high-resistivity surface boundary layer ($\rho_s \approx 3000\text{ }\Omega\cdot\text{m}$ wet), thereby increasing body contact resistance and dramatically reducing touch and step voltages to safe, non-lethal limits during earth faults
- (C) To reflect sunlight away from switchgear
- (D) To reduce the transformer hum sound
**Answer:** (B)
**Concept/Formula:**
- The permissible touch voltage ($E_{\text{touch}}$) and step voltage ($E_{\text{step}}$) are proportional to:
  $$E_{\text{touch}} \approx (1000 + 1.5 C_s \rho_s) \frac{0.116}{\sqrt{t_s}}$$
  $$E_{\text{step}} \approx (1000 + 6 C_s \rho_s) \frac{0.116}{\sqrt{t_s}}$$
- High resistivity crushed rock ($\rho_s = 2000\text{ to } 5000\text{ }\Omega\cdot\text{m}$) adds thousands of ohms in series with the human foot contact resistance, saving human life during ground potential rise (GPR).

---

### Q-SUB-014 `[IEC-62305 / IS/IEC-62305]` 🟡 Moderate
**Topic:** Lightning Protection & Earthing — Surge Protection Devices (SPD)
**Question:** In accordance with IEC 62305, at the main LT incomer panel of an airport terminal receiving power from an overhead or exposed substation, the minimum required Surge Protection Device (SPD) is:
- (A) Type 3 SPD
- (B) Type 1 (Class I / Class B) SPD capable of withstanding direct lightning discharge current with a $10/350\text{ }\mu\text{s}$ impulse waveform
- (C) Type 2 SPD with $8/20\text{ }\mu\text{s}$ waveform only
- (D) A simple rewirable porcelain fuse
**Answer:** (B)
**Concept/Formula:**
- **Type 1 SPD (Class B):** Installed at main service entrance; rated for direct lightning impulse current ($10/350\text{ }\mu\text{s}$, high charge/energy content).
- **Type 2 SPD (Class C):** Installed at sub-distribution boards; rated for induced transient switching surges ($8/20\text{ }\mu\text{s}$).
- **Type 3 SPD (Class D):** Point-of-use surge protection installed right next to sensitive electronics/servers.

---

### Q-SUB-015 `[ICAO-Annex-14 / DGCA-CAR]` 🟢 Easy
**Topic:** Airport Ground Lighting & Infrastructure — Aviation Obstacle Lights (AOL)
**Question:** According to ICAO Annex 14 and DGCA civil aviation regulations, Aviation Obstacle Lights installed on tall airport structures (such as ATC towers, communication masts, and high-mast poles) must:
- (A) Operate on green flashing light during daytime only
- (B) Be fitted with Medium/High Intensity lights and powered through a dedicated uninterrupted power supply with automatic failover to battery/DG to ensure continuous illumination during night and poor visibility
- (C) Be turned off during foggy weather
- (D) Be wired with bare aluminum conductors
**Answer:** (B)
**Concept/Formula:**
- ICAO Annex 14 Chapter 6 mandates obstacle lighting for structures $> 45\text{ m}$ height (or within airfield obstacle limitation surfaces, OLS).
- Type A/B medium intensity lights ($2000\text{ cd}$ red flashing or steady night, $20,000\text{ cd}$ white flashing day/twilight).
- Uninterrupted operation backed by UPS and solar/battery hybrid sets is mandatory for air navigation safety.

