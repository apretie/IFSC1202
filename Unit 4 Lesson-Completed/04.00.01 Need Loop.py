#Quite often programs need to repeat some block several times. 
# That's where loops come in handy. To sum first 5 numbers, 
    #for sure you can write something like what you see in the code section.
isum = 0
isum = isum + 1
isum = isum + 2
isum = isum + 3
isum = isum + 4
isum = isum + 5
print(isum)
# separating using print function
print(1, 2, 3)
print(4, 5, 6)
print(1, 2, 3, sep=", ", end=". ")
print(4, 5, 6, sep=", ", end=". ")
print()
print(1, 2, 3, sep="", end=" -- ")
print(4, 5, 6, sep=" * ", end=".")
#