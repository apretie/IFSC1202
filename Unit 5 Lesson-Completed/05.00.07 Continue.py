#Another instruction used to control the loop execution is continue. 
#If Python meets continue somewhere in the middle of the loop iteration, 
    #it skips all the remaining instructions 
    #and proceeds to the next iteration.

for num in range(2, 10):
   if num % 2 == 0:
       print("Found an even number", num)
       continue
   print("Found an odd number", num)
