#Before you can access a file, you must open it by name using the open() statement. 
# If you open "06.00.00 DemoText.txt", it is assumed that the file is in the root of the file system. 
# If the file is in a folder, say "IFSC1202", then you would specify "IFSC1202/06.00.00 DemoText.txt".

demofile = open("06.00.00 DemoText.txt")
#same as:
demofile = open("06.00.00 DemoText.txt", "rt")

#Because "r" for read, and "t" for text are the default values, you do not need to specify them. 
#Note: Make sure the file exists, or else you will get an error.

#The .read() method is used to read an entire file. 
#The all lines of the contents (including any linefeeds) are placed in a string.

x = demotextfile.read()

#You can display the contents of the file by simply printing it. 
#Note: what happens when a linefeed is printed...output is advanced to the beginning of the new line.

print(x)
#When you are finished with the file, you should close the file to release all of the resources associated with the file.

demotextfile.close()
#putting it all together in 06.00.04 Read Entire File.py
