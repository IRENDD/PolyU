# octal -> decimal -> hex
# hex -> decimal -> octal

# Decimal to Hex
def decTohex(num):
    hexDeciNum = []
    i = 0
    
    while num != 0:
        temp = num % 16

        if temp < 10:
            hexDeciNum.append(chr(temp + 48))
            i += 1
        else:
            hexDeciNum.append(chr(temp + 55))
            i += 1     
        num = int(num / 16)
        
    return ''.join(hexDeciNum[::-1])

# Hex to Decimal
def hexTodec(num):
    decimal = 0
    for i in range(len(num)):
        if num[i] >= 'A' and num[i] <= 'F':
            decimal += int(ord(num[i]) - 55) * 16 ** (len(num) - 1 - i)
        else:
            decimal += int(ord(num[i]) - 48) * 16 ** (len(num) - 1 - i)
    return decimal

# Decimal to Octal
def dec2oct(num):
    octal = []

    while num != 0:
        octal.append(num % 8)
        num = int(num / 8)
    
    return int(''.join(map(str, octal[::-1])))

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

# Hex to Octal
def hex2oct(num):
    decimal = hexTodec(num)
    return dec2oct(decimal)

# Octal to Hex
def oct2hex(num):
    decimal = oct2dec(num)
    return decTohex(decimal)


print(hex2oct("2F"))
print(oct2hex(51))