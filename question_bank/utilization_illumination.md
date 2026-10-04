# AUTHENTIC QUESTION BANK: UTILIZATION, ILLUMINATION & SAFETY CODES
*Sources: AAI JE/Manager PYQs, SSC JE Electrical, State AE/JE, CEA Regulations*

---

### Q-UTL-001 `[AAI-JE-EE-2018]` 🟢 Easy
**Topic:** Laws of Illumination — Inverse Square Law
**Question:** A small lamp of $100\text{ candela}$ is placed at a height of $2\text{ m}$ directly above the center of a table. The illuminance (illumination) at the center of the table is:
- (A) $200\text{ lux}$
- (B) $50\text{ lux}$
- (C) $25\text{ lux}$
- (D) $12.5\text{ lux}$
**Answer:** (C)
**Concept/Formula:**
- Inverse Square Law: $E = \frac{I}{d^2} \cos \theta$.
- Directly underneath: $\theta = 0^\circ \implies \cos 0^\circ = 1$.
- $E = \frac{100}{2^2} = \frac{100}{4} = 25\text{ lux}$ (or $\text{lumens/m}^2$).

---

### Q-UTL-002 `[SSC-JE-2020]` 🟢 Easy
**Topic:** Illumination — Luminous Efficiency
**Question:** The unit of luminous flux is **Lumen**, and the unit of luminous efficacy (efficiency of a light source) is:
- (A) Lux
- (B) Candela
- (C) Lumen / Watt
- (D) Watt / Lumen
**Answer:** (C)
**Concept/Formula:** Luminous efficacy = $\frac{\text{Luminous Flux Output (Lumens)}}{\text{Electrical Power Input (Watts)}}$. Modern LED lamps achieve $100\text{–}150\text{ lm/W}$, whereas incandescent lamps offer only $10\text{–}15\text{ lm/W}$.

---

### Q-UTL-003 `[AAI-JE-EE-2018]` 🟡 Moderate
**Topic:** Earthing & Safety Codes (IS:3043 & Indian Electricity Rules)
**Question:** According to Indian Electricity (IE) Rules and standard safety practice, the permissible earth resistance for a large generating station or major substation should not exceed:
- (A) $0.5\ \Omega$
- (B) $1.0\ \Omega$
- (C) $2.0\ \Omega$
- (D) $5.0\ \Omega$
**Answer:** (A)
**Concept/Formula:**
- Major power stations / grid substations: $< 0.5\ \Omega$.
- Major substations: $< 1.0\ \Omega$.
- Small substations: $< 2.0\ \Omega$.
- Domestic / industrial installations: $< 5.0\ \Omega$.

---

### Q-UTL-004 `[SSC-JE-2021]` 🟡 Moderate
**Topic:** Illumination Design — Lumen Method
**Question:** A room measuring $10\text{ m} \times 8\text{ m}$ is to be illuminated to an average level of $200\text{ lux}$. The lamps used have a luminous flux of $2000\text{ lumens}$ each. Taking a utilization factor (coefficient of utilization) of $0.5$ and a maintenance factor of $0.8$, the number of lamps required is:
- (A) 10
- (B) 20
- (C) 25
- (D) 40
**Answer:** (B)
**Concept/Formula:**
- Total luminous flux required on working plane: $\Phi_{req} = \text{Area} \times E = (10 \times 8) \times 200 = 80 \times 200 = 16000\text{ lumens}$.
- Gross luminous flux to be emitted by lamps:
  $$\Phi_{gross} = \frac{\Phi_{req}}{\text{UF} \times \text{MF}} = \frac{16000}{0.5 \times 0.8} = \frac{16000}{0.4} = 40000\text{ lumens}$$
- Number of lamps $N = \frac{\Phi_{gross}}{\text{Flux per lamp}} = \frac{40000}{2000} = 20\text{ lamps}$.

---

