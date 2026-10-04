# AUTHENTIC QUESTION BANK: FIRE FIGHTING, LIFTS, BMS, CCTV & SPECIAL AIRPORT MEP
*Sources: NBC 2016 (Part 4 & 8), IS:14665 (Lifts), IS:3043 (Earthing), NFPA / CPWD Specifications*

---

### Q-FIR-001 `[NBC-2016-Part4 / AAI-MEP]` 🟢 Easy
**Topic:** Automatic Sprinkler Systems — Glass Bulb Temperature Ratings
**Question:** In an automatic fire sprinkler system, a standard red-coloured liquid glass bulb is calibrated to shatter and activate water discharge at a nominal temperature of:
- (A) $57^\circ\text{C}$ (Orange)
- (B) $68^\circ\text{C}$ (Red)
- (C) $79^\circ\text{C}$ (Yellow)
- (D) $93^\circ\text{C}$ (Green)
**Answer:** (B)
**Concept/Formula:** Standard glass bulb color coding (NFPA 13 / NBC):
- Orange: $57^\circ\text{C}$
- **Red: $68^\circ\text{C}$** (Most common for standard room temperature ceiling applications)
- Yellow: $79^\circ\text{C}$
- Green: $93^\circ\text{C}$
- Blue: $141^\circ\text{C}$
- Mauve/Purple: $182^\circ\text{C}$
- Black: $227\text{–}260^\circ\text{C}$.

---

### Q-FIR-002 `[NBC-2016 / CPWD-MEP]` 🟢 Easy
**Topic:** Electrical Room Fire Protection — Clean Agent Suppression
**Question:** In electrical HT/LT panel rooms, server rooms, and ATC radar consoles, why is water-based sprinkler protection avoided and replaced by Clean Agent Gas Suppression (such as FM-200 / Novec 1230)?
- (A) Water is too expensive to pipe into upper floors
- (B) Clean agent gases are electrically non-conducting, leave zero residue, cause zero thermal shock or short circuits to energized electrical equipment, and extinguish fire within 10 seconds
- (C) Clean agents freeze the fire
- (D) Clean agents remove oxygen completely to 0%
**Answer:** (B)
**Concept/Formula:**
- Clean agents extinguish fires primarily via physical heat absorption and chemical chain reaction interruption at low design concentrations (e.g., 5–9%), leaving safe oxygen levels for human escape (NOAEL safe).
- Zero collateral water damage to high-voltage switchgear and sensitive electronics.

---

### Q-LFT-001 `[IS-14665 / CPWD-Lifts]` 🟢 Easy
**Topic:** Elevators — Automatic Rescue Device (ARD)
**Question:** An Automatic Rescue Device (ARD) in an airport passenger elevator is an auxiliary battery-operated safety system designed to:
- (A) Increase lift speed during rush hours
- (B) Detect power failure, immediately bring the stalled elevator car to the nearest landing floor, open the doors automatically, and release trapped passengers
- (C) Operate the elevator continuously for 24 hours during blackouts
- (D) Act as an emergency brake if ropes snap
**Answer:** (B)
**Concept/Formula:** ARD utilizes a dedicated battery pack and small solid-state inverter. When grid and DG power fail, it releases the mechanical brake, drives the motor in the direction of lightest load (gravity assistance) to the closest floor, opens the door, and parks the lift safely.

---

### Q-LFT-002 `[IS-4591 / Airport-Escalators]` 🟢 Easy
**Topic:** Escalators & Travelators — Angle of Inclination
**Question:** According to IS and international airport standards, the permissible angle of inclination of an escalator with a vertical rise not exceeding $6\text{ m}$ is:
- (A) $30^\circ \text{ or } 35^\circ$
- (B) $45^\circ$
- (C) $60^\circ$
- (D) $15^\circ$
**Answer:** (A)
**Concept/Formula:**
- Maximum angle of inclination for escalators is **$30^\circ$** (standard for heavy duty airport passenger flow). For rises $\le 6\text{ m}$ and rated speed $\le 0.5\text{ m/s}$, an inclination of **$35^\circ$** is permissible.
- For moving walks (travelators): Inclination is typically $0^\circ \text{ to } 12^\circ$.

---

