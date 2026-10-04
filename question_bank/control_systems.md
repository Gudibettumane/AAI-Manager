# AUTHENTIC QUESTION BANK: CONTROL SYSTEMS
*Sources: AAI JE/Manager PYQs, ESE Prelims EE, GATE EE, ISRO EE*

---

### Q-CTL-001 `[GATE-EE-2019]` 🟡 Moderate
**Topic:** Second-Order Time-Domain Specifications
**Question:** A standard second-order unity feedback system has an open-loop transfer function $G(s) = \frac{25}{s(s + 6)}$. The peak overshoot ($M_p$) to a unit step input is approximately:
- (A) $9.5\%$
- (B) $16.3\%$
- (C) $5.0\%$
- (D) $25.0\%$
**Answer:** (A)
**Concept/Formula:**
- Characteristic equation: $1 + G(s) = 0 \implies s^2 + 6s + 25 = 0$.
- Standard form: $s^2 + 2\zeta\omega_n s + \omega_n^2 = 0 \implies \omega_n = 5\text{ rad/s},\ 2\zeta(5) = 6 \implies \zeta = 0.6$.
- Peak overshoot $M_p = e^{-\frac{\pi \zeta}{\sqrt{1 - \zeta^2}}} \times 100\% = e^{-\frac{\pi \times 0.6}{\sqrt{1 - 0.36}}} \times 100\% = e^{-\frac{1.885}{0.8}} \times 100\% = e^{-2.356} \times 100\% \approx 9.5\%$.
- Shortcut values to memorize for exam:
  - $\zeta = 0.5 \implies M_p \approx 16.3\%$
  - $\zeta = 0.6 \implies M_p \approx 9.5\%$
  - $\zeta = 0.7 \implies M_p \approx 4.6\%$

---

### Q-CTL-002 `[ESE-EE-2020]` 🟢 Easy
**Topic:** Routh-Hurwitz Stability Criterion
**Question:** The characteristic equation of a third-order system is $s^3 + 3s^2 + 3s + 1 + K = 0$. The value of $K$ for which the system is marginally stable (oscillates with sustained frequency) is:
- (A) $K = 8$
- (B) $K = 9$
- (C) $K = 1$
- (D) $K = 0$
**Answer:** (A)
**Concept/Formula:**
- For a 3rd-order system $a_0 s^3 + a_1 s^2 + a_2 s + a_3 = 0$:
- Marginal stability occurs when the inner product equals the outer product: $a_1 a_2 = a_0 a_3$.
- Here: $3 \times 3 = 1 \times (1 + K) \implies 9 = 1 + K \implies K = 8$.

---

### Q-CTL-003 `[GATE-EE-2017]` 🟡 Moderate
**Topic:** Steady-State Errors & System Type
**Question:** A unity feedback system with open-loop transfer function $G(s) = \frac{100}{s(s + 2)(s + 5)}$ is subjected to a ramp input $r(t) = 4t$. The steady-state error $e_{ss}$ is:
- (A) $0$
- (B) $0.4$
- (C) $0.2$
- (D) $\infty$
**Answer:** (B)
**Concept/Formula:**
- Velocity error constant $K_v = \lim_{s \to 0} s G(s) = \lim_{s \to 0} s \frac{100}{s(s + 2)(s + 5)} = \frac{100}{2 \times 5} = 10$.
- Input magnitude $A = 4$.
- Steady-state error $e_{ss} = \frac{A}{K_v} = \frac{4}{10} = 0.4$.

---

### Q-CTL-004 `[ESE-EE-2018]` 🟢 Easy
**Topic:** Controllers & Compensators
**Question:** The introduction of derivative control (PD controller) in a feedback system results in:
- (A) Increased steady-state error and sluggish response
- (B) Improved transient response, increased damping, and reduced peak overshoot
- (C) Increased system type and eliminated steady-state error
- (D) Destabilization of an already stable system
**Answer:** (B)
**Concept/Formula:**
- Derivative control adds a zero in the left half plane: increases damping ($\zeta$), reduces overshoot ($M_p$), increases stability margin, and speeds up response.
- Integral control (PI) increases system type by 1 and eliminates steady-state error, but reduces stability and damping.

