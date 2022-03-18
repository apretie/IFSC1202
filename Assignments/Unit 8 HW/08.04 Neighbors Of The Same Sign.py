#Load the values into a list.
#Find and print the first adjacent elements which have the same sign.
#If there is no such pair, leave the output blank.
#Do not use the list or string functions or methods for this assignment (except the .split() method).
#Do not use the for x in y iterator; use for x in range(n)

#HW Output:
#Enter Values Separated by Spaces: -1 2 3 -1 -2
#2 3
#-1 -2
value = input(str("Enter Values Separated by Spaces: "))
vlist = value.split()
for i in range(len(vlist)):
    vlist[i] = int(vlist[i])
for i in range(len(vlist)):
    if (i + 1) == (len(vlist)):
        exit()
    elif vlist[i] > 0 and vlist[i+1] > 0:
        pos = str(vlist[i]) + " " + str(vlist[i+1])
        print(pos)
    elif vlist[i] < 0 and vlist[i+1] < 0:
        neg = str(vlist[i]) + " " + str(vlist[i+1])
        print(neg)

