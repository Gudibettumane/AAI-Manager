# AUTHENTIC QUESTION BANK: PUMPS, HYDRAULICS & FLUID MECHANICS
*Sources: ESE Prelims, SSC JE, State AE, PSU Water Management & MEP Papers*

---

### Q-PMP-001 `[ESE-ME/CE-2020]` 🟡 Moderate
**Topic:** Centrifugal Pumps — Specific Speed ($N_s$)
**Question:** The specific speed ($N_s$) of a centrifugal pump operating at rotational speed $N$ (rpm), delivering discharge $Q$ ($\text{m}^3\text{/s}$) against a total head $H$ (m) is given by:
- (A) $N_s = \frac{N \sqrt{Q}}{H^{3/4}}$
- (B) $N_s = \frac{N \sqrt{P}}{H^{5/4}}$
- (C) $N_s = \frac{N Q^{3/4}}{\sqrt{H}}$
- (D) $N_s = \frac{N \sqrt{H}}{Q^{3/4}}$
**Answer:** (A)
**Concept/Formula:**
- For **Pumps**: $N_s = \frac{N \sqrt{Q}}{H^{3/4}}$.
- For **Hydraulic Turbines**: $N_s = \frac{N \sqrt{P}}{H^{5/4}}$.
- **Exam Trap:** Don't confuse the pump formula (uses discharge $Q$ and exponent $3/4$) with the turbine formula (uses power $P$ and exponent $5/4$).

---

### Q-PMP-002 `[SSC-JE-2021]` 🟢 Easy
**Topic:** Centrifugal Pumps — Cavitation & NPSH
**Question:** In a centrifugal pumping system, cavitation occurs at the impeller inlet when:
- (A) The available Net Positive Suction Head is greater than the required NPSH ($\text{NPSHA} > \text{NPSHR}$)
- (B) The absolute pressure at the suction eye of the impeller falls below the saturated vapour pressure of the liquid ($P_{eye} \le P_v$)
- (C) The pump operates at very low discharge
- (D) The discharge pipe diameter is smaller than the suction pipe
**Answer:** (B)
**Concept/Formula:**
- If static pressure drops below vapour pressure, vapour bubbles form; when carried to higher-pressure zones in the impeller, they collapse violently, causing shockwaves, severe pitting erosion, noise, and vibration $\implies$ **Cavitation**.
- To prevent cavitation: Always ensure $\text{NPSHA} > \text{NPSHR} + \text{Safety Margin}$ (typically $0.5\text{–}1.0\text{ m}$).

---

### Q-PMP-003 `[ESE-CE/ME-2019]` 🟢 Easy
**Topic:** Fluid Mechanics — Bernoulli's Equation
**Question:** Bernoulli’s theorem for steady, incompressible, frictionless (inviscid) fluid flow along a streamline represents the conservation of:
- (A) Mass
- (B) Linear momentum
- (C) Mechanical Energy
- (D) Angular momentum
**Answer:** (C)
**Concept/Formula:**
- $\frac{P}{\rho g} + \frac{v^2}{2g} + z = \text{Constant}$ (Total Head = Pressure Head + Velocity Head + Datum/Potential Head).
- Derived by integrating Euler's equation of motion along a streamline.

---

### Q-PMP-004 `[GATE-CE/ME-2018]` 🟡 Moderate
**Topic:** Pipe Flow — Darcy-Weisbach Head Loss
**Question:** The frictional head loss ($h_f$) in a circular pipe of length $L$ and diameter $D$ carrying a fluid at average velocity $V$ is given by Darcy-Weisbach equation: $h_f = \frac{f L V^2}{2 g D}$. If the flow velocity is doubled while keeping pipe dimensions and friction factor constant, the head loss:
- (A) Doubles ($2\times$)
- (B) Quadruples ($4\times$)
- (C) Increases by eight times ($8\times$)
- (D) Remains unchanged
**Answer:** (B)
**Concept/Formula:**
- $h_f \propto V^2$.
- When velocity $V$ is doubled: $h_f' = (2V)^2 = 4 V^2 = 4 h_f$ (Quadruples).

---

### Q-PMP-005 `[State-AE-2020]` 🟢 Easy
**Topic:** Pipe Flow — Reynolds Number & Flow Regimes
**Question:** In pipe flow of a Newtonian fluid, the flow is classified as **laminar** if the Reynolds number ($\text{Re} = \frac{\rho V D}{\mu}$) is:
- (A) $\text{Re} < 2000$
- (B) $2000 < \text{Re} < 4000$
- (C) $\text{Re} > 4000$
- (D) $\text{Re} > 10000$
**Answer:** (A)
**Concept/Formula:**
- Laminar flow: $\text{Re} < 2000$.
- Transition flow: $2000 \le \text{Re} \le 4000$.
- Turbulent flow: $\text{Re} > 4000$.
- For laminar flow in circular pipes, Darcy friction factor is $f = \frac{64}{\text{Re}}$.

