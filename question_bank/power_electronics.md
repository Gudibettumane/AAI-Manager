# AUTHENTIC QUESTION BANK: POWER ELECTRONICS & DRIVES
*Sources: AAI JE/Manager PYQs, ESE Prelims EE, GATE EE, ISRO, PGCIL*

---

### Q-PEL-001 `[AAI-JE-EE-2018]` 🟢 Easy
**Topic:** SCR Ratings — Latching vs Holding Current
**Question:** In a Thyristor (SCR), the latching current is:
- (A) Associated with the turn-off process and is lower than the holding current
- (B) Associated with the turn-on process and is higher than the holding current
- (C) Exactly equal to the holding current
- (D) Independent of gate pulse duration
**Answer:** (B)
**Concept/Formula:** 
- Latching current ($I_L$): Minimum anode current that must be attained during turn-on before the gate trigger pulse is removed so that the SCR remains ON.
- Holding current ($I_H$): Minimum anode current below which the SCR turns OFF during commutation.
- Fundamental rule: $I_L > I_H$ (typically $I_L \approx 2 \text{ to } 3 \times I_H$).

---

### Q-PEL-002 `[ESE-EE-2020]` 🟡 Moderate
**Topic:** Single-Phase Full Converter
**Question:** A single-phase fully controlled bridge converter is fed from a $230\text{ V},\ 50\text{ Hz}$ AC source. If the firing angle $\alpha = 60^\circ$ and load current is continuous and ripple-free, the average DC output voltage is:
- (A) $103.5\text{ V}$
- (B) $207.1\text{ V}$
- (C) $146.4\text{ V}$
- (D) $230.0\text{ V}$
**Answer:** (A)
**Concept/Formula:**
- $V_{dc} = \frac{2 V_m}{\pi} \cos \alpha = \frac{2 \times (230 \sqrt{2})}{\pi} \cos 60^\circ$.
- $V_{dc} = \frac{2 \times 325.27}{\pi} \times 0.5 = \frac{325.27}{\pi} \approx 103.54\text{ V}$.

---

### Q-PEL-003 `[GATE-EE-2017]` 🟡 Moderate
**Topic:** DC-DC Choppers
**Question:** A step-down DC chopper operates from a $100\text{ V}$ DC supply and feeds an $RL$ load. The switching frequency is $1\text{ kHz}$ and the duty cycle $D = 0.4$. The average output voltage is:
- (A) $40\text{ V}$
- (B) $60\text{ V}$
- (C) $250\text{ V}$
- (D) $100\text{ V}$
**Answer:** (A)
**Concept/Formula:**
- Buck / Step-down chopper: $V_{o,avg} = D \times V_s = 0.4 \times 100\text{ V} = 40\text{ V}$.
- For boost / step-up chopper: $V_{o,avg} = \frac{V_s}{1 - D}$.

---

### Q-PEL-004 `[ESE-EE-2019]` 🟢 Easy
**Topic:** Inverters — Output Harmonics & PWM
**Question:** In single-pulse width modulation (PWM) of a single-phase voltage source inverter, to completely eliminate the $n$-th harmonic from the output voltage waveform, the pulse width $2d$ must be chosen such that:
- (A) $2d = \frac{180^\circ}{n}$
- (B) $2d = \frac{360^\circ}{n}$
- (C) $2d = n \times 180^\circ$
- (D) $2d = \frac{90^\circ}{n}$
**Answer:** (B)
**Concept/Formula:**
- The $n$-th harmonic amplitude in single-pulse PWM is proportional to $\sin(n d)$.
- To eliminate the $n$-th harmonic: $\sin(n d) = 0 \implies n d = 180^\circ \implies d = \frac{180^\circ}{n}$.
- Therefore, the full pulse width $2d = \frac{360^\circ}{n}$.
- Example: To eliminate the 3rd harmonic ($n=3$), pulse width $2d = \frac{360^\circ}{3} = 120^\circ$.
