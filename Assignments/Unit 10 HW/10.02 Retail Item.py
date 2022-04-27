class RetailItem ():
     def __init__(self, description="", unitsonhand=0, price=0):
          self.Description = description
          self.UnitsOnHand = unitsonhand
          self.Price = price
     def InventoryValue(self):
          return self.UnitsOnHand * self.Price

openfile = open("/workspace/IFSC1202/Assignments/Unit 10 HW/10.02 Inventory.txt", 'r') 

x = openfile.readline()
y = x.split(",")
item1 = RetailItem(y[0].strip(),int(y[1].strip()),float(y[2].strip()))    
x = openfile.readline()
y = x.split(",")
item2 = RetailItem(y[0].strip(),int(y[1].strip()),float(y[2].strip()))    
x = openfile.readline()
y = x.split(",")
item3 = RetailItem(y[0].strip(),int(y[1].strip()),float(y[2].strip()))    

openfile.close()

print("{:>11} {:>20} {:>20} {:>20}".format("Description","Units On Hand","Price","Inventory Value"))
print("{:>11} {:20} {:20.2f} {:20.2f}".format(item1.Description,item1.UnitsOnHand,item1.Price,item1.InventoryValue()))
print("{:>11} {:20} {:20.2f} {:20.2f}".format(item2.Description,item2.UnitsOnHand,item2.Price,item2.InventoryValue()))
print("{:>11} {:20} {:20.2f} {:20.2f}".format(item3.Description,item3.UnitsOnHand,item3.Price,item3.InventoryValue()))


#HW Output:
#Description       Units On Hand               Price     Inventory Value
     #Jacket                  12                9.95              119.40
      #Jeans                  40               34.95             1398.00
      #Shirt                  20               24.95              499.00