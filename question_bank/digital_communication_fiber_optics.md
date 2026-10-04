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

---

### Q-DCF-007 `[GATE-EC/EE-2016]` 🟡 Moderate
**Topic:** Optical Fibers — V-Number & Single-Mode Cutoff
**Question:** For a step-index optical fiber to operate in single-mode regime ($V < 2.405$), the normalized frequency parameter $V$ is given by $V = \frac{2\pi a}{\lambda} \text{NA}$. If core radius $a = 4\ \mu\text{m}$ and $\text{NA} = 0.12$, the cut-off wavelength $\lambda_c$ below which multi-mode propagation begins is:
- (A) $1.25\ \mu\text{m}$
- (B) $1.55\ \mu\text{m}$
- (C) $0.85\ \mu\text{m}$
- (D) $2.40\ \mu\text{m}$
**Answer:** (A)
**Concept/Formula:**
- $V_c = 2.405 = \frac{2\pi a}{\lambda_c} \text{NA} \implies \lambda_c = \frac{2\pi a \cdot \text{NA}}{2.405} = \frac{2\pi \times 4 \times 0.12}{2.405} = \frac{3.016}{2.405} \approx 1.254\ \mu\text{m}$.
- For single-mode operation, operating wavelength must be $\lambda > \lambda_c$.

---

### Q-DCF-008 `[ESE-EE/EC-2019]` 🟢 Easy
**Topic:** Fiber Optic Transmission Windows & Attenuation
**Question:** In silica glass optical fibers, the lowest optical attenuation (loss $\approx 0.2\text{ dB/km}$) occurs at which standard optical wavelength window?
- (A) $850\text{ nm}$
- (B) $1310\text{ nm}$
- (C) $1550\text{ nm}$
- (D) $632.8\text{ nm}$
**Answer:** (C)
**Concept/Formula:**
- First window ($850\text{ nm}$): Loss $\approx 2\text{–}3\text{ dB/km}$ (limited by Rayleigh scattering $\propto 1/\lambda^4$).
- Second window ($1310\text{ nm}$): Zero material dispersion point, loss $\approx 0.4\text{ dB/km}$.
- **Third window ($1550\text{ nm}$):** Absolute minimum loss ($\approx 0.2\text{ dB/km}$), standard for long-haul telecom.

---

### Q-DCF-009 `[GATE-EC/EE-2017]` 🟡 Moderate
**Topic:** Information Theory — Shannon Channel Capacity
**Question:** A communication channel has a bandwidth $B = 4\text{ kHz}$ and a signal-to-noise ratio $\text{SNR} = 15$. The theoretical channel capacity $C$ in bits per second (bps) is:
- (A) $16\text{ kbps}$
- (B) $32\text{ kbps}$
- (C) $60\text{ kbps}$
- (D) $8\text{ kbps}$
**Answer:** (A)
**Concept/Formula:**
- Shannon's Capacity formula: $C = B \log_2(1 + \text{SNR})$.
- $C = 4000 \log_2(1 + 15) = 4000 \log_2(16) = 4000 \times 4 = 16,000\text{ bps} = 16\text{ kbps}$.

---

### Q-DCF-010 `[ESE-EE/EC-2020]` 🟢 Easy
**Topic:** Multiplexing — TDM vs FDM
**Question:** In Frequency Division Multiplexing (FDM), adjacent channels are separated in frequency by:
- (A) Time slots
- (B) Guard bands
- (C) Parity bits
- (D) Orthogonal codes
**Answer:** (B)
**Concept/Formula:**
- **FDM:** Guard bands prevent spectral overlap and inter-channel crosstalk.
- **TDM:** Guard times prevent time-domain collision between adjacent time slots due to transmission delays.

---

### Q-DCF-011 `[GATE-EC-2018]` 🟡 Moderate
**Topic:** Differential Pulse Code Modulation (DPCM)
**Question:** The primary advantage of Differential Pulse Code Modulation (DPCM) over standard Pulse Code Modulation (PCM) is:
- (A) It eliminates quantization noise completely
- (B) It exploits the correlation between adjacent samples by quantizing and encoding the prediction error rather than the original sample, reducing the required bit rate/bandwidth
- (C) It requires no low-pass reconstruction filter
- (D) It works without any clock synchronization
**Answer:** (B)
**Concept/Formula:** Because real-world voice and video signals change slowly between successive samples, the difference (prediction error $e[n] = x[n] - \hat{x}[n]$) has a much smaller dynamic range than $x[n]$, allowing fewer bits per sample (e.g., 4 bits in DPCM vs 8 bits in PCM) for identical fidelity.

---

### Q-DCF-012 `[GATE-EC-2015]` 🟡 Moderate
**Topic:** Error Control Coding — Linear Block Codes & Hamming Distance
**Question:** A linear block code has a minimum Hamming distance $d_{min} = 5$. The maximum number of bit errors this code can guarantee to **detect** ($s$) and **correct** ($t$) are respectively:
- (A) $s = 4,\ t = 2$
- (B) $s = 5,\ t = 2$
- (C) $s = 2,\ t = 1$
- (D) $s = 5,\ t = 5$
**Answer:** (A)
**Concept/Formula:**
- Error Detection condition: $d_{min} \ge s + 1 \implies s = d_{min} - 1 = 5 - 1 = 4\text{ bits}$.
- Error Correction condition: $d_{min} \ge 2t + 1 \implies 2t \le 5 - 1 = 4 \implies t = 2\text{ bits}$.

---

### Q-DCF-013 `[ISRO-EC/EE-2019]` 🟢 Easy
**Topic:** Optical Detectors — PIN vs APD
**Question:** In an optical fiber receiver, an Avalanche Photodiode (APD) is chosen over a PIN photodiode when:
- (A) High sensitivity is required for low-power optical signals due to APD's internal current multiplication gain
- (B) Lowest possible bias voltage is required
- (C) Zero temperature sensitivity is required
- (D) Lowest cost is the primary factor
**Answer:** (A)
**Concept/Formula:** An APD operates under high reverse bias near breakdown. Primary photocarriers trigger impact ionization, yielding internal current gain ($M \approx 50\text{–}200$), greatly improving receiver sensitivity for weak signals over long fiber spans.

---

### Q-DCF-014 `[ESE-EE/EC-2021]` 🟢 Easy
**Topic:** QPSK Modulation — Constellation & Spectral Efficiency
**Question:** In Quadrature Phase Shift Keying (QPSK), each transmitted symbol carries:
- (A) 1 bit
- (B) 2 bits
- (C) 4 bits
- (D) 8 bits
**Answer:** (B)
**Concept/Formula:** QPSK uses 4 distinct carrier phases ($45^\circ, 135^\circ, 225^\circ, 315^\circ$). $M = 4 = 2^2 \implies 2\text{ bits per symbol}$. For a given bit rate, QPSK requires only half the transmission bandwidth of BPSK ($B_{QPSK} = B_{BPSK} / 2$).

---

### Q-DCF-015 `[GATE-EC-2019]` 🟡 Moderate
**Topic:** Convolutional Codes & Viterbi Algorithm
**Question:** In digital communication systems, the standard maximum likelihood decoding algorithm for convolutional codes is the:
- (A) Viterbi Algorithm
- (B) Huffman Algorithm
- (C) RSA Algorithm
- (D) Dijkstra Algorithm
**Answer:** (A)
**Concept/Formula:** The Viterbi algorithm performs maximum likelihood decoding by finding the shortest path (minimum metric) through the trellis diagram of the convolutional encoder. Widely used in satellite and wireless links.
