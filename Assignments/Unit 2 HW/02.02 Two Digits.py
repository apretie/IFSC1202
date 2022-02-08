from math import floor
num = int(input("Enter a Number: "))
one = (num % 10)
ten = (num / 10)
ten = floor(ten)
print("Ones Digit: {:1d}".format(one))
print("Tens Digit: {:1d}".format(ten))
