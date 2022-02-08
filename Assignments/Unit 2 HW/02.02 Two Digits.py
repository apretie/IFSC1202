from math import floor
num = int(input("Enter a Number: "))
one = format(num % 10)
ten = format(num / 10)
ten = floor(ten)
print("Ones Digit: " + one)
print("Tens Digit: " + ten)