---

### Q-CTL-005 `[GATE-EE-2018]` 🟡 Moderate
**Topic:** Root Locus — Asymptotes & Angle of Departure
**Question:** An open-loop transfer function is given by $G(s)H(s) = \frac{K}{s(s + 2)(s + 4)}$. The asymptotes of the root loci meet on the real axis at a centroid ($\sigma_A$) equal to:
- (A) $-2.0$
- (B) $-3.0$
- (C) $-1.5$
- (D) $-6.0$
**Answer:** (A)
**Concept/Formula:**
- Centroid of asymptotes: $\sigma_A = \frac{\sum \text{Real parts of Poles} - \sum \text{Real parts of Zeros}}{P - Z}$.
- Poles: $s = 0, -2, -4 \implies \sum P = 0 - 2 - 4 = -6$.
- Zeros: None $\implies \sum Z = 0$.
- $P = 3,\ Z = 0 \implies P - Z = 3$.
- $\sigma_A = \frac{-6 - 0}{3} = -2.0$.
- Angles of asymptotes: $\theta_A = \frac{(2q + 1)180^\circ}{3} = 60^\circ, 180^\circ, 300^\circ$.

---

### Q-CTL-006 `[ESE-EE-2021]` 🟡 Moderate
**Topic:** Bode Plot — Gain Margin & Phase Margin
**Question:** In a Bode diagram, if the Phase Margin (PM) is $+40^\circ$ and the Gain Margin (GM) is $+12\text{ dB}$, the closed-loop system is:
- (A) Marginally stable
- (B) Unstable
- (C) Stable
- (D) Conditionally stable
**Answer:** (C)
**Concept/Formula:**
- For a minimum-phase system, if BOTH Gain Margin and Phase Margin are strictly positive ($\text{GM} > 0\text{ dB}$ and $\text{PM} > 0^\circ$), the closed-loop system is guaranteed to be **Stable**.
- If $\text{GM} = 0\text{ dB}$ and $\text{PM} = 0^\circ \implies$ Marginally stable.
- If either $\text{GM} < 0\text{ dB}$ or $\text{PM} < 0^\circ \implies$ Unstable.

---

### Q-CTL-007 `[GATE-EE-2016]` 🟠 Difficult
**Topic:** Nyquist Stability Criterion
**Question:** The open-loop transfer function of a unity feedback system has 1 pole in the right-half of the s-plane ($P = 1$). For the closed-loop system to be stable, the Nyquist plot of $G(s)H(s)$ must encircle the critical point $(-1 + j0)$:
- (A) Once in clockwise direction
- (B) Once in counter-clockwise direction
- (C) Twice in counter-clockwise direction
- (D) Zero times (must not encircle)
**Answer:** (B)
**Concept/Formula:**
- Nyquist stability formula: $N = P - Z$, where:
  - $N$ = Number of counter-clockwise (CCW) encirclements of $(-1 + j0)$.
  - $P$ = Number of open-loop poles in RHS of s-plane.
  - $Z$ = Number of closed-loop poles in RHS of s-plane.
- For closed-loop stability, we require $Z = 0 \implies N = P - 0 = P$.
- Since $P = 1$, we must have $N = 1$ (exactly ONE counter-clockwise encirclement).

---

