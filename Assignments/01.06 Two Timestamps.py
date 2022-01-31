print("First Timestamp")
h = int(input("Enter Hours: "))
m = int(input("Enter Minutes: "))
s = int(input("Enter Seconds: "))
h = h * 60**2
m = m * 60
t = h + m + s

print("Second Timestamp")
h2 = int(input("Enter Hours: "))
m2 = int(input("Enter Minutes: "))
s2 = int(input("Enter Seconds: "))
h2 = h2 * 60**2
m2 = m2 * 60
t2 = h2 + m2 + s2
print(t2 - t)