---

### Q-PMP-006 `[ESE-CE-2021]` 🟡 Moderate
**Topic:** Flow Measurement — Venturimeter
**Question:** A Venturimeter has a coefficient of discharge ($C_d$) typically in the range of:
- (A) $0.60 \text{ to } 0.65$
- (B) $0.70 \text{ to } 0.75$
- (C) $0.95 \text{ to } 0.98$
- (D) $1.05 \text{ to } 1.10$
**Answer:** (C)
**Concept/Formula:**
- Because of the gradual converging and diverging cones, flow separation and eddy formation are minimized in a venturimeter, resulting in very low energy loss $\implies C_d \approx 0.95\text{–}0.98$.
- In contrast, an orifice meter has an abrupt constriction and vena contracta, giving a much lower $C_d \approx 0.60\text{–}0.65$.

---

### Q-PMP-007 `[ESE-ME/CE-2018]` 🟢 Easy
**Topic:** Centrifugal Pumps — Series vs Parallel Operation
**Question:** Two identical centrifugal pumps each capable of delivering discharge $Q$ against a head $H$ are connected:
1. In **Series**: Resulting in total head $H_{series}$ and discharge $Q_{series}$
2. In **Parallel**: Resulting in total head $H_{parallel}$ and discharge $Q_{parallel}$
The characteristics of these connections are:
- (A) Series: $2H, Q$; Parallel: $H, 2Q$
- (B) Series: $H, 2Q$; Parallel: $2H, Q$
- (C) Series: $2H, 2Q$; Parallel: $H, Q$
- (D) Series: $\sqrt{2}H, Q$; Parallel: $H, \sqrt{2}Q$
**Answer:** (A)
**Concept/Formula:**
- In Series: Fluid passes through impellers sequentially $\implies$ Heads add up ($H_{total} \approx 2H$) at same flow rate $Q$.
- In Parallel: Both pumps discharge into a common header $\implies$ Flow rates add up ($Q_{total} \approx 2Q$) at same head $H$.

---

### Q-PMP-008 `[SSC-JE-2020]` 🟢 Easy
**Topic:** Centrifugal Pump Operation — Priming
**Question:** "Priming" of a centrifugal pump is necessary before starting because:
- (A) The pump will rotate in the reverse direction if air is present
- (B) If the pump casing and suction pipe contain air, the head developed in terms of liquid column is negligible ($\Delta P = \rho_{air} g H \approx 0$) due to the extremely low density of air, preventing suction of water
- (C) To lubricate the impeller bearings
- (D) To balance electrical voltage
**Answer:** (B)
**Concept/Formula:** Head developed by an impeller $H = \frac{u_2^2 - u_1^2}{2g}$ depends on impeller velocity, but pressure rise $\Delta P = \rho g H$. Since $\rho_{air} \approx \frac{1}{800}\text{th}$ of $\rho_{water}$, the suction vacuum created by an unprimed pump is nearly zero, failing to draw liquid up the suction pipe.

---

### Q-PMP-009 `[GATE-ME-2019]` 🟡 Moderate
**Topic:** Centrifugal Pump Impellers — Vane Curvature
**Question:** Centrifugal pumps for water supply almost exclusively use impellers with:
- (A) Backward-curved vanes (blade outlet angle $\beta_2 < 90^\circ$)
- (B) Forward-curved vanes ($\beta_2 > 90^\circ$)
- (C) Radial vanes ($\beta_2 = 90^\circ$)
- (D) Helical screw vanes
**Answer:** (A)
**Concept/Formula:**
- **Backward-curved vanes ($\beta_2 < 90^\circ$):** Produce a dropping head-discharge curve ($H-Q$) and a self-limiting power characteristic, which prevents motor overload if flow surges. They also offer higher hydraulic efficiency and lower kinetic energy at the impeller outlet.
- Forward-curved vanes are used in low-pressure blower fans (squirrel cage fans) where high outlet velocity is desired in a compact casing.

---

