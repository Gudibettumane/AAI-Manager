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
