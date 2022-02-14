#Here is a Black Jack-like example: 
    #Program reads numbers and sums them until the total gets greater or equal to 21. 
    #The input sequence ends with 0 for the program to be able to stop 
        #even if the total sum of all numbers is less than 21.
total_sum = 0
a = int(input("Enter a Number:"))
while a != 0:
    total_sum += a
    if total_sum >= 21:
        print('Total sum is', total_sum)
        break
    a = int(input("Enter a Number:"))
else:
    print('Total sum is less than 21 and is equal to ' + str(total_sum) + '.')