#Given two integers representing the rows and columns (m×n), and subsequent m rows of n elements
#Input the number of rows and columns in the list
#Input the array
#Print the array.
#Find the index position of the maximum element and print two numbers representing the index (i×j) or the row number and the column number. 
#If there exist multiple such elements in different rows, print the one with smaller row number. 
#If there multiple such elements occur on the same row, output the smallest column number.

a = []
x = input("Enter the number of rows and columns: ")
MofN = x.split(" ")
# Convert the values from string to an integer
for i in range(len(MofN)):
    MofN[i] = int(MofN[i])

# MofN has number of rows in 0 and columns in 1
for m in range(MofN[0]):
    data = input("Input a line of data: ")
    line = data.split(" ")
    # string to int conversion
    for num in range(MofN[1]):
        line[num] = int(line[num])
    # Append the list to the two dimensional array
    a.append(line)

# Loop through each row in the two dimensional array
for i in range(len(a)):
    # Loop though each element in the list
    for j in range(len(a[i])):
        # Find the max
        max(j) then find maybe? idk"

print("The maximum value {} occured in row {} column {}".format(max,m,n))







#HW Output:
# Enter the number of rows and columns: 3 4
# Enter a line of data: 0 3 2 4
# Enter a line of data: 2 3 5 5 
# Enter a line of data: 5 1 2 3
#0 3 2 4 
#2 3 5 5 
#5 1 2 3 
#The maximum value 5 occurred in row 1 column 2