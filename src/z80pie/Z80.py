class Z80:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.F = 0
        self.PC = 0x0000
        self.SP = 0xFFFF
        self.memory = bytearray(65536)  # 64 KB

    def fetch_byte(self):
        byte = self.memory[self.PC]
        self.PC += 1
        return byte

    def step(self):
        opcode = self.fetch_byte()

        if opcode == 0x3E:  # LD A, n
            self.A = self.fetch_byte()
            print(f"Loaded {hex(self.A)} into A")
        
        elif opcode == 0x06:  # LD B, n
            self.B = self.fetch_byte()
            print(f"Loaded {hex(self.B)} into B")
        
        elif opcode == 0x0E:  # LD C, n
            self.C = self.fetch_byte()
            print(f"Loaded {hex(self.C)} into C")

        elif opcode == 0x00:  # NOP
            print("No operation (NOP) executed")
            pass

        elif opcode == 0xC3:  # JP nn
            lo = self.fetch_byte()
            hi = self.fetch_byte()
            address = (hi << 8) | lo
            self.PC = address
            print(f"Jumped to {hex(address)}")

        elif opcode == 0x3C:  # INC A
            self.A = (self.A + 1) & 0xFF # Ensure A wraps around 255 + 1 (keep lower 8 bits)
            self.F = 0  # TODO: Set flags based on the new value of A
            print(f"Incremented A to {hex(self.A)}")
        
        elif opcode == 0x3D:  # DEC A
            self.A = (self.A - 1) & 0xFF # Ensure A wraps around 0 - 1 (keep lower 8 bits)
            self.F = 0  # TODO: Set flags based on the new value of A 
            print(f"Decremented A to {hex(self.A)}")
        
        elif opcode == 0xC6:  # ADD A, n
            value = self.fetch_byte()
            self.A = (self.A + value) & 0xFF # Ensure A wraps around 255 + 1 (keep lower 8 bits)
            self.F = 0  # TODO: Set flags based on the new value of A
            print(f"Added {hex(value)} to A, new value is {hex(self.A)}")

        elif opcode == 0x3A:  # LD A, (nn)
            lo = self.fetch_byte()
            hi = self.fetch_byte()
            addr = (hi << 8) | lo
            self.A = self.memory[addr]
            self.F = 0  # TODO: Set flags based on the new value of A
            print(f"Loaded A from memory[{hex(addr)}]: {hex(self.A)}")
        
        elif opcode == 0x32:  # LD (nn), A
            lo = self.fetch_byte()
            hi = self.fetch_byte()
            addr = (hi << 8) | lo
            self.memory[addr] = self.A
            print(f"Loaded memory[{hex(addr)}] with value of A: {hex(self.A)}")

        else:
            print(f"Unknown opcode: {hex(opcode)}")
            raise NotImplementedError()

