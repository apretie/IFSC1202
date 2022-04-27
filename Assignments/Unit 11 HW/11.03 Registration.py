class Student ():
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.CourseList = []

class StudentList ():
    def __init__(self):
        self.Studentlist = []
    def add_student(self, firstname, lastname, tnumber):
        person = Student(firstname, lastname, tnumber)
        self.append(person)
    def find_student(self, studenttofind):
        for sindex in range(len(Studentlist)):
            if self[sindex].TNumber == studenttofind:
                return sindex
            #print_student_list - Prints the Student Registration data - def print_student_list(self):
                #Prints headings
                #Loops through each student and prints name and t-number
                    #For each students, loops through the courses in which the student has registered.
    def print_student_list(self):
        print("First Name     Last Name      T-Number       Course          Name                                             Room           Meeting Times")
        for i in range(len(Studentlist)):
            print("{:<15}{:<15}{:<15}".format(Studentlist[i].FirstName,Studentlist[i].LastName,Studentlist[i].TNumber))
            for j in range(len(Studentlist[i].CourseList)): 
                print("{}{:4} {:4}       {:49}{:15}{:15}".format(" "*45,Studentlist[i].CourseList[j].Department,Studentlist[i].CourseList[j].Number,Studentlist[i].CourseList[j].Name,Studentlist[i].CourseList[j].Room,Studentlist[i].CourseList[j].MeetingTimes))
    def add_student_from_file(self, filename):
        studentsfile = open(filename, 'r')
        line = studentsfile.readline()
        while line != "":
            y = line.split(",")
            StudentList.add_student(Studentlist, y[0].strip(), y[1].strip(), y[2].strip())
            line = studentsfile.readline()
        studentsfile.close()

class Course():
    def __init__(self, department, number, name, room, meetingtimes):
        self.Department = department
        self.Number = number
        self.Name = name
        self.Room = room
        self.MeetingTimes = meetingtimes

class CourseList ():
    def __init__(self):
        self.Courselist = []
    def add_course(self, department, number, name, room, meetingtimes):
        classes = Course(department, number, name, room, meetingtimes)
        self.append(classes)
    def find_course(self, departmenttofind, numbertofind):
        for cindex in range(len(Courselist)):
            if self[cindex].Department == departmenttofind and self[cindex].Number == numbertofind:
                return cindex
    def add_course_from_file(self, filename):
        coursesfile = open(filename, 'r')
        line = coursesfile.readline()
        while line != "":
            z = line.split(",")
            CourseList.add_course(Courselist, z[0].strip(), z[1].strip(), z[2].strip(), z[3].strip(), z[4].strip())
            line = coursesfile.readline()
        coursesfile.close()

# Main
Courselist = []
CourseList.add_course_from_file(Courselist, "/workspace/IFSC1202/Assignments/Unit 11 HW/11.03 Courses.txt")
Studentlist = []
StudentList.add_student_from_file(Studentlist, "/workspace/IFSC1202/Assignments/Unit 11 HW/11.03 Students.txt")


openfile = open("/workspace/IFSC1202/Assignments/Unit 11 HW/11.03 Registration.txt", 'r') 
reg = openfile.readline()

while reg != "":
    x = reg.split(",")
    cindex = CourseList.find_course(Courselist, x[1].strip(), x[2].strip())
#     Create a new course object out the selected course object
    mycourse = Courselist[cindex]
    mystudentlist = []
    sindex = StudentList.find_student(Studentlist, x[0])
    #Append the new course object to course list in the selected student course list using .append mystudentlist.Studentlist[sindex].CourseList.append(mycourselist)
    mystudentlist.append(Studentlist[sindex].CourseList.append(mycourse))
    reg = openfile.readline()

StudentList.print_student_list(mystudentlist)
openfile.close()

#Hw Output:
#First Name    Last Name     T-Number      Course         Name                                              Room          Meeting Times
#Jim           Evans         T123456       
                                          #IFSC 1202      Introduction to Object-oriented Technology        EIT 212       M-W 11:00-12:00
                                          #IFSC 1310      Web Technologies                                  EIT 213       M-W 12:00-1:00
                                          #IFSC 2200      Ethics in the Profession                          EIT 214       M-W 1:00-2:00
                                          #IFSC 2300      Object-oriented Technology                        EIT 211       M-W 3:00-4:00
                                          #IFSC 3300      Web Client Applications                           EIT 211       T-T 1:00-2:00
#Joe           Smith         T654321       
                                          #IFSC 2305      Computer Systems                                  EIT 212       T-T 9:00-10:50
                                          #IFSC 2315      Information Systems Software                      EIT 213       T-T 11:00-12:00
                                          #IFSC 2340      Human Computer Interface                          EIT 214       T-T 12:00-1:00
                                          #IFSC 3300      Web Client Applications                           EIT 211       T-T 1:00-2:00
                                          #IFSC 3315      Applied Networking                                EIT 212       T-T 2:00-3:00
#Jane          Doe           T121212       
                                          #IFSC 3320      Database Concepts                                 EIT 213       T-T 3:00-4:00
                                          #IFSC 3342      Mobile Web Development                            EIT 211       M-W 11:00-12:00
                                          #IFSC 3360      System Analysis and Design                        EIT 212       M-W 12:00-1:00
                                          #IFSC 4325      Data Mining Concepts and Techniques               EIT 211       M-W 3:00-4:00
                                          #IFSC 4330      Database Security                                 EIT 212       T-T 9:00-10:50