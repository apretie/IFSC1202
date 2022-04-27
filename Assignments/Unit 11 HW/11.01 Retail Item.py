#Create a Class called RetailItem that holds data about an Item in a retail store.
class RetailItem ():
    def __init__(self, description="", unitsonhand=0, price=0):
        self.Description = description
        self.UnitsOnHand = unitsonhand
        self.Price = price
#Create a method called InventoryValue, which returns the UnitsOnHand times Price.

    def InventoryValue(self):
        return self.UnitsOnHand * self.Price

def print_inventory(mylist):
    print("{:>11} {:>20} {:>20} {:>20}".format("Description","Units On Hand","Price","Inventory Value"))
    for i in range(len(mylist)):
        print("{:>11} {:>20} {:>20} {:>20.2f}".format(mylist[i].Description, mylist[i].UnitsOnHand, mylist[i].Price, mylist[i].InventoryValue()))

def find_inventory(mylist, name):
    for j in range(len(mylist)):
        if mylist[j].Description == name:
            return j
    return -1

#Read 11.01 Inventory.txt and create a list of inventory items
openfile = open("/workspace/IFSC1202/Assignments/Unit 11 HW/11.01 Inventory.txt", 'r') 
x = openfile.readline()

mylist = []
while x != "":
    y = x.split(",")
    item = RetailItem(y[0],int(y[1].strip()),float(y[2].strip()))
    mylist.append(item)
    x = openfile.readline()
print_inventory(mylist)
openfile.close()

print()
    
#Read 11.01 InventoryUpdate.txt, search for the item to update, and update the price
ufile = open("/workspace/IFSC1202/Assignments/Unit 11 HW/11.01 InventoryUpdate.txt", 'r') 
u = ufile.readline()

while u != "":
    for i in range(len(mylist)):
        y = u.split(",")
        uname = y[0].strip()
        update = float(y[1].strip())
        mylist[find_inventory(mylist,uname)].Price = update
        u = ufile.readline()

print_inventory(mylist)
ufile.close()

#HW Output:
#Description       Units On Hand               Price     Inventory Value
#     Jacket                  12                9.95              119.40
#      Jeans                  40               34.95             1398.00
#      Shirt                  20               24.95              499.00

#Description       Units On Hand               Price     Inventory Value
#     Jacket                  12               10.95              131.40
#      Jeans                  40               35.95             1438.00
#      Shirt                  20               25.95              519.00