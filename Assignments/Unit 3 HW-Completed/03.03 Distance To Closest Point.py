A = int(input("Enter Point A: "))
B = int(input("Enter Point B: "))
C = int(input("Enter Point C: "))

if abs(A - B) < abs(A - C):
    cp = B

else:
    cp = C
print(abs(A - cp))
