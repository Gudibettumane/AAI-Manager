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

---

### Q-MPU-006 `[GATE-EE-2015]` 🟢 Easy
**Topic:** 8085 Bus Demultiplexing — ALE Signal
**Question:** In an 8085 microprocessor, the Address Latch Enable (ALE) signal is used to:
- (A) Latch the data lines $D_0 \text{ to } D_7$ during write operation
- (B) Demultiplex the lower-order address/data bus ($AD_0 \text{ to } AD_7$) to latch the lower 8 bits of the address ($A_0 \text{ to } A_7$) into an external latch (such as 74LS373)
- (C) Enable interrupt acknowledge
- (D) Indicate that CPU is in halt state
**Answer:** (B)
**Concept/Formula:** During the $T_1$ state of every machine cycle, ALE goes HIGH. The falling edge of ALE is used to clock the lower 8-bit memory address from lines $AD_0-AD_7$ into latch 74LS373, freeing the bus for data transfer during $T_2$ and $T_3$.

---

### Q-MPU-007 `[ESE-EE-2021]` 🟡 Moderate
**Topic:** 8085 Machine Cycles & T-States
**Question:** The execution of the instruction `STA 8050H` (Store Accumulator Direct) requires how many machine cycles and T-states?
- (A) 4 machine cycles, 13 T-states
- (B) 3 machine cycles, 10 T-states
- (C) 2 machine cycles, 7 T-states
- (D) 4 machine cycles, 16 T-states
**Answer:** (A)
**Concept/Formula:**
- Machine cycles:
  1. Opcode Fetch (4 T-states)
  2. Memory Read (lower address byte $50\text{H}$) (3 T-states)
  3. Memory Read (higher address byte $80\text{H}$) (3 T-states)
  4. Memory Write (write accumulator contents into $8050\text{H}$) (3 T-states)
- Total: 4 Machine Cycles, $4 + 3 + 3 + 3 = 13\text{ T-states}$.

---

### Q-MPU-008 `[GATE-EE-2018]` 🟢 Easy
**Topic:** Stack Pointer Operations — PUSH and POP
**Question:** If the Stack Pointer (SP) of an 8085 microprocessor is initially loaded with $2099\text{H}$, after the execution of the instruction `PUSH B`, the new content of SP will be:
- (A) $2097\text{H}$
- (B) $209\text{B}\text{H}$
- (C) $2098\text{H}$
- (D) $2099\text{H}$
**Answer:** (A)
**Concept/Formula:**
- The stack in 8085 grows downwards (towards lower memory addresses).
- `PUSH` decrements SP by 2:
  - SP is decremented $\implies 2098\text{H}$ (high byte $B$ stored).
  - SP is decremented again $\implies 2097\text{H}$ (low byte $C$ stored).
- Therefore, new SP = $2097\text{H}$.
- `POP` retrieves the bytes and increments SP by 2.

---

### Q-MPU-009 `[ISRO-EE-2019]` 🟢 Easy
**Topic:** Direct Memory Access (DMA) — HOLD and HLDA
**Question:** In an 8085 microprocessor, high-speed data transfer between a peripheral and memory without CPU intervention (DMA) is initiated by the DMA controller using which handshake pins?
- (A) HOLD and HLDA
- (B) READY and WAIT
- (C) RESET IN and RESET OUT
- (D) SID and SOD
**Answer:** (A)
**Concept/Formula:**
- DMA controller (e.g., 8237/8257) asserts **HOLD** HIGH.
- The 8085 finishes the current machine cycle, releases control of address and data buses (tri-states them), and asserts **HLDA (Hold Acknowledge)** HIGH to let the DMA controller drive the buses directly.

---

### Q-MPU-010 `[ESE-EE-2019]` 🟡 Moderate
**Topic:** 8085 Addressing Modes
**Question:** Identify the addressing mode used in the instruction `LDAX B`:
- (A) Register addressing
- (B) Direct addressing
- (C) Register Indirect addressing
- (D) Immediate addressing
**Answer:** (C)
**Concept/Formula:**
- `LDAX B` copies data into Accumulator from the memory location whose 16-bit address is held in register pair BC.
- Since the address is specified indirectly through a register pair, it is **Register Indirect Addressing**.
- Contrast with `LDA 2000H` (Direct) and `MVI A, 35H` (Immediate).