### Q-UTL-005 `[State-AE-2020]` 🟢 Easy
**Topic:** Electric Heating — Dielectric Heating
**Question:** Dielectric heating is applied exclusively for the heating of:
- (A) Ferromagnetic metals like iron and steel
- (B) Non-ferrous conducting metals like copper and aluminum
- (C) Non-conducting insulating materials (dielectrics) such as wood, plastic, and ceramics
- (D) Molten metal baths
**Answer:** (C)
**Concept/Formula:**
- Dielectric heating produces heat uniformly throughout the volume of an insulating material placed between two electrodes energized by high-frequency AC ($10\text{–}50\text{ MHz}$).
- Power loss formula: $P = 2\pi f C V^2 \tan \delta\text{ Watts}$.
- Extensively used in wood gluing, plastic welding, food dehydration, and medical diathermy.

---

### Q-UTL-006 `[ESE-EE-2018]` 🟡 Moderate
**Topic:** Electric Traction — Mechanics of Train Movement
**Question:** In electric traction, a trapezoidal speed-time curve consists of the following distinct periods in chronological order:
- (A) Acceleration $\to$ Free running $\to$ Coasting $\to$ Braking
- (B) Acceleration $\to$ Coasting $\to$ Free running $\to$ Braking
- (C) Free running $\to$ Acceleration $\to$ Braking $\to$ Coasting
- (D) Acceleration $\to$ Free running $\to$ Braking (without coasting)
**Answer:** (A)
**Concept/Formula:**
- Trapezoidal curve (typical of main-line services with large inter-station distances):
  1. Acceleration (constant acceleration under current limit + speed curve running).
  2. Free running (constant maximum speed with power ON).
  3. Coasting (power cut OFF; train runs on stored kinetic energy, decelerating due to friction and air resistance).
  4. Braking (brakes applied to bring train to rest).
- For suburban / urban services, a quadrilateral speed-time curve (without free running) is used due to short station spacing.

---

### Q-UTL-007 `[AAI-JE-EE / SSC-JE]` 🟢 Easy
**Topic:** Illumination — Lambert's Cosine Law
**Question:** A light source of luminous intensity $I$ is mounted at height $h$ directly above a point $O$ on a horizontal surface. The illumination $E_P$ at a point $P$ situated at a distance $r$ from the source, where the light ray makes an angle $\theta$ with the vertical normal, is given by:
- (A) $E_P = \frac{I}{r^2} \cos \theta = \frac{I}{h^2} \cos^3 \theta$
- (B) $E_P = \frac{I}{h^2} \sin \theta$
- (C) $E_P = \frac{I}{r} \tan \theta$
- (D) $E_P = I \cdot r^2 \cos^2 \theta$
**Answer:** (A)
**Concept/Formula:**
- By Inverse Square Law: $E_P = \frac{I}{r^2} \cos \theta$.
- Since $r = \frac{h}{\cos \theta}$, substituting gives:
  $$E_P = \frac{I \cos \theta}{(h / \cos \theta)^2} = \frac{I}{h^2} \cos^3 \theta$$
- Illumination directly below the lamp ($\theta = 0$) is maximum: $E_0 = \frac{I}{h^2}$.

---

### Q-UTL-008 `[ESE-EE-2021]` 🟡 Moderate
**Topic:** Electric Heating — Induction Surface Hardening & Skin Depth
**Question:** In high-frequency induction heating used for surface case-hardening of steel shafts and gears, the depth of current penetration ($\delta$) into the workpiece is related to frequency ($f$), electrical resistivity ($\rho$), and magnetic permeability ($\mu$) by:
- (A) $\delta = \sqrt{\frac{\rho}{\pi f \mu}}$
- (B) $\delta = \sqrt{\frac{\pi f \mu}{\rho}}$
- (C) $\delta = \frac{1}{2\pi f \mu \rho}$
- (D) $\delta = 2\pi \sqrt{\rho f \mu}$
**Answer:** (A)
**Concept/Formula:**
- Skin effect forces high-frequency eddy currents to concentrate within a shallow surface layer of depth $\delta$.
- Because $\delta \propto \frac{1}{\sqrt{f}}$, higher frequencies (e.g. $10\text{ kHz to } 500\text{ kHz}$) produce extremely thin hardening depths ($0.5\text{ to } 2\text{ mm}$), leaving the core ductile and tough against shock.

