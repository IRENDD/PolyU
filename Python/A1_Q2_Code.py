# Made By Ilyas Akramov. 2296786D
R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))

M = []
freq = {}

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


# Counting frequencies in the matrix using a dictionary 
# Extracting lists from the matrix
for lis in M:
    # Extracting numbers from the list 
    for item in lis:
        if(item in freq):
            freq[item] += 1
        else:
            freq[item] = 1 

#print(freq)
print("The most frequent value in the matrix is: " + str(max(freq, key=freq.get)))    


