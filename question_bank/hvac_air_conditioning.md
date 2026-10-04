# AUTHENTIC QUESTION BANK: HVAC & AIR-CONDITIONING SYSTEMS
*Sources: CPWD / MES AE (Electrical & Mechanical), ESE Prelims, Airport Authority MEP PYQs, ISHRAE*

---

### Q-HVC-001 `[CPWD-AE-2020]` 🟢 Easy
**Topic:** Refrigeration Units — Ton of Refrigeration (TR)
**Question:** One Ton of Refrigeration (1 TR) is equivalent to the rate of heat removal required to freeze 1 short ton of water at $0^\circ\text{C}$ into ice at $0^\circ\text{C}$ in 24 hours. In SI units, 1 TR is equal to:
- (A) $3.517\text{ kW}$ ($211\text{ kJ/min}$)
- (B) $4.184\text{ kW}$ ($250\text{ kJ/min}$)
- (C) $2.500\text{ kW}$ ($150\text{ kJ/min}$)
- (D) $5.000\text{ kW}$ ($300\text{ kJ/min}$)
**Answer:** (A)
**Concept/Formula:**
- $1\text{ TR} = 12,000\text{ BTU/hr} \approx 3.517\text{ kW} = 3024\text{ kcal/hr} \approx 211\text{ kJ/min} = 50\text{ kcal/min}$.
- Essential conversion constant for all HVAC chilling calculations in airports.

---

### Q-HVC-002 `[MES-AE-2021]` 🟡 Moderate
**Topic:** Cooling Towers — Range and Approach
**Question:** In an HVAC cooling tower, if the cooling tower receives warm water from the condenser at $37^\circ\text{C}$ and cools it down to $32^\circ\text{C}$ when the ambient air wet-bulb temperature is $27^\circ\text{C}$, the "Cooling Range" and "Approach" of the cooling tower are respectively:
- (A) Range = $5^\circ\text{C}$; Approach = $5^\circ\text{C}$
- (B) Range = $10^\circ\text{C}$; Approach = $5^\circ\text{C}$
- (C) Range = $5^\circ\text{C}$; Approach = $10^\circ\text{C}$
- (D) Range = $32^\circ\text{C}$; Approach = $27^\circ\text{C}$
**Answer:** (A)
**Concept/Formula:**
- **Range:** Temperature difference between entering hot water and leaving cold water:
  $$\text{Range} = T_{in} - T_{out} = 37^\circ\text{C} - 32^\circ\text{C} = 5^\circ\text{C}$$
- **Approach:** Temperature difference between leaving cold water and ambient Wet-Bulb (WB) temperature:
  $$\text{Approach} = T_{out} - T_{wb} = 32^\circ\text{C} - 27^\circ\text{C} = 5^\circ\text{C}$$
- Note: Approach is the ultimate indicator of cooling tower sizing and performance; a lower approach indicates a larger, more efficient cooling tower.

---

### Q-HVC-003 `[AAI-MEP-PYQ / State-AE]` 🟢 Easy
**Topic:** Precision Air Conditioning (PAC)
**Question:** In airport Air Traffic Control (ATC) server rooms and Radar equipment rooms, Precision Air Conditioning (PAC) units are installed instead of comfort air conditioners because PAC units:
- (A) Focus mainly on latent heat removal without humidity control
- (B) Maintain tight temperature ($\pm 1^\circ\text{C}$) and relative humidity ($50 \pm 5\%$) tolerances, have high Sensible Heat Ratio (SHR $\approx 0.9\text{–}0.95$), and operate 24x7x365 continuously
- (C) Are cheaper to install than split AC units
- (D) Use water as the circulating refrigerant inside the room
**Answer:** (B)
**Concept/Formula:**
- Server and telecommunications rooms generate almost 100% sensible heat (electronic heat dissipation without human sweat/moisture).
- Standard comfort AC has an SHR of 0.65–0.70 (wasting energy over-dehumidifying). PAC units operate with **SHR > 0.90**, high CFM air recirculation, HEPA filtration, and precision microprocessor humidity/temperature control.

---

### Q-HVC-004 `[ESE-ME/EE-2019]` 🟡 Moderate
**Topic:** Central Chiller Types — Screw vs Centrifugal Chillers
**Question:** For very large commercial facilities like airport passenger terminal buildings requiring cooling capacities exceeding $500\text{ to } 1000\text{ TR}$ per machine, which chiller type offers the highest operating efficiency at full load?
- (A) Reciprocating compressor chiller
- (B) Centrifugal compressor chiller
- (C) Air-cooled scroll chiller
- (D) Absorption chiller using low pressure steam
**Answer:** (B)
**Concept/Formula:**
- **Centrifugal Chillers:** Highest full-load efficiency (lowest kW/TR, typically 0.50–0.55 kW/TR for water-cooled units) in large sizes ($> 400\text{–}500\text{ TR}$ up to several thousand TR).
- **Screw Chillers:** Dominant in the $100\text{–}500\text{ TR}$ range, with excellent part-load efficiency via slide-valve / VFD modulation.
- **Scroll Chillers:** Used in smaller systems ($10\text{–}100\text{ TR}$).

---

### Q-HVC-005 `[CPWD-AE-2021]` 🟢 Easy
**Topic:** Air Handling Unit (AHU) Components
**Question:** In a standard central chilled-water Air Handling Unit (AHU), the purpose of the VAV (Variable Air Volume) box is:
- (A) To vary the chilled water temperature supplied to the cooling coil
- (B) To modulate the volume of conditioned air delivered to a specific airport terminal zone based on localized thermostat demand
- (C) To control the speed of the cooling tower fan
- (D) To heat water in the boiler
**Answer:** (B)
**Concept/Formula:**
- In a VAV system, the AHU supply fan delivers air at a constant temperature (e.g., $13^\circ\text{C}$), and motorized dampers in individual **VAV terminal boxes** open or close to modulate air flow (CFM) to match fluctuating room thermal loads, maximizing energy efficiency.
