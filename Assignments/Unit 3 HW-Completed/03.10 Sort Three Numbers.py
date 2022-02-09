x = int(input("First Number: "))
y = int(input("Second Number: "))
z = int(input("Third Number: "))

if x <= y <= z:
    print(x, y, z)
elif x <= z <= y:
    print(x, z, y)
elif y <= z <= x:
    print(y, z, x)
elif y <= x <= z:
    print(y, x, z)
elif z <= y <= x:
    print(z, y, x)
else:
    print(z, x, y)


# <= can go in the test line not just print