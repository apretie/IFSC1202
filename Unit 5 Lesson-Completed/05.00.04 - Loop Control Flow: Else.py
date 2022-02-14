#You can write an else:* 
# statement after a loop body 
# which is executed once after the end of the loop.

i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('Loop ended, i =', i)
#The else statement after a loop only has sense when used in combination with the instruction break. 
# If during the execution of the loop Python encounters break, 
    #it immediately stops the loop execution and exits out of it. 
#In this case, the else: branch is not executed. 
# So, break is used to abort the loop execution during the middle of any iteration.