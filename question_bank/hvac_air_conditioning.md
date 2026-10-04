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

---

### Q-HVC-006 `[ESE-ME-2018]` 🟡 Moderate
**Topic:** Psychrometrics — Sensible Heat Ratio (SHR)
**Question:** If the sensible heat load of an airport lounge is $70\text{ kW}$ and the latent heat load (due to human occupancy and infiltration) is $30\text{ kW}$, the Sensible Heat Factor (SHF / SHR) of the room is:
- (A) $0.70$
- (B) $0.43$
- (C) $0.30$
- (D) $1.00$
**Answer:** (A)
**Concept/Formula:**
- $\text{SHR} = \frac{\text{Sensible Heat (RSH)}}{\text{Total Heat (RSH + RLH)}} = \frac{70}{70 + 30} = \frac{70}{100} = 0.70$.
- Standard comfort spaces have $\text{SHR} \approx 0.70\text{–}0.75$; electronic server rooms have $\text{SHR} \ge 0.90$.

---

### Q-HVC-007 `[CPWD-MEP-2020]` 🟢 Easy
**Topic:** VRV / VRF Air Conditioning Systems
**Question:** In Variable Refrigerant Volume (VRV / VRF) systems widely used in administrative airport buildings, the variable capacity control of cooling is achieved by:
- (A) Cycling the compressor ON and OFF
- (B) Modulating the speed of the inverter-driven DC compressor to continuously adjust the mass flow rate of refrigerant to multiple indoor fan coil units based on exact individual room thermal demand
- (C) Changing the diameter of refrigerant pipes during operation
- (D) Mixing cold air with hot boiler flue gases
**Answer:** (B)
**Concept/Formula:** VRV systems use inverter scroll compressors and electronic expansion valves (EEVs) in each indoor unit to modulate refrigerant mass flow, offering exceptional part-load efficiency and independent zone temperature control.

---

### Q-HVC-008 `[ASHRAE-Standard / ISHRAE]` 🟡 Moderate
**Topic:** Chilled Water Pumping — Primary-Secondary System
**Question:** In large airport central chilled-water systems, a "Primary-Secondary" pumping arrangement with a common "decoupler pipe" (bypass pipe) is designed so that:
- (A) Secondary pumps run at constant speed while primary pumps vary
- (B) Primary pumps maintain a constant water flow rate through the chiller evaporators to prevent freezing/tripping, while secondary variable-speed pumps modulate flow through terminal AHUs using 2-way control valves
- (C) Chillers are protected from electrical power surges
- (D) Chilled water mixes with cooling tower water
**Answer:** (B)
**Concept/Formula:** Chillers require a constant (or slowly varying) minimum flow through the evaporator tubes to maintain heat transfer and avoid freezing. Variable-frequency drive (VFD) secondary pumps adjust distribution flow to the AHUs based on differential pressure ($\Delta P$), with excess/deficit flow circulating through the neutral decoupler pipe.

---

### Q-HVC-009 `[MES-MEP-2019]` 🟢 Easy
**Topic:** Chillers — Air-Cooled vs Water-Cooled Efficiency
**Question:** Comparing Water-Cooled chillers with Air-Cooled chillers of equal cooling capacity:
- (A) Air-cooled chillers have higher COP and consume less electrical power per TR
- (B) Water-cooled chillers operate at lower condensing temperatures (governed by wet-bulb temperature) and achieve significantly higher COP (lower kW/TR $\approx 0.55\text{–}0.65$ vs $1.1\text{–}1.3$ for air-cooled)
- (C) Water-cooled chillers do not require cooling towers or condenser water pumps
- (D) Air-cooled chillers require chemical water treatment
**Answer:** (B)
**Concept/Formula:** Water-cooled chillers reject heat to water whose temperature is limited by ambient wet-bulb (typically $27\text{–}28^\circ\text{C}$ in India), whereas air-cooled chillers reject heat directly to ambient dry-bulb (which can reach $42\text{–}45^\circ\text{C}$). The lower condensing head reduces compressor power by 30% to 50%.

---

### Q-HVC-010 `[CPWD-Boiler-2021]` 🟢 Easy
**Topic:** Heating Plants & Hot Water Generators — Safety Fittings
**Question:** According to Indian Boiler Regulations (IBR), every steam boiler or high-pressure hot water generator must be fitted with a minimum of:
- (A) One safety valve and no pressure gauge
- (B) At least two independent safety valves of approved design
- (C) A fusible plug only
- (D) An automatic water chiller
**Answer:** (B)
**Concept/Formula:** IBR legally mandates at least two independent safety valves capable of discharging all steam/pressure without allowing boiler pressure to rise more than 10% above maximum permissible working pressure (safety redundancy).

