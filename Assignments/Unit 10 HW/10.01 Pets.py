class Pet():
  def __init__(self):
    self.PetName = ""
    self.Type = ""
    self.Age = ""

petlist = []
petfile = open("/workspace/IFSC1202/Assignments/Unit 10 HW/10.01 Pets.txt", 'r') 
x = petfile.readline()
print("{:>8s} {:>8s} {:>8}".format("Name","Type","Age"))

while x != "":
  y = x.split(",")
  mypet = Pet()
  mypet.PetName = y[0].strip()
  mypet.Type = y[1].strip()
  mypet.Age = int(y[2].strip())
  print("{:>8s} {:>8s} {:>8}".format(mypet.PetName,mypet.Type,mypet.Age))
  petlist.append(mypet)
  x = petfile.readline()

petfile.close()