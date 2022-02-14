#If the break and continue are placed inside several nested loops, 
    #they affect only the execution of the innermost one. 
# Have a look at rather silly example to demonstrate it.
for i in range(3):
    for j in range(5):
        if j > i:
            # breaks only the for on line 2
            break
        print(i, j)