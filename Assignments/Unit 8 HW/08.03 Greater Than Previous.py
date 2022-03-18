value = input(str("Enter Values Separated by Spaces: "))
vlist = value.split()
for i in range(len(vlist)):
    vlist[i] = int(vlist[i])
for i in range(len(vlist)):
    if (i + 1) == (len(vlist)):
        exit()
    elif vlist[i+1] > vlist[i]:
        print(vlist[i+1])

#Print all of the elements that are greater than the previous element.
#Do not use the list or string functions or methods for this assignment 
#(except the .split() method).
#Do not use the for x in y iterator; use for x in range(n)