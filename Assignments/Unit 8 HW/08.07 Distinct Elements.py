#Print the number of distinct elements in the list.

#Hw Output:
#Enter Values Separated by Spaces: 1 2 2 3 3 3
#Number of Distinct Elements: 3

value = input(str("Enter Values Separated by Spaces: "))
vlist = value.split()
num, count = 0, 0
for i in range(len(vlist)):
    vlist[i] = int(vlist[i])
for i in range(len(vlist)):
    if num != vlist[i]:
        count += 1
    num = vlist[i]

print("Number of Distinct Elements: {}".format(count))