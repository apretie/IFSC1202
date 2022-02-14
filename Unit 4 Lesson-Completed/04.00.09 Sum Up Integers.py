#Remember: the maximum value in range(min_value, max_value) is not included! 
# To make i running from 1 to n inclusively, 
#   the maximum value in range() should be n + 1.

result = 0
n = 5
for i in range(1, n + 1):
    result += i
    # this ^^ is the shorthand for
    # result = result + i
print(result)