---

### Q-UTL-009 `[SSC-JE-EE / State-AE]` 🟢 Easy
**Topic:** Electric Welding — Power Source Characteristics
**Question:** An electric arc welding power source (transformer or generator) must possess which type of volt-ampere output characteristic to ensure a stable electric arc and prevent destructive short-circuit currents during electrode touchdown?
- (A) Drooping (steeply falling) V-I characteristic
- (B) Rising V-I characteristic
- (C) Flat constant-voltage characteristic
- (D) Constant infinite power characteristic
**Answer:** (A)
**Concept/Formula:**
- Open-circuit voltage (OCV) must be high ($70\text{–}100\text{ V}$) to strike and ionize the arc easily.
- Once the arc is established, voltage drops to normal arc operating voltage ($20\text{–}40\text{ V}$).
- A drooping characteristic ensures that momentary electrode short-circuits to the workpiece produce only a limited, safe current increase, stabilizing the arc plasma.

---

### Q-UTL-010 `[ESE-EE-2019]` 🟡 Moderate
**Topic:** Electric Traction — Coefficient of Adhesion
**Question:** In electric locomotives, the maximum tractive effort that can be exerted without wheel slip is fundamentally limited by the "Adhesive Weight" ($W_a$) and "Coefficient of Adhesion" ($\mu_a$) according to:
- (A) $F_{\text{max}} = \mu_a \cdot W_a \cdot g$
- (B) $F_{\text{max}} = \frac{W_a}{\mu_a}$
- (C) $F_{\text{max}} = \mu_a^2 \cdot W_a$
- (D) $F_{\text{max}} = \frac{\mu_a \cdot g}{W_a}$
**Answer:** (A)
**Concept/Formula:**
- Tractive effort developed at the wheel rim cannot exceed frictional adhesion between steel wheel and steel rail: $F_{\text{adhesion}} = \mu_a W_a$ (in kg-wt or $\text{Newtons}$).
- For clean dry rails, $\mu_a \approx 0.25\text{ to } 0.30$.
- In wet or greasy rail conditions, $\mu_a$ drops to $0.15$, requiring sand ejectors to improve traction.

---

### Q-UTL-011 `[AAI-MEP / ICAO-Annex-14]` 🟢 Easy
**Topic:** Airport Apron & High Mast Lighting Design
**Question:** For airport apron floodlighting where aircraft parking, passenger boarding, and baggage loading occur, ICAO Annex 14 and NBC standards stipulate an average horizontal illuminance of at least:
- (A) $20\text{ lux}$ (with an average-to-minimum uniformity ratio not exceeding $4:1$)
- (B) $500\text{ lux}$
- (C) $1\text{ lux}$
- (D) $5\text{ lux}$
**Answer:** (A)
**Concept/Formula:**
- ICAO Annex 14 Volume I mandates:
  - Aircraft stand parking position: Minimum **$20\text{ lux}$** horizontal illuminance with uniformity ratio (average to minimum) $\le 4:1$.
  - Vertical illuminance at height $2\text{ m}$: Minimum **$20\text{ lux}$**.
  - Glare shielding is compulsory to prevent blinding approaching pilots and ATC tower controllers.

---

