#Determine and print the quantity of elements that are greater than both of their neighbors.
#The first and the last items of the list shouldn't be considered because they don't have two neighbors.
value = input(str("Enter Values Separated by Spaces: "))
vlist = value.split()
count = 0
for i in range(len(vlist)):
    vlist[i] = int(vlist[i])
for i in range(1,(len(vlist)-1)):
    if vlist[i] > vlist[i-1] and vlist[i] > vlist[i+1]:
        count += 1
print(count)