### Q-PMP-010 `[ESE-CE-2019]` 🟡 Moderate
**Topic:** Open Channel Flow — Hydraulic Jump
**Question:** A hydraulic jump in an open channel is an example of:
- (A) Steady, uniform flow
- (B) Rapidly Varied Flow (RVF) where flow transitions from supercritical ($Fr > 1$) to subcritical ($Fr < 1$) with significant kinetic energy dissipation
- (C) Gradually Varied Flow (GVF) with zero energy loss
- (D) Laminar creeping flow
**Answer:** (B)
**Concept/Formula:** A hydraulic jump occurs when high-velocity supercritical flow ($Fr_1 > 1$) abruptly decelerates into tranquil subcritical flow ($Fr_2 < 1$). It is characterized by severe surface turbulence, air entrainment, and major conversion of kinetic energy into heat.

---

### Q-PMP-011 `[GATE-CE-2017]` 🟢 Easy
**Topic:** Open Channel Flow — Froude Number
**Question:** In open channel flow, the Froude number ($Fr$) represents the ratio of:
- (A) Inertia force to Gravity force ($Fr = \frac{V}{\sqrt{g D_h}}$)
- (B) Inertia force to Viscous force
- (C) Inertia force to Surface tension
- (D) Pressure force to Inertia force
**Answer:** (A)
**Concept/Formula:**
- Critical flow: $Fr = 1$.
- Subcritical (tranquil) flow: $Fr < 1$ (gravity dominates; surface disturbances can travel upstream).
- Supercritical (rapid/shooting) flow: $Fr > 1$ (inertia dominates; disturbances only travel downstream).

---

### Q-PMP-012 `[ESE-CE/ME-2020]` 🟡 Moderate
**Topic:** Pipe Minor Losses — Sudden Expansion Loss
**Question:** The head loss due to a sudden enlargement of a pipe from cross-sectional area $A_1$ (velocity $V_1$) to area $A_2$ (velocity $V_2$) is given by:
- (A) $\frac{V_1^2 - V_2^2}{2g}$
- (B) $\frac{(V_1 - V_2)^2}{2g}$
- (C) $0.5 \frac{V_2^2}{2g}$
- (D) $\frac{V_1^2 + V_2^2}{2g}$
**Answer:** (B)
**Concept/Formula:** Borda-Carnot equation for sudden expansion: $h_L = \frac{(V_1 - V_2)^2}{2g}$. For sudden contraction: $h_c \approx 0.5 \frac{V_2^2}{2g}$.

---

### Q-PMP-013 `[State-AE-2021]` 🟢 Easy
**Topic:** Pipe Flow — Water Hammer & Surge Protection
**Question:** In long airport water pumping mains, "Water Hammer" caused by sudden pump stoppage or rapid valve closure is mitigated by installing:
- (A) Orifice plates
- (B) Surge tanks or Air Vessels (hydropneumatic expansion tanks) near the pump discharge
- (C) Small diameter pipes
- (D) Gate valves
**Answer:** (B)
**Concept/Formula:** Rapid closure converts kinetic energy of flowing water into an intense acoustic pressure surge ($P_{surge} = \rho c \Delta V$). Air vessels provide a compressible air cushion that absorbs the pressure shockwave, protecting pipes and check valves from catastrophic burst.

---

### Q-PMP-014 `[CPWD-MEP-2020]` 🟢 Easy
**Topic:** Flow Velocity Measurement — Pitot Tube
**Question:** A Pitot tube aligned with the fluid flow direction measures:
- (A) Static pressure only
- (B) Total (Stagnation) pressure ($P_{stag} = P_{static} + \frac{1}{2}\rho V^2$)
- (C) Dynamic pressure directly without static pressure
- (D) Mass flow rate directly
**Answer:** (B)
**Concept/Formula:** When fluid enters the impact hole, its velocity drops to zero ($V = 0$ at stagnation point). The stagnation pressure equals static pressure plus dynamic pressure ($P_0 = P + \frac{1}{2}\rho V^2$). When combined with static holes in a Pitot-Static tube, flow velocity is calculated as $V = \sqrt{\frac{2(P_0 - P)}{\rho}}$.

---

### Q-PMP-015 `[AAI-Airport-Water]` 🟢 Easy
**Topic:** Airport Drainage & Sewage Pumping — Non-Clog Submersible Pumps
**Question:** For sewage and storm-water drainage sumps in airport apron areas and terminal basements, the pump impellers are of **Non-Clog (Vortex / Single-Vane)** type because:
- (A) They create maximum possible pressure head
- (B) They provide large clear passages that allow solids, rags, and fibrous debris to pass through without clogging the pump
- (C) They operate at supersonic speeds
- (D) They do not use electric motors
**Answer:** (B)
**Concept/Formula:** Closed multi-vane impellers clog easily on sewage solids. Vortex (recessed) and single-channel non-clog impellers create a swirling vortex in the casing, passing solid spheres (typically $50\text{–}100\text{ mm}$ diameter) directly from suction to discharge without wedging between blades.
