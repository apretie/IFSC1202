#Create a class named Employee that has the following attributes:
    #FirstName
    #LastName
    #IDNumber
    #HoursWorked
    #Wage
#Create an initializer that accepts the FirstName, LastName, IDNumber, HoursWorked, and Wage and assigns them to the appropriate attribute.
#The Employee class should have method called WeeklyPay, which calculates the weekly pay.
#Weekly pay is defined as 1 times the wage for hours 0-40, and 1.5 times wage for hours greater than 40
#As you read each line from Payroll.txt, you will create one Employee object. You can reuse this object as you read the next employee.
#Print the FirstName, LastName, IDNumber, HoursWorked, HourlyWage, and WeeklyPay for each employee
class Employee:
    def __init__(self,firstname,lastname,idnumber,hoursworked,wage):
        self.FirstName = firstname
        self.LastName = lastname
        self.IDNumber = idnumber
        self.HoursWorked = int(hoursworked)
        self.Wage = float(wage)
    def WeeklyPay(self):
        if self.HoursWorked >= 40:
             OT = (self.HoursWorked-40) * (1.5 * self.Wage)
             RT = 40 * self.Wage
        else:
             OT = 0
             RT = self.HoursWorked * self.Wage
        return RT + OT

textfile = open("/workspace/IFSC1202/Assignments/Unit 10 HW/10.06 Payroll.txt", 'r') 
line = textfile.readline()

print("{:>7} {:>7} {:>7} {:>7} {:>7} {:>7}".format("First","Last","ID","Hours","Hourly","Weekly"))
print("{:>7} {:>7} {:>7} {:>7} {:>7} {:>7}".format("Name","Name","Number","Worked","Wage","Pay"))

while line != "":
   y = line.split(",")
   emp1 = Employee(y[0].strip(),y[1].strip(),y[2].strip(),y[3].strip(),y[4].strip())
   print("{:>7} {:>7} {:>7} {:7.2f} {:7.2f} {:7.2f}".format(emp1.FirstName,emp1.LastName,emp1.IDNumber,emp1.HoursWorked,emp1.Wage,emp1.WeeklyPay()))
   line = textfile.readline()

textfile.close()


#HW Output:
#First    Last      ID   Hours  Hourly  Weekly
    #Name    Name  Number  Worked    Wage     Pay
   #Susan  Meyers   47899   41.00   15.64  649.06
    #Mark   Jones   39119   37.00   14.46  535.02
     #Joy  Rogers   41774   43.00   15.28  679.96


#Grading Rubric:
#25 points - init method for Employee Class
#25 points - WeeklyPay method
#25 points = Instantiate 3 employee objects and prints attributes