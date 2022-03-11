nametxt = open("/workspace/IFSC1202/Assignments/Unit 6 HW/Text Files/", "r")
nametxt = nametxt.readline()
name = nametxt.strip(" ")


def ProperCase(s):
    x = s. lower()
    
    return s.upper
#Returns a properly cases string s by uppercasing the first character and lowercasing the rest of the string.
# Hint: use upper() and lower() methods
def RemoveNewLine(s):
#Returns a string with the NewLine Character ("\n") removed from string s
#Hint: use replace() method
def Trim(s):
    return s.strip()
#Returns a string with the leading and trailing spaces removed from string s
#Hint: use strip() method
def FirstName(s):
#Returns the first name of string s
#Hint:
# Find the first space in string s using the find() method
# Create a substring from the beginning of string s up to the first space
# Call the ProperCase() function
def LastName(s):
#Returns the last name of string s
#Hint:
# Find the last space in string s using the rfind() method
# Create a substring from the last space to the ending of sring s
# Call the ProperCase() function
def MiddleName(s):
#Returns the middlename from string s
# Hint:
# Find the first space in string s using the find() method
# Find the last space in string s using the rfind() method
# Create a substing from the first space to the last space of string s
# Call the Trim() function
# Call the ProperCase() function
# If the length of the middle name is one, then it is an initial without a period. Append a period.