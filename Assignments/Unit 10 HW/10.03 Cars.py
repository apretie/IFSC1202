#Create a class named Car that has the following attributes
    #Year - Year the car was manufactured
    #Make - Maker of the car
    #Speed - Current speed of the car
#Constructor
    #The constructor should accept the car's year and make. The speed should be set to zero.
#Methods
    #Accelerate - Adds the value to the cars current speed
    #Brake - Subtract the value from the cars current speed (don't go below zero)
#The first record in the 10.03 Cars.txt contains the year and the make. Instantiate one car object with this data.
#The rest of the 10.03 Cars.txt contains acceleration and brake information.
#If the number is greater than zero, call the Accelerate method to add that amount of speed to the car.
#If the number is less that zero. call the Brake method to subtract that amount of speed from the car.
#Print the change of speed value and the current speed value


class Car ():
     def __init__(self, year, make):
          self.Year = year
          self.Make = make
          self.Speed = 0
     def Accelerate(self, change):
          self.Speed += change
          return self.Speed
     def Brake(self, change):
          self.Speed -= change
          if self.Speed < 0:
             self.Speed = 0
          return self.Speed

openfile = open("/workspace/IFSC1202/Assignments/Unit 10 HW/10.03 Cars.txt", 'r') 
x = openfile.readline()

y = x.split(",")
car1 = Car(y[0].strip(),y[1].strip())
print("Make: {}".format(car1.Make))
print("Year: {}".format(car1.Year))
print()
print("Change    Speed")
x = openfile.readline()

while x != "":
  change = int(x.strip())
  if change > 0:
    car1.Speed = car1.Accelerate(change)
  else:
    car1.Speed = car1.Brake(abs(change))
  print("{:>6}{:>9}".format(change,car1.Speed))
  x = openfile.readline()

openfile.close()

#HW Output:
#Make: Jeep
#Year: 2014

#Change    Speed
    #60       60
    #-5       55
   #-10       45
    # 3       48