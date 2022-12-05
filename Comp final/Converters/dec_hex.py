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

# Hex to Decimal
def hexTodec(num):
    decimal = 0
    for i in range(len(num)):
        if num[i] >= 'A' and num[i] <= 'F':
            decimal += int(ord(num[i]) - 55) * 16 ** (len(num) - 1 - i)
        else:
            decimal += int(ord(num[i]) - 48) * 16 ** (len(num) - 1 - i)
    return decimal

hex = input("Hex: ")

print(hexTodec(hex))