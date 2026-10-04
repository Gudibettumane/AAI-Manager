# AUTHENTIC QUESTION BANK: SIGNALS AND SYSTEMS
*Sources: GATE EE/EC, ESE Prelims, ISRO EE*

---

### Q-SIG-001 `[GATE-EE-2019]` 🟢 Easy
**Topic:** Signal Operations — Time Shifting and Scaling
**Question:** A continuous-time signal $x(t)$ is non-zero only over the interval $[-2, 4]$. The signal $y(t) = x(2t - 3)$ is non-zero only over the interval:
- (A) $[0.5, 3.5]$
- (B) $[-1, 5]$
- (C) $[-7, 5]$
- (D) $[1, 7]$
**Answer:** (A)
**Concept/Formula:**
- Given: $-2 \le \tau \le 4$, where $\tau = 2t - 3$.
- $-2 \le 2t - 3 \le 4 \implies 1 \le 2t \le 7 \implies 0.5 \le t \le 3.5$.
- Transformation order: Shift by 3 to the right, then compress by factor 2.

---

### Q-SIG-002 `[ESE-EE-2020]` 🟡 Moderate
**Topic:** LTI and Causal Systems
**Question:** A continuous-time system is described by the input-output relationship $y(t) = x(t) \cos(100\pi t)$. The system is:
- (A) Linear, time-invariant, and causal
- (B) Linear, time-variant, and causal
- (C) Non-linear, time-invariant, and non-causal
- (D) Linear, time-invariant, and non-causal
**Answer:** (B)
**Concept/Formula:**
- **Linearity:** Homogeneity and additivity hold $\implies$ Linear.
- **Time Invariance:** Delaying input gives $x(t - t_0) \cos(100\pi t)$, whereas delaying output gives $x(t - t_0) \cos(100\pi (t - t_0))$. Since the two are not equal due to the explicit $t$ in $\cos(100\pi t)$, the system is **Time-Variant**.
- **Causality:** $y(t)$ depends only on the present input $x(t)$ $\implies$ **Causal**.

---

### Q-SIG-003 `[GATE-EE-2018]` 🟡 Moderate
**Topic:** Laplace Transform & Region of Convergence (ROC)
**Question:** The bilateral Laplace transform of a signal $x(t) = e^{-3t} u(t) + e^{2t} u(-t)$ is:
- (A) $X(s) = \frac{1}{s + 3} - \frac{1}{s - 2}$, with ROC: $-3 < \text{Re}(s) < 2$
- (B) $X(s) = \frac{1}{s + 3} + \frac{1}{s - 2}$, with ROC: $\text{Re}(s) > -3$
- (C) $X(s) = \frac{-5}{(s + 3)(s - 2)}$, with ROC: $\text{Re}(s) < 2$
- (D) Laplace transform does not exist
**Answer:** (A)
**Concept/Formula:**
- $\mathcal{L}\{e^{-3t} u(t)\} = \frac{1}{s + 3}$, with ROC: $\text{Re}(s) > -3$.
- $\mathcal{L}\{e^{2t} u(-t)\} = -\frac{1}{s - 2}$, with ROC: $\text{Re}(s) < 2$.
- Overall ROC is the intersection: $-3 < \text{Re}(s) < 2$.
- Since ROC includes the $j\omega$-axis ($\text{Re}(s) = 0$), the Fourier transform also exists.

---

### Q-SIG-004 `[GATE-EC/EE-2017]` 🟡 Moderate
**Topic:** Z-Transform & Discrete-Time System Stability
**Question:** A discrete-time causal LTI system has a system function $H(z) = \frac{1}{1 - 0.5 z^{-1}}$. For the system to be stable and causal, the ROC must be:
- (A) $|z| < 0.5$
- (B) $|z| > 0.5$
- (C) $0.5 < |z| < 1$
- (D) Entire z-plane except $z = 0$
**Answer:** (B)
**Concept/Formula:**
- For a **causal** system, the ROC is the exterior of a circle: $|z| > |p|$. Here pole is at $z = 0.5 \implies$ ROC is $|z| > 0.5$.
- For **stability**, the ROC must enclose the unit circle ($|z| = 1$).
- Since $|z| > 0.5$ includes the unit circle $|z| = 1$, the system is both causal and stable.

---

### Q-SIG-005 `[ESE-EE-2021]` 🟢 Easy
**Topic:** Fourier Transform — Duality & Sinc Function
**Question:** The Fourier transform of a rectangular pulse of width $T$ and unit height centered at the origin in the time domain is:
- (A) A triangular function
- (B) A sinc function: $T \frac{\sin(\omega T / 2)}{\omega T / 2}$
- (C) An impulse train
- (D) An exponential decay
**Answer:** (B)
**Concept/Formula:** Rectangular pulse in time domain $\mathcal{F} \longleftrightarrow$ Sinc pulse in frequency domain ($\mathcal{F}\{\text{rect}(t/T)\} = T \cdot \text{sinc}(\omega T / 2\pi)$).
