### 8080 Emulator Opcode Checklist

| Z80 Mnemonic         | 8080 Mnemonic   | Opcode(s)                 | Status | Notes                 |
|----------------------|-----------------|---------------------------|--------|-----------------------|
| LD r, n              | MVI r, n        | 0x06,0x0E,0x16...         |        |                       |
| LD r1, r2            | MOV r1, r2      | 0x40–0x7F                 |        |                       |
| LD A, (nn)           | LDA addr        | 0x3A                      |        |                       |
| LD (nn), A           | STA addr        | 0x32                      |        |                       |
| LDAX rp (BC/DE)      | LDAX rp         | 0x0A, 0x1A                |        |                       |
| STAX rp (BC/DE)      | STAX rp         | 0x02, 0x12                |        |                       |
| LXI rp, nn           | LXI rp, nn      | 0x01,0x11,0x21,0x31       |        |                       |
| LD SP, HL            | SPHL            | 0xF9                      |        |                       |
| JP nn                | JMP addr        | 0xC3                      |        |                       |
| CALL nn              | CALL addr       | 0xCD                      |        |                       |
| RET                  | RET             | 0xC9                      |        |                       |
| INC r                | INR r           | 0x04,0x0C,0x14...         |        |                       |
| DEC r                | DCR r           | 0x05,0x0D,0x15...         |        |                       |
| INC rp               | INX rp          | 0x03,0x13,0x23,0x33       |        |                       |
| DEC rp               | DCX rp          | 0x0B,0x1B,0x2B,0x3B       |        |                       |
| ADD A, r             | ADD r           | 0x80–0x87                 |        |                       |
| ADD A, n             | ADI n           | 0xC6                      |        |                       |
| SUB r                | SUB r           | 0x90–0x97                 |        |                       |
| SUB n                | SUI n           | 0xD6                      |        |                       |
| AND r                | ANA r           | 0xA0–0xA7                 |        |                       |
| AND n                | ANI n           | 0xE6                      |        |                       |
| OR r                 | ORA r           | 0xB0–0xB7                 |        |                       |
| OR n                 | ORI n           | 0xF6                      |        |                       |
| XOR r                | XRA r           | 0xA8–0xAF                 |        |                       |
| XOR n                | XRI n           | 0xEE                      |        |                       |
| CMP r                | CMP r           | 0xB8–0xBF                 |        |                       |
| CMP n                | CPI n           | 0xFE                      |        |                       |
| RLC                  | RLC             | 0x07                      |        |                       |
| RRC                  | RRC             | 0x0F                      |        |                       |
| RAL                  | RAL             | 0x17                      |        |                       |
| RAR                  | RAR             | 0x1F                      |        |                       |
| PUSH rp              | PUSH rp         | 0xC5,0xD5,0xE5,0xF5       |        |                       |
| POP rp               | POP rp          | 0xC1,0xD1,0xE1,0xF1       |        |                       |
| XCHG                 | XCHG            | 0xEB                      |        |                       |
| XTHL                 | XTHL            | 0xE3                      |        |                       |
| PCHL                 | PCHL            | 0xE9                      |        |                       |
| IN port              | IN port         | 0xDB                      |        |                       |
| OUT port             | OUT port        | 0xD3                      |        |                       |
| HLT                  | HLT             | 0x76                      |        |                       |
| NOP                  | NOP             | 0x00                      |        |                       |
| DI                   | DI              | 0xF3                      |        |                       |
| EI                   | EI              | 0xFB                      |        |                       |
| STC                  | STC             | 0x37                      |        |                       |
| CMC                  | CMC             | 0x3F                      |        |                       |
| CMA                  | CMA             | 0x2F                      |        |                       |
| SBB r                | SBB r           | 0x98–0x9F                 |        |                       |
| SBB n                | SBI n           | 0xDE                      |        |                       |
| ADC r                | ADC r           | 0x88–0x8F                 |        |                       |
| ADC n                | ACI n           | 0xCE                      |        |                       |
| DAD rp               | DAD rp          | 0x09,0x19,0x29,0x39       |        |                       |
| RST n                | RST n           | 0xC7,0xCF...              |        |                       |
