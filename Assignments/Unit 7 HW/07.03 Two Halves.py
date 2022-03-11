x  = str(input("Enter a string: "))
half = (len(x) +1) // 2
firsthalf = x[:half]
sechalf = x[half:]
interchange = sechalf + firsthalf
print(interchange)


#Enter a string: bigboy
#boybig
#Print a new string on a single row with the first and second halves interchanged 
#(second half first and the first half second)
#Don't use the if statement in this task.