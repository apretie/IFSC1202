prompt = int(input("Enter Number: "))
n = 1
z = 0
for i in range(1, prompt + 1):
    n *= i
    z += n

print("Sum of Factorials: {}".format(z))