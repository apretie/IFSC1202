class Pet():
  def __init__(self):
    self.PetName = ""
    self.Type = ""
    self.Age = ""


petfile = open("/workspace/IFSC1202/Assignments/Unit 10 HW/10.01 Pets.txt", 'r') 

x = petfile.readline()
y = x.split(",")
mypet1 = Pet()
mypet1.PetName = y[0].strip()
mypet1.Type = y[1].strip()
mypet1.Age = int(y[2].strip())

x = petfile.readline()
y = x.split(",")
mypet2 = Pet()
mypet2.PetName = y[0].strip()
mypet2.Type = y[1].strip()
mypet2.Age = int(y[2].strip())

x = petfile.readline()
y = x.split(",")
mypet3 = Pet()
mypet3.PetName = y[0].strip()
mypet3.Type = y[1].strip()
mypet3.Age = int(y[2].strip())

petfile.close()

print("{:>8s} {:>8s} {:>8}".format("Name","Type","Age"))
print("{:>8s} {:>8s} {:>8}".format(mypet1.PetName,mypet1.Type,mypet1.Age))
print("{:>8s} {:>8s} {:>8}".format(mypet2.PetName,mypet2.Type,mypet2.Age))
print("{:>8s} {:>8s} {:>8}".format(mypet3.PetName,mypet3.Type,mypet3.Age))