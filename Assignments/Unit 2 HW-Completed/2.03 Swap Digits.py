from math import floor
num = int(input("Enter a Number: "))
one = (num % 10)
ten = (num / 10)
ten = floor(ten)
print("Swapped Number: {0:1d}{1:1d}".format(one,ten))
