l = int(input("Enter Length of Race in Kilometers: "))
m = int(input("Enter Minutes: ")) 
s = int(input("Enter Seconds: "))

lmiles = l / 1.61
min = m / 60
sec = s / 60**2
h = min + sec
print(lmiles / h)