n = int(input("Enter N: "))  #prompt 
x = int(n/2 + 1)  #x is the prompt/2, x is max range
for i in range(2, x):
    if int(n % i != 0):
        print("PRIME")
    else:
        print("COMPOSITE")
                                                   