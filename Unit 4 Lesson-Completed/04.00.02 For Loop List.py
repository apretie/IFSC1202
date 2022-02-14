#for loop iterates over any sequence. 
# Let's see the simplest example of using for. 
# Same as with if-else, 
   #indentation is what specifies which instructions are controlled by for and which aren't.

i = 1
for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
    print('#', i, 'color of rainbow is', color)
    i = i + 1