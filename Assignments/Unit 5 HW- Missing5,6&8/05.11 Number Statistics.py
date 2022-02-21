count = 0
sum = float(0.0)
avg = float(0.0)
min = float(0.0)
max = float(0.0)
tmp_min = float(0.0)
tmp_max = float(0.0)
n1 = int(input("Enter a Value (zero to quit): "))
n2 = 1
while n1 != 0:
    count += 1
    sum += n1
    avg = sum / count
    if (n1 <= n2) or (tmp_min == 0):
        tmp_min = float(n1)
    if n1 > tmp_max:
        tmp_max = float(n1)
    min = tmp_min
    max = tmp_max
    n2 = n1
    n1 = int(input("Enter a Number (zero to quit): "))
print("Count:  ", count)
print("Sum:    ", sum)
print("Average:", avg)
print("Minimum:", min)
print("Maximum:", max)