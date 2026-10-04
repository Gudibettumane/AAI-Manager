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
