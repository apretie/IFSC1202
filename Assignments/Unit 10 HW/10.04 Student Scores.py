#Step 1 - Create a class called Student
#Step 2 - Define the initializer, the initializer should accept the folloing class values:
    #firstname (string)
    #lastname (string)
    #tnumber (string)
    #scores (List of string scores) Note this list is variable in length
#Step 3 - In the initializer, create the following object attributes
    #FirstName (string)
    #LastName (string)
    #TNumber (string)
    #Grades (List of string grades) Note that this list is variable in length
#Step 4 - Define the methods for the object
    #RunningAverage(self) - calculates the running average (non-blank) of the scores
    #TotalAverage(self) - calculates the average oft the scores, where missing scores are treated a zero
    #LetterGrade(self) - Returns the letter grade based on TotalAverage, where
        #>= 90 is an"A"
        #>= 80 and < 90 is a "B"
        #>= 70 and < 80 is a "C"
        #>= 60 and < 70 is a "D"
        #< 60 is an "F"
#As you read each line from StudentScores.txt, you will create one Student object. 
#You can reuse this object as you read the next student.
#Note about 10.04 StudentScores.txt
    #Jim Evans has 3 scores - the second score is missing
    #Joe Smith has 4 scores
    #Jane Doe has 2 scores - the first score is missing
class Student():
    def_init_(self, firstname, lastname, tnumber, scores):
        self.First Name = firstname
        self.Last




#HW Output:
  #First         Last           ID      Running     Semester       Letter
        #Name         Name       Number      Average      Average        Grade
#------------ ------------ ------------ ------------ ------------ ------------
         #Jim        Evans      T123456        83.00        55.33            F 
         #Joe        Smith      T654321        88.00        88.00            B 
        #Jane          Doe      T121212        99.50        66.33            D 