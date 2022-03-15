word = str(input("Enter a string: "))
num = word.count("f")
if num > 1:
    word = word.replace("f","a",1)
    next = word.find("f")
    print(next)
elif num == 1:
    print("One f")
else:
    print("Zero f")
# determine if string contains an f
# if the letter "f" is in the second location print index
#If the string contains the letter "f" only once, then print "One f".
#If the string does not contain the letter "f", then pring "Zero f".