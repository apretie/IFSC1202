#Else branch can also be used with the for loop. 
# Example of a program:
    #reads exactly five integers but 
    # stops right when the first negative integer is met.

for i in range(5):
    a = int(input("Enter a Number:"))
    if a < 0:
        print('Met a negative number', a)
        break
else:
    print('No negative numbers met')