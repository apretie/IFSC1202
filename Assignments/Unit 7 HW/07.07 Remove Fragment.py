x = str(input("Enter a string: "))
first = x.find("h")
last = x.rfind("h")
print(x[:first] + x[last + 1:])
#Prompt for a string that contains the letter "h" at least two times
# In the string, remove the first and last occurance of the letter "h" as well as all the characters between them, 
# then print the result.
# Example: Enter a string: ah2h3hb
#ab