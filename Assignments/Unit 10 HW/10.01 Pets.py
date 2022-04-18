#Create a class called Pet which has the following attributes:
#Name - name of pet
#Type - type of pet, such as "Cat", "Dog", etc
#Age - age of pet
#The constructor for the Pet class should not have any arguments.
#Read the 10.01 Pets.txt file, create three pet objects, one for each line, and print the object attributes for the pets using the .format method
#Print the Name, Type, and Age attributes from each of the pet objects
openfile
readfile
class Pet():
  def __init__(self):
    self.petname = ""
    self.type = ""
    self.age = ""

def Name(self):
  a = []
petfile = open("/workspace/IFSC1202/Assignments/Unit 10 HW/10.01 Pets.txt", 'r') 
x = petfile.readline()
y = x.split(",")





print("{:<8s} {:<8s} {:<10}".format("Name","Type","Age"))


#HW Output:
    #Name    Type     Age
    #Fido     Dog       3
  #Fluffy     Cat       5
  #Tweety    Bird       4
