# Open a file for reading, remember to specify the folder if not just in root folder IFSC1202
demotextfile = open("Unit 6 Lesson/06.00.00 DemoText.txt", "r")
# Read the entire contents of the file into a single string
x = demotextfile.read("Unit 6 Lesson/06.00.00 DemoText.txt")
# Print the contents - Note the embedded linefeeds
print(demotextfile)
# Close the file
demotextfile.close()