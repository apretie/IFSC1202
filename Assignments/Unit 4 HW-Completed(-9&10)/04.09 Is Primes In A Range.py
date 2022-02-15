a = int(input("Enter A: "))
b = int(input("Enter B: "))
n = a
x = int(n/2 + 1)

for i in range(a, b + 1):
    n += 1
    for k in range(2, x):
        if int(n % 2 != 0) and int(n % 3 != 0):
         print(n)
    