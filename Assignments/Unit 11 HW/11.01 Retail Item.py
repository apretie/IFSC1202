#Create a Class called RetailItem that holds data about an Item in a retail store.
class RetailItem ():
#The RetailItem class should have the following attributes:
    def __init__(self, description="", unitsonhand=0, price=0):
          self.Description = description
          self.UnitsOnHand = unitsonhand
          self.Price = price
#Create a constructor for the RetialItem class that accepts the Description, UnitOnHand, and Price, then sets them to attributes in the RetailItem Class. If one of the it ems is not present, then set the attribute to the default value.
#Create a method called InventoryValue, which returns the UnitsOnHand times Price.

    def InventoryValue(self):
        return self.UnitsOnHand * self.Price

def find_inventory(mylist):
    print("{:>11} {:>20} {:>20} {:>20}".format("Description","Units On Hand","Price","Inventory Value"))
    for i in range(len(mylist)):

        print(list[i].Description, list[i].UnitsOnHand, list[i].Price, list[i].InventoryValue)        
def print_inventory(mylist):
    print("{:>11} {:>20} {:>20} {:>20}".format("Description","Units On Hand","Price","Inventory Value"))
    for i in range(len(mylist)):
        print(mylist[i].Description, mylist[i].UnitsOnHand, mylist[i].Price, mylist[i].InventoryValue)
#Read 11.01 Inventory.txt and create a list of inventory items

openfile = open("/workspace/IFSC1202/Assignments/Unit 11 HW/11.01 Inventory.txt", 'r') 
x = openfile.readline()
mylist = []

#Print the list of inventory items with the initial inventory value using the RetailItem attributes
while x != "":
    y = x.split(",")
    item = RetailItem(y[0],int(y[1].strip()),float(y[2].strip()))
    mylist.append(item)
    x = openfile.readline()
print_inventory(mylist)
   #print("{:>11} {:20} {:20.2f} {:20.2f}".format(item.Description,item.UnitsOnHand,item.Price,item.InventoryValue()))
    
#Read 11.01 InventoryUpdate.txt, search for the item to update, and update the price

updatefile = open("/workspace/IFSC1202/Assignments/Unit 11 HW/11.01 InventoryUpdate.txt", 'r') 
x = updatefile.readline()

#Print the list of inventory items with the updated inventory value

#Create thr following functions in your main program:
#print_inventory - which has the list at the argument. Prints the list with headings
#find_inventory - which has the list and the name of the inventory item as the argument. This function searches the list and looks for a match between the inventory item and the description. The function returns the index of the item. If the item is not found a -1 is returned. See the find_ball function in 11.01 - Creating a List of Objects Using Instantiation




print("{:>11} {:>20} {:>20} {:>20}".format("Description","Units On Hand","Price","Inventory Value"))

list = []


openfile.close()

#HW Output:
#Description       Units On Hand               Price     Inventory Value
#     Jacket                  12                9.95              119.40
#      Jeans                  40               34.95             1398.00
#      Shirt                  20               24.95              499.00

#Description       Units On Hand               Price     Inventory Value
#     Jacket                  12               10.95              131.40
#      Jeans                  40               35.95             1438.00
#      Shirt                  20               25.95              519.00