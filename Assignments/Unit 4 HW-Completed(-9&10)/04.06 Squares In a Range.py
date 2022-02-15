a = int(input("Enter A: "))
b = int(input("Enter B: "))
z = 0
for i in range(a, b + 1):
    z = i ** 2
    print("{}*{}={}".format(i, i, z))