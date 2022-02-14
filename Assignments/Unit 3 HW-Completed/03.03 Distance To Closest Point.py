A = int(input("Enter Point A: "))
B = int(input("Enter Point B: "))
C = int(input("Enter Point C: "))
#Subtract B from A to get the distance(in absolute value:
  # ab = abs(A - B)
    # ac = abs(A - C)

if abs(A - B) < abs(A - C):
    cp = B

else:
    cp = C
print(abs(A - cp))
