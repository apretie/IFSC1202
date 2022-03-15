x  = str(input("Enter a string: "))
hstring = str(input("Enter a string: "))
first = hstring.find("h")
last = hstring.rfind("h")
print(hstring[last:first-1:-1])
#Prompt for a string containg the letter "h" at least two times.
#Reverse the sequence of characters between the first letter "h" and the last letter "h"
# Example: Enter a string: abch123h456hdef
#abch654h321hdef
