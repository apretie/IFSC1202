n = int(input("Enter N: "))
x = n
zero = 0
for i in range(n):
    x = int(input("Enter Number: "))
    if x == 0:
        zero += 1
print("Number of Zeros: {}".format(zero))