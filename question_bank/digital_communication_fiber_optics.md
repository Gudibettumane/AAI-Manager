# AUTHENTIC QUESTION BANK: DIGITAL COMMUNICATION & FIBER OPTIC SYSTEMS
*Sources: GATE EC/EE, ESE Prelims, ISRO, BEL, AAI CNS/ATC PYQs*

---

### Q-DCF-001 `[GATE-EC/EE-2019]` 🟡 Moderate
**Topic:** Pulse Code Modulation (PCM) — Quantization Noise & Bandwidth
**Question:** In a uniform PCM system, if the number of quantization levels is increased from $64$ to $256$, the signal-to-quantization noise ratio (SQNR) improves by approximately:
- (A) $6\text{ dB}$
- (B) $12\text{ dB}$
- (C) $18\text{ dB}$
- (D) $24\text{ dB}$
**Answer:** (B)
**Concept/Formula:**
- $L_1 = 64 = 2^6 \implies n_1 = 6\text{ bits/sample}$.
- $L_2 = 256 = 2^8 \implies n_2 = 8\text{ bits/sample}$.
- Number of bits added: $\Delta n = 8 - 6 = 2\text{ bits}$.
- Golden Rule for PCM: Every additional bit increases the SQNR by approximately $6\text{ dB}$ ($(\text{SQNR})_{dB} \approx 1.76 + 6.02 n$).
- Therefore, for 2 extra bits: Improvement = $2 \times 6\text{ dB} = 12\text{ dB}$.

---

### Q-DCF-002 `[ESE-EE/EC-2020]` 🟢 Easy
**Topic:** Delta Modulation — Slope Overload Distortion
**Question:** In Delta Modulation (DM), "slope overload distortion" occurs when:
- (A) The input signal amplitude is too small relative to step size
- (B) The rate of change of the input signal exceeds the maximum rate of rise of the staircase approximation ($\left|\frac{dx(t)}{dt}\right| > \frac{\Delta}{T_s}$)
- (C) The sampling frequency is much higher than the Nyquist rate
- (D) The step size $\Delta$ is made too large
**Answer:** (B)
**Concept/Formula:**
- Maximum slope of the staircase: $\frac{\Delta}{T_s} = \Delta \cdot f_s$.
- If $\left|\frac{dx(t)}{dt}\right|_{max} > \Delta \cdot f_s \implies$ **Slope Overload Distortion**.
- Remedy: Increase step size $\Delta$ or increase sampling frequency $f_s$ (Adaptive Delta Modulation - ADM).
- If $\Delta$ is too large when input is flat/slowly varying $\implies$ **Granular (Idle) Noise**.

---

### Q-DCF-003 `[GATE-EC/EE-2018]` 🟡 Moderate
**Topic:** Digital Modulation Schemes — ASK, PSK, FSK
**Question:** Which digital modulation scheme provides the highest power efficiency (lowest bit error rate for a given $E_b/N_0$)?
- (A) Coherent BPSK (Binary Phase Shift Keying)
- (B) Coherent BFSK (Binary Frequency Shift Keying)
- (C) Non-coherent BASK (Amplitude Shift Keying / OOK)
- (D) DPSK (Differential Phase Shift Keying)
**Answer:** (A)
**Concept/Formula:**
- Bit error probability for coherent BPSK is $P_e = Q\left(\sqrt{\frac{2 E_b}{N_0}}\right)$.
- For coherent BFSK: $P_e = Q\left(\sqrt{\frac{E_b}{N_0}}\right)$, requiring $3\text{ dB}$ more power than BPSK for the same error rate.
- BASK is even less power efficient and highly susceptible to amplitude noise.

---

### Q-DCF-004 `[ESE-EE/EC-2021]` 🟢 Easy
**Topic:** Computer Networks — OSI 7-Layer Architecture
**Question:** In the ISO-OSI 7-layer reference model, the layer responsible for end-to-end reliable data delivery, flow control, and error recovery is:
- (A) Network Layer
- (B) Transport Layer
- (C) Data Link Layer
- (D) Session Layer
**Answer:** (B)
**Concept/Formula:**
- **Layer 4 (Transport Layer):** End-to-end communication, segmentation, reassembly, reliable delivery (TCP/UDP), flow control.
- **Layer 3 (Network Layer):** Routing, logical addressing (IP addresses), packet forwarding.
- **Layer 2 (Data Link Layer):** Hop-to-hop framing, physical addressing (MAC addresses), error detection (CRC).
- **Layer 1 (Physical Layer):** Transmission of raw bitstream over physical media.

---

### Q-DCF-005 `[GATE-EC/EE-2017]` 🟡 Moderate
**Topic:** Fiber Optics — Numerical Aperture & Acceptance Angle
**Question:** An optical fiber has a core refractive index $n_1 = 1.50$ and a cladding refractive index $n_2 = 1.47$. The Numerical Aperture (NA) of the fiber in air is approximately:
- (A) $0.30$
- (B) $0.45$
- (C) $0.15$
- (D) $0.60$
**Answer:** (A)
**Concept/Formula:**
- $\text{NA} = \sqrt{n_1^2 - n_2^2} = \sqrt{(1.50)^2 - (1.47)^2} = \sqrt{2.25 - 2.1609} = \sqrt{0.0891} \approx 0.2985 \approx 0.30$.
- Maximum acceptance angle in air $\theta_a = \sin^{-1}(\text{NA}) = \sin^{-1}(0.30) \approx 17.4^\circ$.

---

### Q-DCF-006 `[ISRO-EC/EE-2020]` 🟢 Easy
**Topic:** Optical Sources — Laser Diode vs LED
**Question:** In fiber optic communication systems, Laser diodes are preferred over LEDs for long-distance, high-bit-rate optical links because Laser diodes provide:
- (A) Broader spectral width and incoherent emission
- (B) Narrow spectral line-width, high output power, and coherent stimulated emission
- (C) Lower cost and simple drive circuitry
- (D) Freedom from temperature dependence
**Answer:** (B)
**Concept/Formula:**
- Laser diodes emit monochromatic, spatially coherent light with a very narrow spectral width ($\Delta \lambda < 1\text{–}2\text{ nm}$ compared to $30\text{–}50\text{ nm}$ for LEDs), minimizing chromatic dispersion and allowing multi-gigabit transmission over long spans.
