def print_list(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ') 
        print()
def swap_columns(a, i, j):
    for row in range(len(a)):
        tmp = a[row][i]
        a[row][i] = a[row][j]
        a[row][j] = tmp
    return(a)

a = []
numfile = open("/workspace/IFSC1202/Text Files/09.02 NumbersList.txt", 'r') 
num = numfile.readline() 

while num != "":
    y = num.split(" ")
    for i in range(len(y)):
        y[i] = int(y[i]) 
    a.append(y)
    num = numfile.readline()
numfile.close()

print_list(a)
swap = input("Enter the columns to swap: ")
s = []
s = swap.split(" ")
i = int(s[0])
j = int(s[1]) 

swap_columns(a, i, j)
print_list(a)









#HW Output:
#11 12 13 14 15 16 
#21 22 23 24 25 26 
#31 32 33 34 35 36 
#41 42 43 44 45 46 
#Enter the columns to swap: 0 5
#16 12 13 14 15 11 
#26 22 23 24 25 21 
#36 32 33 34 35 31 
#46 42 43 44 45 41 