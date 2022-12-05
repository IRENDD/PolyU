# Positive Converter 

# Decimal to Binary
def decTobin(num):
    if num < 0:
        return 'Must be only positive integer'
    elif num == 0:
        return '0'
    else:
        return decTobin(num // 2) + str(num % 2)

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

n = int(input("Decimal: "))

print(decTobin(n))

print(binTodec(decTobin(n)))