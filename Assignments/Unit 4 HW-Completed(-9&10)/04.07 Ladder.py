n = int(input("Enter N: "))
z = 0
for i in range(1, n + 1):
    z += 1
    for k in range(1, z + 1):
        print(k, sep="", end="")
    print()