x = input("First Number: ")
y = input("Second Number: ")
z = input("Third Number: ")
#Check for all three numbers
if x == y and x == z:
    print(3)
#Check for two numbers equal
elif x == y or x == z:
    print(2)
#Check if none are equal
else: print(0)