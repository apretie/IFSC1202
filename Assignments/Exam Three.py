class House ():
     def __init__(self, address, sqft, price):
          self.Address = address
          self.Sqft = sqft
          self.Price = price
    def costpersqft (self,):
        return self.Price * self.Sqft
    def payment (ar, ny):

openfile = open("/workspace/IFSC1202/Assignments/Exam Three Houses.txt", 'r') 
x = openfile.readline()

intrate = input(str("Enter Interest Rate: "))
years = input(str("Enter Years for Mortgage: "))

