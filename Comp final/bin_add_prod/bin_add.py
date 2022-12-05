def binEqualize(binA, binB):
    n = len(binA)
    m = len(binB)
    
    tempStr = ""
    
    if n > m:
        for i in range(n - m):
            tempStr += "0"
        binB = (tempStr + binB[0:])
    else:
        for i in range(m - n):
            tempStr += "0"
        binA = (tempStr + binA[0:])
    
    return binA, binB


# Only Positive Binary Addition
def binAdd(binA, binB):
    binA, binB = binEqualize(binA, binB)
    
    carry = 0
    ans = ""
    print(binA, binB)
    
    for i in range(len(binA) - 1, -1, -1):
        sum = int(binA[i]) + int(binB[i])
        if carry == 1:
            if sum == 2:
                ans += '1'
            elif sum == 1:
                ans += '0'
            else:
                ans += '1'
                carry = 0
        else:
            if sum == 2:
                carry = 1
                ans += '0'
            elif sum == 1:
                ans += '1'
            else:
                ans += '0'
    if carry != 0:
        ans += '1'
        carry = 0
    
    ans += '0'
    
    return ans[::-1]

binA = input("Enter: ")
binB = input("Enter: ")

print(binAdd(binA, binB))