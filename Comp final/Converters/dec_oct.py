# Octal to Decimal
def oct2dec(num):
    decimal = 0
    base = 1
    
    while num:
        temp = num % 10
        decimal += temp * base
        base = base * 8
        num = int(num / 10)
        
    return decimal

# Decimal to Octal
def dec2oct(num):
    octal = []

    while num != 0:
        octal.append(num % 8)
        num = int(num / 8)
    
    return int(''.join(map(str, octal[::-1])))

    # for i in range(len(octal) - 1, -1, -1):
    #   print(octal[i], end = "")

octal = int(input("Octal: "))

print(oct2dec(octal))

num = int(input("Decimal: "))

print(dec2oct(num))