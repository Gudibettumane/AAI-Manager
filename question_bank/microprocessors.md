# AUTHENTIC QUESTION BANK: MICROPROCESSORS & MICROCOMPUTERS
*Sources: GATE EE/EC, ESE Prelims, ISRO EE, State AE*

---

### Q-MPU-001 `[GATE-EE-2019]` 🟢 Easy
**Topic:** 8085 Interrupts — Priority & Vector Addresses
**Question:** Which of the following hardware interrupts in the 8085 microprocessor is non-maskable and highest in priority?
- (A) INTR
- (B) RST 7.5
- (C) TRAP (RST 4.5)
- (D) RST 6.5
**Answer:** (C)
**Concept/Formula:**
- Priority order: **TRAP** > **RST 7.5** > **RST 6.5** > **RST 5.5** > **INTR**.
- TRAP is edge and level sensitive and cannot be masked by software (non-maskable).
- Restart vector address formula: $\text{Vector Address} = (\text{RST Number}) \times 8$ in hexadecimal:
  - TRAP (RST 4.5) $\implies 4.5 \times 8 = 36 = 0024\text{H}$.
  - RST 5.5 $\implies 5.5 \times 8 = 44 = 002\text{C}\text{H}$.
  - RST 6.5 $\implies 6.5 \times 8 = 52 = 0034\text{H}$.
  - RST 7.5 $\implies 7.5 \times 8 = 60 = 003\text{C}\text{H}$.

---

### Q-MPU-002 `[ESE-EE-2020]` 🟡 Moderate
**Topic:** 8085 Instruction Set & Flags
**Question:** In an 8085 microprocessor, after the execution of the instruction `XRA A` (Exclusive OR Accumulator with itself):
- (A) The accumulator content becomes $00\text{H}$, Zero flag is set ($Z = 1$), and Carry flag is cleared ($CY = 0$)
- (B) The accumulator content remains unchanged and $Z = 0$
- (C) The accumulator content becomes $\text{FF}\text{H}$ and $CY = 1$
- (D) Parity flag is reset ($P = 0$)
**Answer:** (A)
**Concept/Formula:**
- $A \oplus A = 00\text{H}$.
- Since the result is zero, the Zero flag is set ($Z = 1$).
- Logic operations clear the Carry flag ($CY = 0$).
- Parity of $00\text{H}$ has an even number of 1s (zero 1s) $\implies P = 1$ (Even parity).

---

### Q-MPU-003 `[GATE-EE-2016]` 🟡 Moderate
**Topic:** Memory Interfacing — Address Decoding
**Question:** An 8085-based system has a $4\text{ KB}$ EPROM chip mapped starting at memory address $8000\text{H}$. The end address of this EPROM is:
- (A) $8\text{FFF}\text{H}$
- (B) $9\text{FFF}\text{H}$
- (C) $8\text{E00}\text{H}$
- (D) $8\text{7FF}\text{H}$
**Answer:** (A)
**Concept/Formula:**
- $4\text{ KB} = 4 \times 1024 = 4096\text{ bytes} = 2^{12}\text{ bytes}$.
- Requires 12 address lines ($A_0 \text{ to } A_{11}$).
- Size in hex: $4096 - 1 = 4095 = 0\text{FFF}\text{H}$.
- End Address = Start Address + Size $- 1 = 8000\text{H} + 0\text{FFF}\text{H} = 8\text{FFF}\text{H}$.

---

### Q-MPU-004 `[ESE-EE-2018]` 🟢 Easy
**Topic:** Memory-Mapped I/O vs I/O-Mapped I/O
**Question:** In memory-mapped I/O scheme:
- (A) 16-bit addresses are used for I/O devices, and all memory-reference instructions (`MOV`, `LDA`, `STA`) can access I/O ports
- (B) Only `IN` and `OUT` instructions can be used to communicate with I/O devices
- (C) The CPU can address up to 256 I/O ports only
- (D) Control signals $\overline{\text{IOR}}$ and $\overline{\text{IOW}}$ are activated
**Answer:** (A)
**Concept/Formula:**
- **Memory-Mapped I/O:** I/O ports are treated as memory locations with 16-bit addresses. Standard instructions (`MOV`, `LDA`, `STA`, `ADD M`) can be used. Reduces available memory address space, but offers versatile data manipulation.
- **I/O-Mapped (Isolated) I/O:** 8-bit port address ($00\text{H} \text{ to } \text{FF}\text{H}$, total 256 ports). Accessible ONLY via `IN` and `OUT` instructions. Uses $\overline{\text{IOR}}$ and $\overline{\text{IOW}}$ control lines.

---

### Q-MPU-005 `[ISRO-EE-2020]` 🟢 Easy
**Topic:** Programmable Peripheral Interface — 8255
**Question:** The 8255 Programmable Peripheral Interface (PPI) IC provides:
- (A) 24 programmable I/O pins organized into three 8-bit ports (Port A, Port B, Port C)
- (B) 16 programmable I/O pins organized into two 8-bit ports
- (C) 8 analog input channels
- (D) 3 independent counter/timer channels
**Answer:** (A)
**Concept/Formula:**
- 8255 has 24 I/O pins: Port A (8 bits), Port B (8 bits), Port C (8 bits, can be split into Port C Upper $PC_4-PC_7$ and Port C Lower $PC_0-PC_3$).
- Modes: Mode 0 (Basic I/O), Mode 1 (Strobed I/O with handshaking), Mode 2 (Bi-directional bus on Port A).