---

### Q-MPU-011 `[GATE-EC/EE-2020]` 🟡 Moderate
**Topic:** 8086 Microprocessor Architecture — Segmentation & Physical Address
**Question:** In the 8086 microprocessor, if the Code Segment register $CS = 348A\text{H}$ and the Instruction Pointer $IP = 4214\text{H}$, the 20-bit physical memory address generated is:
- (A) $38AB4\text{H}$
- (B) $769E\text{H}$
- (C) $38AC4\text{H}$
- (D) $348E4\text{H}$
**Answer:** (A)
**Concept/Formula:**
- Physical Address formula: $\text{Physical Address} = (\text{Segment Base} \times 10\text{H}) + \text{Offset}$.
- $CS \times 10\text{H} = 348A0\text{H}$.
- Offset $IP = 04214\text{H}$.
- Sum: $348A0\text{H} + 04214\text{H} = 38AB4\text{H}$.

---

### Q-MPU-012 `[ESE-EE-2018]` 🟢 Easy
**Topic:** 8086 Pipelining & Architecture
**Question:** The 8086 microprocessor achieves internal instruction pipelining by dividing its CPU architecture into two independent functional units:
- (A) Control Unit (CU) and Arithmetic Logic Unit (ALU)
- (B) Bus Interface Unit (BIU) and Execution Unit (EU)
- (C) Fetch Unit and Writeback Unit
- (D) Memory Management Unit and Cache Controller
**Answer:** (B)
**Concept/Formula:**
- **BIU (Bus Interface Unit):** Fetches instructions from memory and stores them in a 6-byte instruction prefetch queue; handles bus cycles.
- **EU (Execution Unit):** Decodes and executes instructions fetched from the queue simultaneously. This overlapped fetch-execute cycle forms instruction pipelining.

---

### Q-MPU-013 `[GATE-EE-2017]` 🟡 Moderate
**Topic:** Interrupt Masking — SIM and RIM Instructions
**Question:** In the 8085 microprocessor, which instruction is used to set the mask bits for interrupts RST 7.5, RST 6.5, and RST 5.5, and also to transmit serial data via the SOD line?
- (A) RIM (Read Interrupt Mask)
- (B) SIM (Set Interrupt Mask)
- (C) EI (Enable Interrupt)
- (D) DI (Disable Interrupt)
**Answer:** (B)
**Concept/Formula:**
- **SIM:** Interprets contents of Accumulator to mask/unmask RST 7.5, 6.5, 5.5, reset the RST 7.5 flip-flop, and output bit 7 onto the Serial Output Data (SOD) pin if SOD enable bit 6 is 1.
- **RIM:** Reads interrupt pending status, current mask status, and serial bit at Serial Input Data (SID) pin into Accumulator.

---

### Q-MPU-014 `[ISRO-EE-2020]` 🟢 Easy
**Topic:** Programmable Interval Timer — 8254/8253
**Question:** The 8254 Programmable Interval Timer contains:
- (A) Three independent 16-bit counters, each capable of operating in 6 different modes at clock inputs up to 10 MHz
- (B) Two 8-bit counters only
- (C) Four 32-bit registers
- (D) One 24-bit down-counter
**Answer:** (A)
**Concept/Formula:**
- 8254 has Counter 0, Counter 1, Counter 2 (each 16 bits).
- 6 operating modes: Mode 0 (Interrupt on terminal count), Mode 1 (Hardware retriggerable one-shot), Mode 2 (Rate generator), Mode 3 (Square wave generator), Mode 4 (Software triggered strobe), Mode 5 (Hardware triggered strobe).

---

### Q-MPU-015 `[ESE-EE-2021]` 🟢 Easy
**Topic:** Priority Interrupt Controller — 8259
**Question:** An 8259 Programmable Interrupt Controller (PIC) chip can handle up to 8 vectored priority interrupts. By cascading multiple 8259 chips in a master-slave configuration, the total number of vectored interrupts can be expanded up to:
- (A) 16
- (B) 32
- (C) 64
- (D) 128
**Answer:** (C)
**Concept/Formula:** One master 8259 can connect to 8 slave 8259 chips (one on each interrupt line $IR_0-IR_7$). Since each slave handles 8 interrupts, total interrupts = $8 \times 8 = 64$.