---

### Q-HVC-011 `[ISHRAE-Cooling-Tower]` 🟡 Moderate
**Topic:** Cooling Towers — Cycles of Concentration (CoC)
**Question:** In cooling tower water chemistry, "Cycles of Concentration" (CoC) represents:
- (A) The ratio of the dissolved solids (TDS) in the circulating cooling water to the dissolved solids in the fresh makeup water
- (B) The number of rotations of the cooling tower fan per hour
- (C) The ratio of air flow rate to water flow rate
- (D) The percentage of water lost to evaporation
**Answer:** (A)
**Concept/Formula:**
- $\text{CoC} = \frac{\text{TDS in Tower Water}}{\text{TDS in Makeup Water}}$.
- Higher CoC reduces makeup water consumption and blowdown volume, but if CoC is too high ($> 4\text{–}5$), scale formation and biological fouling (Legionella risk) accelerate.

---

### Q-HVC-012 `[AAI-Airport-MEP]` 🟢 Easy
**Topic:** Unitary AC Types — Cassette Air Conditioners
**Question:** Cassette air conditioning units are widely installed in airport retail kiosks, airline lounges, and security check counters because:
- (A) They do not require an outdoor condenser
- (B) The body is recessed completely above the false ceiling with a flush aesthetic grille that provides 4-way multi-directional uniform horizontal air distribution without ducting
- (C) They operate without electrical power
- (D) They generate high acoustic noise
**Answer:** (B)
**Concept/Formula:** Cassette ACs fit into standard ceiling grid tiles ($600 \times 600\text{ mm}$ or $900 \times 900\text{ mm}$), integrate a built-in drain lift pump, and discharge air in 4 directions along the ceiling (Coanda effect) for draft-free comfort.

---

### Q-HVC-013 `[BEE-ECBC-2020]` 🟢 Easy
**Topic:** HVAC Refrigerants — Environmental Protocols
**Question:** The Montreal Protocol and Kigali Amendment mandate the phase-down of Hydrofluorocarbons (HFCs) like R-410A and R-134a primarily because of their:
- (A) High Ozone Depletion Potential (ODP)
- (B) Zero Ozone Depletion Potential (ODP) but extremely High Global Warming Potential (GWP $> 1000\text{–}2000$)
- (C) Flammability in air
- (D) High toxicity to humans
**Answer:** (B)
**Concept/Formula:** HFCs (R-134a, R-410A) have $\text{ODP} = 0$, but their high global warming impact has led to transitions toward lower-GWP alternatives such as R-32 ($\text{GWP} \approx 675$) and Hydrofluoroolefins (HFOs like R-1234ze with $\text{GWP} < 1$).

---

### Q-HVC-014 `[ASHRAE-62.1 / Airport-IAQ]` 🟢 Easy
**Topic:** Indoor Air Quality (IAQ) — Fresh Air Ventilation
**Question:** According to ASHRAE 62.1 and NBC standards, fresh air ventilation in airport passenger terminal buildings is continuously introduced through AHUs to:
- (A) Increase cooling tower water flow
- (B) Dilute indoor contaminants, odors, and carbon dioxide ($CO_2$) generated by high passenger density, maintaining indoor $CO_2$ levels typically below $1000\text{ ppm}$
- (C) Eliminate the need for air filtration
- (D) Cool the elevator motors
**Answer:** (B)
**Concept/Formula:** Passenger terminals feature variable occupancy. Demand Controlled Ventilation (DCV) uses $CO_2$ sensors in return air ducts to modulate motorized fresh air dampers, ensuring sufficient fresh air CFM per person while avoiding excessive energy penalty of conditioning hot ambient air.

---

### Q-HVC-015 `[CPWD-MEP-2021]` 🟡 Moderate
**Topic:** AHU Cooling Coils — Bypass Factor
**Question:** If air enters an AHU cooling coil at $28^\circ\text{C}$ and leaves at $14^\circ\text{C}$, while the effective surface temperature of the coil (Apparatus Dew Point, ADP) is $10^\circ\text{C}$, the Coil Bypass Factor (BPF) is:
- (A) $0.222$
- (B) $0.500$
- (C) $0.778$
- (D) $0.357$
**Answer:** (A)
**Concept/Formula:**
- Bypass Factor $\text{BPF} = \frac{T_{out} - \text{ADP}}{T_{in} - \text{ADP}} = \frac{14 - 10}{28 - 10} = \frac{4}{18} \approx 0.222$ ($22.2\%$).
- Contact Factor $\eta_c = 1 - \text{BPF} = 1 - 0.222 = 0.778$ ($77.8\%$).
