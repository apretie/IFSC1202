prompt = 1
t = 0
while prompt != 0:
    prompt = int(input("Enter a number zero to quit: "))
    t += prompt
print("Sum: {}".format(t))
