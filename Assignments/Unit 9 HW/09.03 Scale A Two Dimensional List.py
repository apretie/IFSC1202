def print_list(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ') 
        print()
def scale_list(a, s):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] *= s
    return(a)

a = []
numfile = open("/workspace/IFSC1202/Text Files/09.03 NumbersList.txt", 'r') 
num = numfile.readline() 

while num != "":
    y = num.split(" ")
    for i in range(len(y)):
        y[i] = int(y[i]) 
    a.append(y)
    num = numfile.readline()
numfile.close()

print_list(a)
s = int(input("Enter scale value: "))
scale_list(a, s)
print_list(a)



#HW Output:
#11 12 
#21 22 23 
#31 32 33 34 
#Enter scale value: 2
#22 24 
#42 44 46 
#62 64 66 68 