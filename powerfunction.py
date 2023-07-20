def power_modulo(A, B, C):
    if B == 0:
        return 1 % C

    result = 1
    base = A % C

    while B > 0:
        if B % 2 == 1:
            result = (result * base) % C

        B //= 2
        base = (base * base) % C

    return result
A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
C = int(input("Enter the value of C: "))
print(power_modulo(A,B,C))