x = int(input("First Number: "))
y = int(input("Second Number: "))
z = int(input("Third Number: "))
if x <= y and x <= z:
    print(x)
elif y <= x and y <= z:
    print(y)
else:
    print(z)
