# octal -> decimal -> binary
# binary -> decimal -> octal


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

# Binary to Octal
def bin2oct(num):
    decimal = binTodec(num)
    return dec2oct(decimal)

# Octal to binary
def oct2bin(num):
    decimal = oct2dec(num)
    return decTobin(decimal)

print(bin2oct('10111'))
print(oct2bin(67))