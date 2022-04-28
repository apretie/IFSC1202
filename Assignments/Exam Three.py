#Code the House class with its attributes and methods
class House ():
    def __init__(self):
          self.Address = ""
          self.Sqft = 0
          self.Price = 0
    
    def costpersqft (self):
        return self.Price / self.Sqft
    
    def payment (self, ar, ny, nper):
        nper = 12 * int(years)
        ar = int(intrate / nper) / 100
        pay = int(ar * self.Price)
        return 100


#Open Exam Three Houses.txt, read a line from the file, split the line into a list
openfile = open("/workspace/IFSC1202/Assignments/Exam Three Houses.txt", 'r') 


#Create a House object from the list and append the House object to a list called HouseList

#Houselist[] = (Houselist[0].strip()Houselist[1].strip())
#streetadd =float(houses[0])

x = openfile.readline()
y = x.split(",")
House1 = House()
House1.Address = y[0].strip()
House1.Sqft = int(y[1].strip())
House1.Price = int(y[2].strip())

x = openfile.readline()
y = x.split(",")
House2 = House()
House2.Address = y[0].strip()
House2.Sqft = int(y[1].strip())
House2.Price = int(y[2].strip())

x = openfile.readline()
y = x.split(",")
House3 = House()
House3.Address = y[0].strip()
House3.Sqft = int(y[1].strip())
House3.Price = int(y[2].strip())

intrate = input(str("Enter Interest Rate: "))
years = int(input(str("Enter Years for Mortgage: ")))

intrate = int(intrate) / 100
print("{:>8s} {:>8s} {:>8} {:>8} {:>8}".format("Address","Sq Ft","SqFt Cost", "Price", "Payment"))
print("{:>8s} {:>8s} {:>8} {:>8} {:>8}".format(House1.Address(), House1.Sqft(), House1.costpersqft(), House1.Price(), House1.payment()))
print("{:>8s} {:>8s} {:>8} {:>8} {:>8}".format(House2.Address(), House2.Sqft(), House2.costpersqft(), House2.Price(), House2.payment()))
print("{:>8s} {:>8s} {:>8} {:>8} {:>8}".format(House3.Address(), House3.Sqft(), House3.costpersqft(), House3.Price(), House3.payment()))