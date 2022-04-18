#reate a class called RetailItem that holds data about an Item in a retail store.
#The class should have the following attributes:
#Description - description of the item (default "")
#UnitsOnHand - the number of units in inventory (default 0)
#Price - the item's retail price (default 0)
#Create a constructor that accepts the Description, UnitOnHand, and Price, then sets them to attributes in the RetailItem Class.
#If one of the attributes is not present, then set the attribute to the default value.
#Create a method called InventoryValue, which returns the UnitsOnHand times Price.
#Read the 10.02 Inventory.txt file and creates three objects, one for each item.
#Display a report that displays the Description, Units On Hand, Price, and Inventory Value

class RetailItem ():
     def __init__(self, Description="", UnitsOnHand=0, Price=0):
          self.Description = Description
          self.UnitsOnHand = UnitsOnHand
          self.Price = Price
     def InventoryValue(self):
          return self.UnitsOnHand * self.Price()
invenfile = open("/workspace/IFSC1202/Assignments/Unit 10 HW/10.02 Inventory.txt", 'r') 
x = invenfile.readline() 
y = x.split(",")
item1 = RetailItem(y[0])

openfile = open("/workspace/IFSC1202/Assignments/Unit 10 HW/10.02 Inventory.txt", 'r') 
x = openfile.readline()

while x != "":
    y = x.split(",")
    for i in range(len(y)):

print("{:<10} {:<10} {:<10}".format("Description","Units On Hand","Price"))


#HW Output:
#Description       Units On Hand               Price     Inventory Value
     #Jacket                  12                9.95              119.40
      #Jeans                  40               34.95             1398.00
      #Shirt                  20               24.95              499.00