words = str(input("Enter a String: "))
space = words.find(" ")
firstword = words[:space ]
secondword = words[space:]
#interchange = secondword + " " + firstword
print(secondword + " " + firstword)
#exactly 2 words separated by a space 
#print a new String w/ first a second word positions Swapped