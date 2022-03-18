value = input(str("Enter Values Separated by Spaces: "))
vlist = value.split()
iofmax = 0
tmp_max, max = 0, 0
for i in range(len(vlist)):
    vlist[i] = int(vlist[i])
for i in range(len(vlist)):
    tmp_max = vlist[i]
    if tmp_max > max:
        max = tmp_max
        iofmax = i
print("Largest Value: {}".format(max))
print("Index of Largest Value: {}".format(iofmax))


#Load the values into a list.
#Determine the element in the list with the largest value.
#Print the value of the largest element and then the index number.
#If the highest element is not unique, print the index of the first instance.
#Do not use the list or string functions or methods for this assignment (except the .split() method).
#Do not use the for x in y iterator; use for x in range(n)

#Hw Output: 
#Enter Values Separated by Spaces: 1 2 3 2 1
#Largest Value: 3
#Index of Largest Value: 2