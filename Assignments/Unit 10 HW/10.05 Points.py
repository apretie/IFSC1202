#Process each line of data in the 10.05 Points.txt file. As you read each line from Points.txt, you will create two Point objects. You can reuse these objects as you read the next datapoint.
#The first two values are the (x,y) values for point A, and the second two values are the (x,y) values for point B.
#Read each datapoint pair and disply the datapoint values, distancd, midpoint, and XAngle.
from math import atan
from math import pi
from math import sqrt

class Point:
    def __init__(self, Xvalue, Yvalue):
        self.x = Xvalue 
        self.y = Yvalue
    def ToString(self):
        return "(" + str(self.x) + ", "+ str(self.y)+")"
def Distance(pointA, pointB):
    return sqrt((pointB.x - pointA.x)**2 + (pointB.y - pointA.y)**2)
def MidPoint(pointA, pointB):
    x = (pointB.x + pointA.x) / 2
    y = (pointB.y + pointA.y) / 2
    newmidpoint = Point(x,y)
    return newmidpoint
def XAngle(pointA, pointB):
    slope = (pointB.y - pointA.y) / (pointB.x - pointA.x)
    newXangle = atan(slope) * 180 / pi
    return newXangle

print("     {:<20s}{:<20s}{:<20s}{:<20s}{:<20s}".format("Point A","Point B","Distance","Midpoint","Angle"))
print("{:>20s}{:>20s}{:>20s}{:>20s}{:>20s}".format("-"*15,"-"*15,"-"*15,"-"*15,"-"*15))

textfile = open("/workspace/IFSC1202/Assignments/Unit 10 HW/10.05 Points.txt", 'r')
line = textfile.readline()

while line != "":
    values = line.split(",")
    pointA = Point(float(values[0].strip()),float(values[1].strip()))
    pointB = Point(float(values[2].strip()),float(values[3].strip()))
    print("{:>20s}{:>20s}{:>20.7f}{:>20s}{:>20.7f}".format(pointA.ToString(), pointB.ToString(), Distance(pointA,pointB), MidPoint(pointA,pointB).ToString(), XAngle(pointA,pointB)))
    line = textfile.readline()

textfile.close()

#HW Output:
#  Point A              Point B             Distance             Midpoint                Angle
     #---------------      ---------------      ---------------      ---------------      --------------- 
          #(0.0, 0.0)           (1.0, 1.0)            1.4142136           (0.5, 0.5)           45.0000000
          #(0.0, 0.0)           (4.0, 3.0)            5.0000000           (2.0, 1.5)           36.8698976
        #(-1.0, -1.0)           (3.0, 2.0)            5.0000000           (1.0, 0.5)           36.8698976
          #(0.0, 0.0)     (1.7320508, 1.0)            2.0000000     (0.8660254, 0.5)           30.0000001