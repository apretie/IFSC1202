n1 = int(input("Enter a Number (zero to quit): "))
n2 = 0
tmp_max, max = 0, 0
tmp_index, index = 0, 1
#why was 7 being read as the maximum when it was 9?
# cause 7 8 9 :)
while n1 != 0:
    tmp_max = n11
    tmp_index += 1
    if tmp_max > max:
        max, index = tmp_max, tmp_index
    n2 = n1
    n1 = int(input("Enter a Number (zero to quit): "))
print("Maximum: {}".format(max))
print("Index of Maximum: {}".format(index))