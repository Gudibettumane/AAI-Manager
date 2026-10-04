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

---

### Q-SIG-006 `[GATE-EE-2015]` 🟢 Easy
**Topic:** Energy and Power Signals
**Question:** A continuous-time signal is given by $x(t) = e^{-2t} u(t)$. The total energy $E$ of this signal is:
- (A) $0.25\text{ J}$
- (B) $0.50\text{ J}$
- (C) $1.0\text{ J}$
- (D) $\infty$ (Infinite)
**Answer:** (A)
**Concept/Formula:**
- Energy $E = \int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{0}^{\infty} (e^{-2t})^2 dt = \int_{0}^{\infty} e^{-4t} dt = \left[ \frac{e^{-4t}}{-4} \right]_0^\infty = 0 - \left(-\frac{1}{4}\right) = \frac{1}{4} = 0.25\text{ J}$.
- Since $0 < E < \infty$, $x(t)$ is an **Energy Signal** with average power $P = 0$.

---

### Q-SIG-007 `[ESE-EE-2018]` 🟢 Easy
**Topic:** Dirac Delta Impulse Function Properties
**Question:** The value of the integral $\int_{-\infty}^{\infty} (t^3 + 4t + 5) \delta(t - 2) dt$ is:
- (A) 5
- (B) 17
- (C) 21
- (D) 0
**Answer:** (C)
**Concept/Formula:**
- Sifting property of Dirac delta: $\int_{-\infty}^{\infty} f(t) \delta(t - t_0) dt = f(t_0)$.
- Here $t_0 = 2 \implies f(2) = (2)^3 + 4(2) + 5 = 8 + 8 + 5 = 21$.

---

### Q-SIG-008 `[GATE-EE-2020]` 🟡 Moderate
**Topic:** Convolution of Finite Duration Signals
**Question:** Two rectangular pulses $x_1(t)$ of duration $3\text{ seconds}$ and $x_2(t)$ of duration $5\text{ seconds}$ are convolved. The total duration of the resulting output signal $y(t) = x_1(t) * x_2(t)$ is:
- (A) $8\text{ seconds}$
- (B) $15\text{ seconds}$
- (C) $5\text{ seconds}$
- (D) $2\text{ seconds}$
**Answer:** (A)
**Concept/Formula:**
- Width property of continuous convolution: If $x_1(t)$ has duration $T_1$ and $x_2(t)$ has duration $T_2$, then $y(t) = x_1(t) * x_2(t)$ has duration $T_y = T_1 + T_2$.
- Here: $T_y = 3 + 5 = 8\text{ seconds}$.

---

### Q-SIG-009 `[ESE-EE-2019]` 🟡 Moderate
**Topic:** Laplace Transform — Initial and Final Value Theorems
**Question:** The Laplace transform of a signal $x(t)$ is $X(s) = \frac{s + 4}{s(s + 2)(s + 5)}$. The final value of $x(t)$ as $t \to \infty$ is:
- (A) $0.4$
- (B) $0.8$
- (C) $0$
- (D) Does not exist
**Answer:** (A)
**Concept/Formula:**
- Final Value Theorem: $\lim_{t \to \infty} x(t) = \lim_{s \to 0} s X(s)$.
- Condition of validity: All poles of $sX(s)$ must lie strictly in the left half of the s-plane ($\text{Re}(s) < 0$).
- Here $sX(s) = \frac{s + 4}{(s + 2)(s + 5)}$. Poles are at $s = -2$ and $s = -5$ (both strictly LHP $\implies$ theorem is valid).
- $\lim_{s \to 0} sX(s) = \frac{0 + 4}{(0 + 2)(0 + 5)} = \frac{4}{10} = 0.4$.

---

### Q-SIG-010 `[GATE-EC/EE-2016]` 🟢 Easy
**Topic:** Sampling Theorem & Nyquist Rate
**Question:** A continuous-time signal $x(t) = 5 \cos(200\pi t) + 10 \sin(500\pi t) - 3 \cos(800\pi t)$ is sampled. To avoid aliasing, the minimum sampling frequency (Nyquist rate) must be:
- (A) $400\text{ Hz}$
- (B) $800\text{ Hz}$
- (C) $1600\text{ Hz}$
- (D) $200\text{ Hz}$
**Answer:** (B)
**Concept/Formula:**
- Frequencies present:
  - $\omega_1 = 200\pi \implies f_1 = 100\text{ Hz}$
  - $\omega_2 = 500\pi \implies f_2 = 250\text{ Hz}$
  - $\omega_3 = 800\pi \implies f_3 = 400\text{ Hz}$
- Maximum frequency component $f_{max} = 400\text{ Hz}$.
- Nyquist Rate $f_s = 2 f_{max} = 2 \times 400 = 800\text{ Hz}$ (or samples/second).

---

