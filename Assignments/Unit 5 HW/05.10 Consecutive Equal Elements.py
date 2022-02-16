n1 = int(input("Enter a Number (zero to quit): "))
n2 = 0
tmp_max, max = 0, 0
tmp_count, count = 1, 1
while n1 != 0:
    if n1 == n2:
        tmp_max = n1
        tmp_count += 1
        if tmp_count > count:
            max, count = tmp_max, tmp_count
            tmp_count = 1
    n2 = n1
    n1 = int(input("Enter a Number (zero to quit): "))
print("{} repeated {} times".format(max, count))