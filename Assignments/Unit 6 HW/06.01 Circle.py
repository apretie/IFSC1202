from math import pi
radiusfile = open("Assignments/Unit 6 HW/Text Files/06.01 Radius.txt", "r")
x = radiusfile.read()
radius = x
#print(x)
def diameter(x):
    radius = x * 2
    return radius
def circum(x):
    c = radius * pi * 2
    return c
def area(x):
    a = pi * radius ** 2
    return a
print("Radius Diameter Circumference Area") #need to use sep{}
print(radius, c, a)