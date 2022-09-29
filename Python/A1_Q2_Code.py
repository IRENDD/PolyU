R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))

M = []
freq = []

largest_num = 0
isTrue = False

for i in range(R):
    a = []
    for j in range(C):
        # Restricting user input in the given range from 0 to 255
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
    # Adding the list to a matrix
    M.append(a)
    #print(a)

# Creating an array that will count the frequency of the numbers
for i in range(0, 256):
    freq.append(0)

# Counting frequencies in the matrix
for i in range(R):
    for j in range(C):
        freq[M[i][j]] += 1

# Finding the maaximum value
for i in range(0, 256):
    if freq[i] > largest_num:
        largest_num = freq[i]

# Finding the maximum value in the matrix and printing
for i in range(R):
    for j in range(C):
        if freq[M[i][j]] == largest_num:
            largest_num = M[i][j]
            isTrue = True
    if isTrue:
        print("The most frequent value in the matrix is: " + str(largest_num))
        break
