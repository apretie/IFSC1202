value = input(str("Enter Values Separated by Spaces: "))
vlist = value.split()

for i in range(1, (len(vlist)), 2):
    print(vlist[i])
for i in range(len(vlist)):
    print(vlist[::2])

