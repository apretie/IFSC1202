a = int(input("Enter Classroom A: "))
b = int(input("Enter Classroom B: "))
c = int(input("Enter Classroom C: "))
a = a // 2 + a % 2
b = b // 2 + b % 2
c = c // 2 + c % 2
print(a + b + c)