### Q-CTL-008 `[ISRO-EE-2019]` 🟢 Easy
**Topic:** Phase Lead vs Phase Lag Compensators
**Question:** A phase-lead compensator has a transfer function $G_c(s) = \frac{s + 2}{s + 10}$. The maximum phase lead ($\phi_m$) occurs at frequency $\omega_m$ equal to:
- (A) $2\text{ rad/s}$
- (B) $4.47\text{ rad/s}$
- (C) $6.0\text{ rad/s}$
- (D) $10\text{ rad/s}$
**Answer:** (B)
**Concept/Formula:**
- For compensator $G_c(s) = \frac{s + z}{s + p}$:
- Maximum phase frequency $\omega_m = \sqrt{z \cdot p} = \sqrt{2 \times 10} = \sqrt{20} \approx 4.47\text{ rad/s}$.
- Note: Since pole $p = 10$ is farther to the left than zero $z = 2$ ($z < p$), it is a **Lead Compensator**.

---

### Q-CTL-009 `[GATE-EE-2020]` 🟡 Moderate
**Topic:** State-Space Representation — Resolvent Matrix & State Transition
**Question:** The state matrix of a continuous-time system is $A = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix}$. The eigenvalues of $A$ (system poles) are:
- (A) $-1$ and $-2$
- (B) $+1$ and $+2$
- (C) $0$ and $-3$
- (D) $-1$ and $+2$
**Answer:** (A)
**Concept/Formula:**
- Characteristic equation: $\det(sI - A) = 0$.
- $\det \begin{bmatrix} s & -1 \\ 2 & s + 3 \end{bmatrix} = s(s + 3) - (-2) = s^2 + 3s + 2 = (s + 1)(s + 2) = 0$.
- Eigenvalues: $s_1 = -1,\ s_2 = -2$.

---

### Q-CTL-010 `[ESE-EE-2019]` 🟢 Easy
**Topic:** Block Diagram Reduction & Mason's Rule
**Question:** In a signal flow graph, the gain of a path that passes through each node not more than once is termed as:
- (A) Loop gain
- (B) Forward path gain
- (C) Non-touching loop gain
- (D) Feedback gain
**Answer:** (B)
**Concept/Formula:**
- **Forward path:** A path from an input node to an output node that passes through no node more than once.
- **Mason's Gain Formula:** $T = \frac{\sum P_k \Delta_k}{\Delta}$, where $P_k$ is the gain of the $k$-th forward path.

---

### Q-CTL-011 `[GATE-EE-2019]` 🟡 Moderate
**Topic:** State-Space Analysis — Kalman's Controllability Test
**Question:** A continuous-time LTI system is described by the state equation:
$$\dot{x} = \begin{bmatrix} 1 & 0 \\ 0 & -2 \end{bmatrix} x + \begin{bmatrix} 1 \\ 0 \end{bmatrix} u$$
The system is:
- (A) Controllable and stable
- (B) Uncontrollable and unstable
- (C) Completely controllable but unstable
- (D) Completely observable and stable
**Answer:** (B)
**Concept/Formula:**
- Controllability matrix: $Q_c = [B \quad AB]$.
  $$AB = \begin{bmatrix} 1 & 0 \\ 0 & -2 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$
  $$Q_c = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix} \implies \det(Q_c) = 0 \implies \text{Rank}(Q_c) = 1 < 2 \text{ (Uncontrollable)}$$
- System eigenvalues (poles) are roots of $\det(sI - A) = 0 \implies s_1 = +1$ (RHP, unstable) and $s_2 = -2$.
- Because eigenvalue $+1$ lies in the RHP, the system is **Unstable**.

---

### Q-CTL-012 `[ESE-EE-2021]` 🟡 Moderate
**Topic:** Root Locus — Breakaway Points
**Question:** For a unity feedback system with open-loop transfer function $G(s) = \frac{K}{s(s + 4)}$, the root locus breakaway point on the real axis occurs at:
- (A) $s = -2$
- (B) $s = -4$
- (C) $s = 0$
- (D) $s = -1$
**Answer:** (A)
**Concept/Formula:**
- Characteristic equation: $1 + G(s) = 0 \implies s^2 + 4s + K = 0 \implies K = -s^2 - 4s$.
- Differentiating with respect to $s$:
  $$\frac{dK}{ds} = -2s - 4 = 0 \implies 2s = -4 \implies s = -2$$