### Q-BMS-001 `[BMS-Standard / AAI-IBMS]` 🟢 Easy
**Topic:** Building Management System (BMS) — Open Communication Protocols
**Question:** In modern airport Intelligent Building Management Systems (IBMS), which open, vendor-independent standard communication protocol is universally used for HVAC and lighting automation?
- (A) BACnet (Building Automation and Control networks) & Modbus
- (B) Bluetooth 2.0
- (C) I2C bus
- (D) MIDI protocol
**Answer:** (A)
**Concept/Formula:**
- **BACnet (ANSI/ASHRAE 135 / ISO 16484-5):** Specifically designed for building automation, allowing chillers, AHUs, VAVs, and lighting controllers from different manufacturers to interoperate seamlessly.
- **Modbus (RTU / TCP):** Widely used for energy meters, VFD drives, and UPS power integration into the BMS.

---

### Q-SEC-001 `[Airport-Security / CPWD-EL]` 🟢 Easy
**Topic:** Public Address (PA) System — 100V Line Distribution
**Question:** In airport terminal Public Address (PA) and evacuation systems, loudspeakers are connected using a **$100\text{ V}$ Constant-Voltage Line** system primarily because:
- (A) Loudspeakers operate directly on 100V DC
- (B) High-voltage step-up allows audio signals to be transmitted over very long cable distances throughout the terminal with negligible $I^2 R$ cable power loss, and allows multiple speakers of different wattage to be connected in parallel using local step-down line matching transformers
- (C) It eliminates the need for an audio amplifier
- (D) It prevents echoes in large terminal halls
**Answer:** (B)
**Concept/Formula:** Analogous to electrical power transmission lines: By stepping up audio voltage to $70\text{ V}$ or $100\text{ V}$, line current is drastically reduced $\implies$ minimal cable resistance loss over terminal distances of 500–1000 meters. Each speaker has a local tapped transformer (e.g., 3W, 6W, 10W) in parallel across the two-wire line.

---

### Q-FIR-003 `[IS-3844 / NBC-2016-Part4]` 🟡 Moderate
**Topic:** Fire Hydrant & Sprinkler System — Pump Automation & Pressure Sequencing
**Question:** In an automated fire-fighting pumping station, what is the role and operating sequence of the small-capacity **Jockey Pump** relative to the Main Electric Fire Pump?
- (A) The Jockey pump runs continuously to fight large fires, while the main pump never starts
- (B) The Jockey pump automatically starts and stops on pressure switch settings to compensate for minor pipeline leakages and maintain system static header pressure (e.g. $7\text{ kg/cm}^2$); if a hydrant/sprinkler opens causing pressure to drop sharply below a lower threshold (e.g. $5.5\text{ kg/cm}^2$), the Main Electric Pump starts automatically and cannot be stopped automatically (manual shutdown mandatory)
- (C) The Jockey pump adds chemicals to fire water
- (D) The Jockey pump operates only when the main pump fails to turn off
**Answer:** (B)
**Concept/Formula:**
- Fire codes mandate that Main Fire Pumps (Electric & Standby Diesel) must **NEVER auto-stop** on pressure recovery; they must be manually turned off by fire officers after confirming fire extinguishment.
- The Jockey pump has automatic start AND stop setpoints to handle minor thermal expansion or small weeping leaks without cycling the massive main pumps.

---

### Q-FIR-004 `[NFPA-72 / NBC-2016]` 🟡 Moderate
**Topic:** Fire Detection — Very Early Warning Aspirating Smoke Detection (VESDA)
**Question:** In critical mission facilities such as ATC Radar equipment rooms and Server Datacenters, Aspirating Smoke Detection Systems (ASD / VESDA) are installed because:
- (A) Standard optical detectors are too cheap
- (B) ASD continuously draws air samples through an active piped sampling network into a laser detection chamber, detecting microscopic sub-micron particles of combustion at the incipient (smoldering) stage hours before visible smoke or open flame develops
- (C) ASD releases halon gas immediately without any delay
- (D) ASD senses room temperature only
**Answer:** (B)
**Concept/Formula:**
- High airflow velocity in air-conditioned server rooms dilutes smoke, preventing passive spot smoke detectors from triggering.
- VESDA actively samples air and detects obscuration levels as low as $0.005\%\text{ to }0.02\%\text{ obs/m}$, triggering multi-stage progressive alarms (Alert, Action, Fire 1, Fire 2) before equipment is damaged.

