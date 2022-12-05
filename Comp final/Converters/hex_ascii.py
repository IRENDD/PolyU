# Hex to Decimal
def hexTodec(num):
    decimal = 0
    for i in range(len(num)):
        if num[i] >= 'A' and num[i] <= 'F':
            decimal += int(ord(num[i]) - 55) * 16 ** (len(num) - 1 - i)
        else:
            decimal += int(ord(num[i]) - 48) * 16 ** (len(num) - 1 - i)
    return decimal

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
        
    return str(''.join(hexDeciNum[::-1]))

# Hex to ASCII
def hex2ascii(hexx):
    ascii = ""
    
    for i in range(0, len(hexx), 2):
        part = hexx[i : i + 2]
        decimal = hexTodec(part)   
        ascii += chr(decimal)
    
    return ascii

# ASCII to Hex
def ascii2hex(ascii):
    hexx = ""
    
    for i in ascii:
        decimal = int(ord(i))
        hexx += decTohex(decimal)
    
    return hexx

hexx = input("Enter: ")

print(hex2ascii(hexx))