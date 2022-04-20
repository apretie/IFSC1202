
class RetailItem ():
     def __init__(self, description="", unitsonhand=0, price=0):
          self.Description = description
          self.UnitsOnHand = unitsonhand
          self.Price = price
     def InventoryValue(self):
          return self.UnitsOnHand * self.Price

openfile = open("/workspace/IFSC1202/Assignments/Unit 10 HW/10.02 Inventory.txt", 'r') 
x = openfile.readline()

print("{:>11} {:>20} {:>20} {:>20}".format("Description","Units On Hand","Price","Inventory Value"))

list = []

while x != "":
    y = x.split(",")
    item = RetailItem(y[0],int(y[1].strip()),float(y[2].strip()))
    print("{:>11} {:20} {:20.2f} {:20.2f}".format(item.Description,item.UnitsOnHand,item.Price,item.InventoryValue()))
    list.append(item)
    x = openfile.readline()

openfile.close()

#HW Output:
#Description       Units On Hand               Price     Inventory Value
     #Jacket                  12                9.95              119.40
      #Jeans                  40               34.95             1398.00
      #Shirt                  20               24.95              499.00