---

### Q-FIR-005 `[BS-6387 / IS-Standards]` 🟢 Easy
**Topic:** Fire Safety — Circuit Integrity Fire-Rated Cables (CWZ Rating)
**Question:** In emergency life-safety systems (fire dampers, smoke extraction fans, emergency evacuation PA), cables with BS 6387 Category CWZ rating are specified because they guarantee:
- (A) Operation at zero Kelvin
- (B) Circuit integrity during fire up to $950^\circ\text{C}$ for 3 hours (Cat C), resistance to fire with water spray (Cat W), and resistance to fire with mechanical shock/impact (Cat Z)
- (C) Immunity to internet viruses
- (D) High speed data transfer only
**Answer:** (B)
**Concept/Formula:**
- Standard PVC/XLPE cables short-circuit within minutes of fire exposure.
- Mineral Insulated (MICC) or Silicon/Mica taped fire survival cables maintain circuit continuity during extreme building fires, ensuring pressurization fans and evacuation alarms remain powered during occupant evacuation.

---

### Q-LFT-003 `[IS-14665 / CPWD-Lifts]` 🟡 Moderate
**Topic:** Traction Elevators — Counterweight Sizing & Balance Ratio
**Question:** In a high-speed passenger traction elevator installed in an airport terminal, the counterweight mass ($M_{cw}$) is conventionally sized to balance:
- (A) The weight of the empty lift car only ($M_{\text{car}}$)
- (B) The weight of the empty car plus $40\%$ to $50\%$ of the rated payload capacity ($M_{\text{payload}}$)
- (C) The maximum gross weight of car plus $100\%$ full load
- (D) Exactly zero kg
**Answer:** (B)
**Concept/Formula:**
$$M_{cw} = M_{\text{car}} + K \cdot M_{\text{payload}}, \quad \text{where } K = 0.40 \text{ to } 0.50 \text{ (Balance Factor)}$$
- Balancing at average load ($\approx 45\%$) minimizes the net out-of-balance load seen by the hoist motor throughout the operating day, reducing motor size, mechanical stress, and electrical energy consumption.

---

### Q-LFT-004 `[IS-14665-Part3]` 🟢 Easy
**Topic:** Elevator Safety Devices — Overspeed Governor & Safety Gear
**Question:** According to IS:14665 elevator safety regulations, if an elevator car exceeds its rated downward speed by more than $15\%$ to $40\%$ (e.g. in event of rope slip or brake failure), which mechanical safety device must engage to physically clamp onto the steel guide rails and stop the car?
- (A) The buffer springs at the bottom of the pit directly
- (B) The Centrifugal Overspeed Governor which trips the electrical safety circuit and then mechanically actuates the car's Progressive Safety Gear jaws against the guide rails
- (C) The door interlock motor
- (D) The landing push button
**Answer:** (B)
**Concept/Formula:**
- For speeds $\le 1.0\text{ m/s}$: Instantaneous safety gear may be used.
- For high-speed airport passenger lifts ($> 1.0\text{ m/s}$): **Progressive (gradual wedge) Safety Gear** is mandatory to ensure controlled deceleration ($\le 1.0\text{ g}$) without causing neck/spine injuries to passengers.

---

### Q-BMS-002 `[BMS-Fundamentals / CPWD-HVAC]` 🟡 Moderate
**Topic:** Building Automation — Direct Digital Controller (DDC) I/O Signal Types
**Question:** In an airport BMS DDC panel controlling an Air Handling Unit (AHU), an analog modulating chilled water valve actuator and an air temperature sensor are typically interfaced to the DDC using which signal standards?
- (A) Modulating valve: $0\text{–}10\text{ V DC}$ or $4\text{–}20\text{ mA}$ Analog Output (AO); Temperature sensor: PT1000 RTD or NTC thermistor Analog Input (AI)
- (B) 230V AC digital pulse for temperature
- (C) Hydraulic oil pressure line
- (D) RS-232 serial cable directly to each resistor
**Answer:** (A)
**Concept/Formula:**
- **Analog Input (AI):** Continuous physical measurement (PT100/1000 RTD for temperature, 0–10V or 4–20mA for humidity/pressure).
- **Analog Output (AO):** Continuous command signal ($0\text{–}10\text{ V DC}$ or $4\text{–}20\text{ mA}$ to position chilled water control valves or adjust VFD fan speed).
- **Digital Input (DI):** Volt-free dry contact for status (e.g., fan run status, filter dirty DP switch).
- **Digital Output (DO):** Relay contact command ($24\text{ V AC/DC}$ to start/stop pumps and fans).

