# Adjusted List to Adjusted Matrix with Weights
def adjWeight_listMatrix(AdjencyList):
    final = []
    mx = -999999

    for element in AdjencyList:
        for edge in element:
            id = ord(str(edge[0])) - 65
            mx = max(id, mx)

    for element in AdjencyList:
        temp = []
        for node in range(mx + 1):
            isFound = 0
            num = 0
            for edge in element:
                if str(edge[0]) == chr(node + 65):
                    isFound = 1
                    num = int(edge[1])
            if isFound == 1:
                temp.append(num)
            else:
                temp.append(0)
        final.append(temp)
    
    return final

# Adjusted List to Adjusted Matrix with Weights
def adjWeight_matrixList(AdjencyMatrix):
    final = []
    
    for element in AdjencyMatrix:
        temp = []
        for edge in range(len(element)):
            if element[edge] != 0:
                temp.append((chr(edge + 65), element[edge]))
        final.append(temp)
    
    return final

AdjencyList = eval(input("Enter adjusted list: "))
print(adjWeight_listMatrix(AdjencyList))

AdjencyMatrix = eval(input("Enter adjusted list: "))
print(adjWeight_matrixList(AdjencyMatrix))
