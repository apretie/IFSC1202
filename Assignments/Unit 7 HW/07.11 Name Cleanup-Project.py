def ProperCase(s):
    s = s.lower()
    return s[0:1].upper() + s[1:].lower()

#Returns a properly cases string s by uppercasing the first character and lowercasing the rest of the string.
# Hint: use upper() and lower() methods

def RemoveNewLine(s):
    return s.replace("\n","")

#Returns a string with the NewLine Character ("\n") removed from string s
#Hint: use replace() method

def Trim(s):
    return s.strip(" ")

#Returns a string with the leading and trailing spaces removed from string s
#Hint: use strip() method

def FirstName(s):
    findex = s.find(" ")
    firstn = s[:findex]
    fname = ProperCase(firstn)
    return fname

#Returns the first name of string s
#Hint:
# Find the first space in string s using the find() method
# Create a substring from the beginning of string s up to the first space
# Call the ProperCase() function

def LastName(s):
    lindex = s.rfind(" ")
    lastn = s[lindex+1:]
    lname = ProperCase(lastn)
    return lname
#Returns the last name of string s
#Hint:
# Find the last space in string s using the rfind() method
# Create a substring from the last space to the ending of sring s
# Call the ProperCase() function

def MiddleName(s):
    findex = s.find(" ")
    lindex = s.rfind(" ")
    middlen = s[findex:lindex]
    Trim(middlen)
    mname = ProperCase(middlen)
    if len(middlen) == 1:
        middlename += "."  
    return middlen
openfile = open("/workspace/IFSC1202/Assignments/Unit 7 HW/07.11 Names.txt","r")
nametxt = openfile.readlines()


#Returns the middlename from string s
# Hint:
# Find the first space in string s using the find() method
# Find the last space in string s using the rfind() method
# Create a substing from the first space to the last space of string s
# Call the Trim() function
# Call the ProperCase() function
# If the length of the middle name is one, then it is an initial without a period. Append a period.

print("{:<10} {:<10} {:<10}".format("First","Middle","Last"))
print("{0:-<10} {0:-<10} {0:-<10}".format("-"))


#while f != "":
for f in nametxt:
    f = Trim(f)
    f = RemoveNewLine(f)
    print("{0:<10} {1:<10} {2:<10}".format(FirstName(f),MiddleName(f),LastName(f)))

nametxt.close()