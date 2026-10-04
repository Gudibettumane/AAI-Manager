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
