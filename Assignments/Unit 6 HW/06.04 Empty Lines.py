inputfilename = "Unit 6 Lesson-Completed/06.00.00 DemoText.txt"
linefile = open("Assignments/Unit 6 HW/Text Files/06.04 EmptyLinesInput.txt", "r")
linesfile = open("Assignments/Unit 6 HW/Text Files/06.04 EmptyLinesOutput.txt", "w")
x = linefile.read()
y = linesfile.write()
linesfile = x
linesfile = y

# The name of the file can be a string
inputfilename = "Unit 6 Lesson-Completed/06.00.00 DemoText.txt"
outputfilename = "Unit 6 Lesson-Completed/06.00.07 NewDemoText.txt"
recordcount = 0
# Open the input file for reading
inputfile = open(inputfilename, 'r')
# Open the output file for writing
outputfile = open(outputfilename, 'w')  
# Read the first line of the input file
line = inputfile.readline()
# Read until the input is empty
while line != '':
# Write to the output file
# Note that line already contains a linefeed character,
# so we don't have to add one when we write it.
     outputfile.write(line)
     recordcount += 1
# Read the next line of the input file
     line = inputfile.readline()
# End of File on input file
# Close both files
inputfile.close()
outputfile.close()
print("{} records written".format(recordcount))