#Here's another use case of the while loop to determine the number of digits of an integer n.

n = int(input("Enter a Number:"))
length = 0
while n > 0:
    n //= 10  # this is equivalent to n = n // 10
    length += 1
print(length)
#On each iteration we cut the last digit of the number using integer division by 10 (n //= 10).
#In the variable length we count how many times we did that.