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
