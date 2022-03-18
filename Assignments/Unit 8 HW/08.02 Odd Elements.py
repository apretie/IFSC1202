value = input(str("Enter Values Separated by Spaces: "))
vlist = value.split()
for i in range(len(vlist)):
    vlist[i] = int(vlist[i])
for i in range(len(vlist)):
    if vlist[i] % 2 != 0:
        print(vlist[i])
