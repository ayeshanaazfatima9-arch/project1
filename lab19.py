a = 60   # binary: 0b111100
b = 13   # binary: 0b011000



print("Bitwise AND: 60 & 13 =", a & b, "(binary:", bin(a & b) + ")")
print("Bitwise OR:  60 | 13 =", a | b, "(binary:", bin(a | b) + ")")
print("Bitwise XOR: 60 ^ 13 =", a ^ b, "(binary:", bin(a ^ b) + ")")

print("Bitwise NOT: ~60 =", ~a, "(binary:", bin(~a) + ")")

print("Bitwise Left Shift:  60 << 2 =", a << 2, "(binary:", bin(a << 2) + ")")
print("Bitwise Right Shift: 60 >> 2 =", a >> 2, "(binary:", bin(a >> 2) + ")")