### Q-SIG-011 `[ISRO-EE-2018]` 🟡 Moderate
**Topic:** Discrete-Time Signals — Even and Odd Components
**Question:** The odd component $x_o(t)$ of a signal $x(t)$ is defined as:
- (A) $\frac{x(t) - x(-t)}{2}$
- (B) $\frac{x(t) + x(-t)}{2}$
- (C) $x(t) \cdot x(-t)$
- (D) $x(t) - x(-t)$
**Answer:** (A)
**Concept/Formula:**
- Any signal $x(t) = x_e(t) + x_o(t)$.
- Even component: $x_e(t) = \frac{x(t) + x(-t)}{2}$ (satisfies $x_e(-t) = x_e(t)$).
- Odd component: $x_o(t) = \frac{x(t) - x(-t)}{2}$ (satisfies $x_o(-t) = -x_o(t)$).

---

### Q-SIG-012 `[GATE-EE-2014]` 🟡 Moderate
**Topic:** Discrete-Time Fourier Transform (DTFT) — Periodicity
**Question:** The Discrete-Time Fourier Transform $X(e^{j\Omega})$ of any discrete-time sequence $x[n]$ is always:
- (A) Periodic with period $\pi$
- (B) Periodic with period $2\pi$
- (C) Non-periodic
- (D) Periodic with period dependent on the sequence length
**Answer:** (B)
**Concept/Formula:**
- $X(e^{j(\Omega + 2\pi)}) = \sum_{n=-\infty}^\infty x[n] e^{-j(\Omega + 2\pi)n} = \sum x[n] e^{-j\Omega n} (e^{-j2\pi n}) = X(e^{j\Omega})$ because $e^{-j2\pi n} = 1$ for all integer $n$.
- Therefore, DTFT is strictly periodic with fundamental period **$2\pi$ radians**.

---

### Q-SIG-013 `[ESE-EE-2021]` 🟢 Easy
**Topic:** Continuous-Time LTI System — Stability Criterion
**Question:** A continuous-time LTI system with impulse response $h(t)$ is Bounded-Input Bounded-Output (BIBO) stable if and only if:
- (A) $\int_{-\infty}^{\infty} |h(t)| dt < \infty$ (Impulse response is absolutely integrable)
- (B) $h(t) = 0$ for $t < 0$
- (C) $\int_{-\infty}^{\infty} |h(t)|^2 dt = 0$
- (D) $\lim_{t \to \infty} h(t) = \infty$
**Answer:** (A)
**Concept/Formula:** Necessary and sufficient condition for BIBO stability of an LTI system is absolute integrability of impulse response: $\int_{-\infty}^{\infty} |h(t)| dt < \infty$. In s-domain, this requires all poles of $H(s)$ to lie strictly in the open left-half of the complex s-plane.

---

### Q-SIG-014 `[GATE-EE-2017]` 🟡 Moderate
**Topic:** Z-Transform of Elementary Sequences
**Question:** The Z-transform of the causal ramp sequence $x[n] = n u[n]$ is:
- (A) $\frac{z^{-1}}{(1 - z^{-1})^2}$, with ROC $|z| > 1$
- (B) $\frac{1}{1 - z^{-1}}$, with ROC $|z| > 1$
- (C) $\frac{z}{(z - 1)}$, with ROC $|z| < 1$
- (D) $\frac{z^{-2}}{(1 - z^{-1})^2}$, with ROC $|z| > 1$
**Answer:** (A)
**Concept/Formula:**
- Differentiation in z-domain property: $\mathcal{Z}\{n x[n]\} = -z \frac{d}{dz} X(z)$.
- For $x[n] = u[n] \implies X(z) = \frac{1}{1 - z^{-1}} = \frac{z}{z - 1}$.
- $\mathcal{Z}\{n u[n]\} = -z \frac{d}{dz} \left(\frac{z}{z - 1}\right) = -z \left[\frac{(z - 1)(1) - z(1)}{(z - 1)^2}\right] = -z \left[\frac{-1}{(z - 1)^2}\right] = \frac{z}{(z - 1)^2} = \frac{z^{-1}}{(1 - z^{-1})^2}$, ROC $|z| > 1$.

---

### Q-SIG-015 `[ESE-EE-2020]` 🟢 Easy
**Topic:** Impulse Response and Step Response Relation
**Question:** In an LTI system, the relationship between the unit step response $s(t)$ and the unit impulse response $h(t)$ is:
- (A) $h(t) = \frac{d}{dt} s(t)$
- (B) $s(t) = \frac{d}{dt} h(t)$
- (C) $h(t) = \int_{-\infty}^{t} s(\tau) d\tau$
- (D) $h(t) = s(t) \cdot u(t)$
**Answer:** (A)
**Concept/Formula:** Since the unit impulse is the derivative of the unit step ($\delta(t) = \frac{d}{dt} u(t)$), the impulse response is the derivative of the step response: $h(t) = \frac{ds(t)}{dt}$. Conversely, $s(t) = \int_{-\infty}^t h(\tau) d\tau$.
