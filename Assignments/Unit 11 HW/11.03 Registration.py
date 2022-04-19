#Create the following objects, attributes, and methods:
    #Student Class
    #The Student Class contains information about a specific student
        #Step 1 - Define the class object "Student"
        #Step 2 - Define the initializer and any default values
            #def init(self, firstname, lastname, tnumber):
        #Step 3 - Define the object attributes for a student
            #FirstName - First Name of student
            #LastName - Last Name of Student
            #TNumber - T-Number of Student
            #CourseList - an empty list of course
        #Step 4 - Define Actions (Methods) associated with the object
            #None
    #StudentList Class
    #The StudentList Class contains a list of Student objects
        #Step 1 - Define the class object "Studentlist"
        #Step 2 - Define the initializer and any default values
            #def init(self):
        #Step 3 - Define the object attributes of the students
            #Studentlist - an empty list of student objects
        #Step 4 - Define Actions (Methods) associated with the object
            #add_student - Add a student to the list - def add_student(self, firstname, lastname, tnumber):
                #Create a new student object using the parameters
                #Append new student object to Studentlist
            #find_student - Find a student in the Studentlist list and return the index - def find_student(self, studenttofind):
                #Loop though Studentlist
                #if the T-Number matches the sttudenttofind, then return the index in Studentlist
            #print_student_list - Prints the Student Registration data - def print_student_list(self):
                #Prints headings
                #Loops through each student and prints name and t-number
                    #For each students, loops through the courses in which the student has registered.
            #add_student_from_file - Reads the student file and append the values to the student list - def add_student_from_file(self, filename):
                #Opens and reads 11.03 Students.txt file
                #Calls add_student with data to create a student object and add it to the student list
    #Course Class
    #The Course contains information about a specific courses
        #Step 1 - Define the class object "Course"
        #Step 2 - Define the initializer and any default values
            #def init(self, department, number, name, room, meetingtimes):
        #Step 3 - Define the object attributes for a student
            #department - four character department abbreviation that is offering the course
            #number - four digit course number
            #name - long name for course
            #room - building and room number where the course meets
            #meetingtimes - day and times when the course meets
        #Step 4 - Define Actions (Methods) associated with the object
            #None
    #CourseList Class
    #The CourseList Class contains a list of Course objects
        #Step 1 - Define the class object "Courselist"
        #Step 2 - Define the initializer and any default values
            #def init(self):
        #Step 3 - Define the object attributes of the students
    #Courselist - an empty list of course objects
        #Step 4 - Define Actions (Methods) associated with the object
            #add_course - Add a course to the list - def add_course(self, department, number, name, room, meetingtimes):
                #Create a new couse object using the parameters
                #Append new course object to Courselist
            #find_course - Find a course in the Courselist list and return the index - def find_course(self, departmenttofind, numbertofind):
                #Loop though Courselist
                #if the department matches the departmenttofind and number matches numbertofind, then return the index in Courselist
            #add_course_from_file - Reads the course file and appends the values to the course list - def add_course_from_file(self, filename):
                #Opens and reads course file
                #Calls add_course with data to create a course object and add it to the course list
#Main Progam
#Create an empty Courselist object
#Read Course List File and append to course list object using add_course_from_file
#Create an empty Studentlist oject
#Read Student List File and append to student list object using add_student_from_file
#Open and read the registration information in the Registration file
#Based on the department and course number, find the index of the course in the course list using find_course
#Create a new course object out the selected course object
#Based on the TNumber, find the index of the student in the student list using find_student
#Append the new course object to course list in the selected student course list using .append mystudentlist.Studentlist[studentindex].CourseList.append(mycourse)
#Print the student registration using print_student_list

def Student ():
    def _init_(self, firstname, lastname, tnumber):
        self.




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