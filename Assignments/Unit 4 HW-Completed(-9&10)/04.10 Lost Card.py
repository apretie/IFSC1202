lost = int(input("Enter Number of Cards: "))
total = 0
#x =  1
#y = 0
for t in range(1, lost +1):
    total += 1
for l in range(1, lost):
    x += 1
    card = int(input("Enter Card: "))
    for i in range(1, x):
        #card = int(input("Enter Card: "))
        y += card


z = x - y

print("Missing Card: {}".format(z))
