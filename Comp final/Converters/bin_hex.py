# hex -> decimal -> binary
# binary -> decimal -> hex

# Binary to Decimal
def binTodec(num):
    binary = int(num)
    decimal = 0
    i = 0
    
    while binary != 0:
        decimal = decimal + (binary % 10) * (2 ** i)
        binary //= 10
        i += 1
    
    return decimal

# Decimal to Binary
def decTobin(num):
    if num < 0:
        return 'Must be only positive integer'
    elif num == 0:
        return '0'
    else:
        return decTobin(num // 2) + str(num % 2)


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

# Binary to Hex
def binTohex(num):
    decimal = binTodec(num)
    return decTohex(decimal)

# Binary to Hex
def hexTobin(num):
    decimal = hexTodec(num)
    return decTobin(decimal)

print(hexTobin('2F'))
