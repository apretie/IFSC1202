#In the assignment, you will use the Cartesian Coordinate system, which uses the x and y axes. Each data point has an x value and a y value.
#Use the following code to create a datapoint object:
        # Step 1 - Define the class object "Point"
            #class Point:
        # Step 2 - Define the initializer and any default values
            #def __init__(self, Xvalue, Yvalue):
        # Step 3 - Define the object attributes
            #self.x = Xvalue
            #self.y = Yvalue
        ## Step 4 - Define the methods for the object
# ToString returns a nicely formated string to represent the data point
            #def ToString(self):
        #return "(" + str(self.x) + ", " + str(self.y) + ")"
#Functions - Create the following functions to make calculations about datapoints
#Distance - calculates the distance between two datapoints.
#Parameters:
#Point A - a Point object with values
#Point B - a Point ojbect with values
#Returns:
#Distance - a floating point number indicated the distance between the two datapoints For points A and B, formula for the distance is:
#The square root of ((XB - XA)2 + (YB - YA)2)
#Note: you will have to import the sqrt function from the math library
#MidPoint - calculates the midpoint between two datapoints.
#Parameters:
#Point A - a Point object with values
#Point B - a Point ojbect with values
#Returns:
#Midpoint Datapoint - a Point object containing the midpoint values. For points A and B, formula for the midpoint is:
#x value = (XB + XA) / 2
#y value = (YB + YA) / 2
#XAngle - calculates angle of the line between the two datapoints.
#Parameters:
#Point A - a Point object with values
#Point B - a Point ojbect with values
#Returns:
#Angle - a floating point number indicating the angle of the line to the x axis in degrees. For points A and B, formula for the XAngle is:
#slope = (YB - YA / (XB - XA)
#XAngle = atan(slope) * 180 / pi
#Note: you will have to import the atan function from the math library (arc tangent function)
#Process each line of data in the 10.05 Points.txt file. As you read each line from Points.txt, you will create two Point objects. You can reuse these objects as you read the next datapoint.
#The first two values are the (x,y) values for point A, and the second two values are the (x,y) values for point B.
#Read each datapoint pair and disply the datapoint values, distancd, midpoint, and XAngle.




#HW Output:
#  Point A              Point B             Distance             Midpoint                Angle
     #---------------      ---------------      ---------------      ---------------      --------------- 
          #(0.0, 0.0)           (1.0, 1.0)            1.4142136           (0.5, 0.5)           45.0000000
          #(0.0, 0.0)           (4.0, 3.0)            5.0000000           (2.0, 1.5)           36.8698976
        #(-1.0, -1.0)           (3.0, 2.0)            5.0000000           (1.0, 0.5)           36.8698976
          #(0.0, 0.0)     (1.7320508, 1.0)            2.0000000     (0.8660254, 0.5)           30.0000001