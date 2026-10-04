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
