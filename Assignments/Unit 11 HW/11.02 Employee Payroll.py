#Create a class named Employee that has the following attributes:
#FirstName
#LastName
#IDNumber
#HoursWorked
#Wage
#Create an initializer that accepts the FirstName, LastName, IDNumber, and Wage and assigns them to the appropriate attribute. Set HoursWorked to 0.
#Create a method called WeeklyPay, which calculates the weekly pay. Weekly pay is defined as 1 times the wage for hours 0-40, and 1.5 times wage for hours greater than 40
#In your main program, create the following function:
#find_employee - which has the Employee list and the EmployeeID as the arguments. This function searches the list and looks for a match on the EmployeeID. The function returns the index of the employee. If the item is not found a -1 is returned. See the find_ball function in 11.01 - Creating a List of Objects Using Instantiation
#Read the 11.02 Employees.txt file and create a list of employee objects
#Read the 11.02 Hours.txt file, update the hour worked for the appropriate employee
#Print the results
class Employee:
    def __init__(self,firstname,lastname,idnumber,hoursworked,wage):
        self.FirstName = firstname
        self.LastName = lastname
        self.IDNumber = idnumber
        self.HoursWorked = 0
        self.Wage = float(wage)

    def WeeklyPay(self):
        if self.HoursWorked >= 40:
             OT = (self.HoursWorked-40) * (1.5 * self.Wage)
             RT = 40 * self.Wage
        else:
             OT = 0
             RT = self.HoursWorked * self.Wage
        return RT + OT
    
def find_employee(emplist, empID):
    for i in range(len(emplist)):
        if emplist[i].IDNumber == empID:
            return i
    return -1

emplist = []

file1 = open("/workspace/IFSC1202/Assignments/Unit 11 HW/11.02 Employees.txt", 'r')
line1 = file1.readline()
file2 = open("/workspace/IFSC1202/Assignments/Unit 11 HW/11.02 Hours.txt", 'r')
line2 = file2.readline()

print("{:>7} {:>7} {:>7} {:>7} {:>7} {:>7}".format("First","Last","ID","Hours","Hourly","Weekly"))
print("{:>7} {:>7} {:>7} {:>7} {:>7} {:>7}".format("Name","Name","Number","Worked","Wage","Pay"))

while line1 != "":
   y = line1.split(",")
   emp1 = Employee(y[0].strip(),y[1].strip(),y[2].strip(),0,y[3].strip())
   emplist.append(emp1)
   line1 = file1.readline()
while line2 != "":
   z = line2.split(",")
   empID = z[0]
   hours = z[1]
   emplist[find_employee(emplist, empID)].HoursWorked = int(hours)
   line2 = file2.readline()
for i in range(len(emplist)):
   print("{:>7} {:>7} {:>7} {:7.2f} {:7.2f} {:7.2f}".format(emplist[i].FirstName,emplist[i].LastName,emplist[i].IDNumber,emplist[i].HoursWorked,emplist[i].Wage,emplist[i].WeeklyPay()))
file1.close()
file2.close()




#HW Output:
#First    Last      ID   Hours  Hourly  Weekly
#   Name    Name  Number  Worked    Wage     Pay
#   Susan  Meyers   47899   41.00   15.64  649.06
#    Mark   Jones   39119   37.00   14.46  535.02
#     Joy  Rogers   41774   43.00   15.28  679.96