- Since $s = -2$ lies on the real axis between poles $s = 0$ and $s = -4$ where root locus exists, $s = -2$ is a valid breakaway point.

---

### Q-CTL-013 `[GATE-EE-2015]` 🟢 Easy
**Topic:** Frequency Domain — Initial Slope of Bode Magnitude Plot
**Question:** If the initial low-frequency asymptotic slope of the Bode magnitude plot of a transfer function is $-40\text{ dB/decade}$, the system has:
- (A) No poles at the origin (Type 0)
- (B) One pole at the origin (Type 1)
- (C) Two poles at the origin (Type 2)
- (D) Two zeros at the origin
**Answer:** (C)
**Concept/Formula:**
- An initial slope of $0\text{ dB/decade}$ indicates a **Type 0** system.
- An initial slope of $-20\text{ dB/decade}$ indicates a **Type 1** system (one integrator $\frac{1}{s}$).
- An initial slope of $-40\text{ dB/decade}$ indicates a **Type 2** system (two integrators $\frac{1}{s^2}$).
- Generally, initial slope $= -20N\text{ dB/decade}$, where $N$ is the system Type.

---

### Q-CTL-014 `[ESE-EE-2020]` 🟡 Moderate
**Topic:** Controller Design — Ziegler-Nichols Frequency Response Tuning
**Question:** In the Ziegler-Nichols continuous cycling method for tuning a PID controller, the ultimate gain is found to be $K_u = 10$ and the ultimate period of sustained oscillations is $T_u = 4\text{ seconds}$. The tuned controller parameters ($K_p$, integral time $T_i$, and derivative time $T_d$) are:
- (A) $K_p = 6.0,\ T_i = 2.0\text{ s},\ T_d = 0.5\text{ s}$
- (B) $K_p = 5.0,\ T_i = 4.0\text{ s},\ T_d = 1.0\text{ s}$
- (C) $K_p = 4.5,\ T_i = 1.5\text{ s},\ T_d = 0.375\text{ s}$
- (D) $K_p = 10.0,\ T_i = 0.5\text{ s},\ T_d = 0.125\text{ s}$
**Answer:** (A)
**Concept/Formula:**
- Classical Ziegler-Nichols tuning formulas for a PID controller:
  - $K_p = 0.6 \cdot K_u = 0.6 \times 10 = 6.0$
  - $T_i = 0.5 \cdot T_u = 0.5 \times 4\text{ s} = 2.0\text{ s}$
  - $T_d = 0.125 \cdot T_u = \frac{4}{8}\text{ s} = 0.5\text{ s}$

---

### Q-CTL-015 `[ISRO-EE-2018]` 🟡 Moderate
**Topic:** Nyquist Criterion & Polar Plots
**Question:** The polar plot of an open-loop transfer function $G(s) = \frac{1}{(1 + sT_1)(1 + sT_2)}$ as $\omega$ increases from $0$ to $\infty$ starts at:
- (A) Magnitude $1$, phase $0^\circ$ and terminates at origin $(0, 0)$ with phase $-180^\circ$
- (B) Origin $(0,0)$ and terminates at infinity
- (C) Magnitude $\infty$, phase $-90^\circ$
- (D) Magnitude $0.5$, phase $-45^\circ$
**Answer:** (A)
**Concept/Formula:**
- Magnitude: $|G(j\omega)| = \frac{1}{\sqrt{1 + \omega^2 T_1^2}\sqrt{1 + \omega^2 T_2^2}}$.
- Phase: $\angle G(j\omega) = -\tan^{-1}(\omega T_1) - \tan^{-1}(\omega T_2)$.
- At $\omega = 0$: $|G| = 1,\ \angle G = 0^\circ$ (Point $(+1, 0)$ on positive real axis).
- At $\omega \to \infty$: $|G| \to 0,\ \angle G \to -180^\circ$ (Enters the origin along the negative real axis).
- Entire plot lies within the fourth and third quadrants of the complex plane.

