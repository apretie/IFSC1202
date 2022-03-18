value = input(str("Enter Values Separated by Spaces: "))
vlist = value.split()

for i in range(len(vlist)):
    vlist[i] = int(vlist[i])
if (len(vlist)) % 2 == 0:
    end = (len(vlist))
else:
    end = (len(vlist)-1)
for i in range(0,end,2):
    hold = vlist[i]
    print(hold)
    vlist[i] = vlist[i+1]
    print(vlist[i])
    vlist[i+1] = hold
    print(vlist[i+1])

print("Swapped Values: ",end="")
for i in range(len(vlist)):
    print(str(vlist[i]) + " ",end="")