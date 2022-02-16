n1 = int(input("Enter a Number (zero to quit): "))
n2 = 0
tmp_max, max = 0, 0
while n1 != 0:
    tmp_max = n1
    if tmp_max > max:
        max = tmp_max
    n2 = n1
    n1 = int(input("Enter a Number (zero to quit): "))
print("Maximum: {}".format(max))