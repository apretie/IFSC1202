#def defines and creates a function
def factorial(n):
    res = 1  #res means result
    for i in range(1, n + 1):
        res *= i
    return res

print(factorial(3))