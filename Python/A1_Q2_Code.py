from typing import Counter

R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))
M = []

for i in range(R):
    a = []
    for j in range(C):
        while True:
            try:
                num = int(input())
            except:
                print("Enter a integer input") 
            
            if num not in range(0, 256):
                print("Please enter a valid input")
            else:
                a.append(num)
                break
    M.append(a)

res = dict(sum(map(Counter, M), Counter()))
print(res)
print("The most frequent value in the matrix is: " + str(max(res, key=res.get)))    