---

### Q-BMS-003 `[NBC-2016-Part8 / BMS-HVAC]` 🟢 Easy
**Topic:** Life Safety HVAC Integration — Fire Smoke Damper Interlocking
**Question:** During a confirmed fire alarm in an airport terminal zone, the Building Management System (BMS) and Fire Alarm Control Panel (FACP) must immediately cause the motorized Fire & Smoke Dampers (FSD) in the supply air ducts of that zone to:
- (A) Open fully to blow air into the fire
- (B) Snap closed via spring return actuator (energized to open, spring to close on power cut/alarm signal) and trip the supply AHU fan to prevent smoke migration to adjacent unaffected passenger zones
- (C) Double the fan speed
- (D) Switch to cooling mode
**Answer:** (B)
**Concept/Formula:**
- Smoke inhalation causes $> 75\%$ of fire casualties.
- Fire dampers are spring-loaded fail-safe (normally energized). Upon fire signal or thermal fuse link melt ($72^\circ\text{C}$), power is cut $\implies$ mechanical spring closes damper blades tightly $< 15\text{ seconds}$.
- Simultaneously, AHU fans interlock to shut off, while dedicated Smoke Spill exhaust fans start to exhaust toxic fumes outside.

---

### Q-SEC-002 `[Airport-CCTV-Design / CPWD]` 🟡 Moderate
**Topic:** CCTV Surveillance — IP Camera Bandwidth & Storage Estimation
**Question:** An airport security network has 100 Full HD ($1080\text{p}$, $1920\times 1080$) IP cameras streaming at 25 frames per second using H.265 video compression with an average constant bitrate of $2\text{ Mbps}$ per camera. What is the approximate total storage required for continuous 24/7 recording for 30 days retention?
- (A) $\approx 2.16\text{ TB}$
- (B) $\approx 64.8\text{ TB}$
- (C) $\approx 648\text{ TB}$
- (D) $\approx 10\text{ GB}$
**Answer:** (B)
**Concept/Formula:**
- Total bandwidth = $100 \times 2\text{ Mbps} = 200\text{ Mbps} = \frac{200}{8}\text{ MB/s} = 25\text{ MB/s}$.
- Storage per day:
  $$25\text{ MB/s} \times 3600\text{ s/hr} \times 24\text{ hr/day} = 25 \times 86400\text{ MB} = 2,160,000\text{ MB} = 2.16\text{ TB/day}$$
- For 30 days:
  $$\text{Total Storage} = 2.16\text{ TB/day} \times 30\text{ days} = 64.8\text{ TB}$$
- Note: H.265 achieves $\approx 50\%$ bandwidth and storage reduction compared to older H.264 codecs.

---

### Q-SEC-003 `[NFPA-72 / NBC-2016-Part4]` 🟡 Moderate
**Topic:** Fire Alarm Systems — Class A (Style 7) vs Class B (Style 4) Signaling Line Circuits
**Question:** In high-reliability airport terminal Addressable Fire Detection Systems, why is Class A (Loop) wiring with Fault Isolator Modules specified instead of Class B (Radial) wiring?
- (A) Class A wiring requires only a single uninsulated wire
- (B) In Class A, the signaling circuit originates and returns to the control panel forming a closed ring; if an open-circuit break or single wire cut occurs, the panel drives the loop from both directions, maintaining full communication with 100% of detectors and sounders
- (C) Class A circuits do not need power
- (D) Class B circuits cannot detect smoke
**Answer:** (B)
**Concept/Formula:**
- **Class B (Radial/Spur):** A single wire cut renders all downstream detectors dead.
- **Class A (Loop):** Both ends terminate at the FACP. Upon a line break, the controller senses the discontinuity and immediately transmits/receives from both ends, achieving zero loss of protection.
- Fault Isolator Modules installed every 20–25 devices isolate short-circuited segments automatically.

