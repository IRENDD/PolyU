# Adjusted List to Adjusted Matrix
def adjListMatrix(AdjustListA):
    final = []
    mx = -9999999

    for element in AdjustListA:
        for edge in element:
            id = ord(edge) - 65
            mx = max(id, mx)


    for element in AdjustListA:
        temp = []
        for node in range(mx + 1):
            isFound = 0
            for edge in element:
                if edge == chr(node + 65):
                    isFound = 1
            if isFound == 1:
                temp.append(1)
            else:
                temp.append(0)
        final.append(temp)
    
    return final

# Adjusted Matrix to Adjusted List
def adjMatrixList(MatrixAdjustA):
    final = []
    
    for element in MatrixAdjustA:
        temp = []
        for edge in range(len(element)):
            if element[edge] == 1:
                temp.append(chr(edge + 65))
        final.append(temp)
    
    return final
        

AdjustListA = eval(input("Enter adjusted list: "))
MatrixAdjustA = eval(input("Enter adjusted matrix: "))

print(adjListMatrix(AdjustListA))
print(adjMatrixList(MatrixAdjustA))