### Q-UTL-012 `[BEE-Lighting / CPWD-Specs]` 🟢 Easy
**Topic:** Lighting Quality — Color Rendering Index (CRI) and Correlated Color Temperature (CCT)
**Question:** In airport passenger terminal lounges, retail concourses, and check-in halls, what are the recommended Color Rendering Index ($R_a$) and Correlated Color Temperature (CCT) for modern LED luminaires?
- (A) CRI $\ge 80$, CCT $4000\text{ K}$ (Neutral White) or $3000\text{ K}$ (Warm White)
- (B) CRI $\le 40$, CCT $10,000\text{ K}$
- (C) CRI $= 0$, Monochromatic Sodium Yellow
- (D) CRI $\ge 99$, Ultraviolet
**Answer:** (A)
**Concept/Formula:**
- **CRI ($R_a$):** Measures light source fidelity compared to natural daylight (scale 0–100). Interior passenger commercial spaces mandate $R_a \ge 80$.
- **CCT (Kelvin):**
  - Warm white ($2700\text{–}3000\text{ K}$): Relaxed lounges.
  - Neutral / Cool white ($4000\text{–}5000\text{ K}$): High-activity terminal concourses, baggage claim, and check-in counters.
  - High mast apron floodlights: $5000\text{–}5700\text{ K}$ daylight white.

---

### Q-UTL-013 `[BMS-Lighting / ECBC-2017]` 🟡 Moderate
**Topic:** Energy Conservation — DALI Protocol vs Analog 1-10V Dimming
**Question:** In airport terminal smart lighting control systems, the **Digital Addressable Lighting Interface (DALI-2)** protocol is superior to traditional $1\text{–}10\text{ V}$ analog dimming primarily because:
- (A) DALI uses a two-wire digital bus where each luminaire driver has a unique digital address, enabling individual or group dimming, bidirectional status feedback (lamp failure, burn hours, energy consumption), and reconfiguration via software without changing field wiring
- (B) DALI requires high-voltage 3-phase wiring to each bulb
- (C) DALI cannot be connected to daylight sensors
- (D) DALI operates only on DC batteries
**Answer:** (A)
**Concept/Formula:**
- DALI (IEC 62386) is a bi-directional digital standard. Up to 64 addresses per DALI loop.
- It provides fault reporting (failed driver or failed LED board), individual power monitoring, dynamic daylight harvesting, and scheduled scene control integrated with the airport central IBMS.

---

### Q-UTL-014 `[ESE-EE-2017]` 🟡 Moderate
**Topic:** Electric Heating — Coreless Induction Furnaces
**Question:** In a high-frequency coreless induction melting furnace, the primary coil is constructed of:
- (A) Hollow water-cooled copper tubing
- (B) Solid aluminum strip
- (C) Nichrome wire wrapped around iron core
- (D) Carbon electrodes
**Answer:** (A)
**Concept/Formula:**
- Due to skin effect and very high circulating reactive currents at frequencies from $500\text{ Hz to } 10\text{ kHz}$, heavy $I^2 R$ heat is generated in the coil itself.
- Hollow electrolytic copper tubing allows continuous circulation of cooling demineralized water inside the conductor while carrying RF current on its outer perimeter.

---

### Q-UTL-015 `[ESE-EE-2022]` 🟡 Moderate
**Topic:** Electric Traction — Specific Energy Consumption (SEC)
**Question:** The Specific Energy Consumption (SEC) of an electric train, expressed in Watt-hours per ton-kilometer ($\text{Wh / ton-km}$), is minimized by:
- (A) Increasing the distance between consecutive station stops and increasing the coasting period
- (B) Increasing the maximum train speed with very short station runs
- (C) Applying heavy mechanical friction braking at full speed
- (D) Operating on steep uphill gradients continuously
**Answer:** (A)
**Concept/Formula:**
$$\text{SEC} = \frac{\text{Total Energy Consumed (Wh)}}{\text{Train Weight (tons)} \times \text{Distance Run (km)}}$$
- Longer run distances reduce the proportion of energy lost in acceleration and braking per km.
- Extended coasting utilizes the train's kinetic energy to overcome resistance without drawing power from the overhead catenary.
- Regenerative braking returns $20\text{–}30\%$ of braking kinetic energy back to the grid.

