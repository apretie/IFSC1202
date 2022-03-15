#The 09.06 CityTemps.txt file contains weekly temperature readings for various cities in Central Arkansas for Mo, Tu, We, Th, Fr, Sa, and Su.
#Create a program calculates the average temperature by city and displays the result. 
#Don't hard code the column numbers; 
    #use the length of your list or array to loop through the values.
#The program will perform the following tasks:
    #Open 09.06 CityTemps.txt for reading
    #Create the temps list that contains the city name and temperature values
    #Read the input file
    #Check for end of file (line is blank)
    #Split the input line into its parts
    #Append the input as a row in a two dimensional array. Note that the first element is the city name
    #Read the next line
    #Close the input file
    #Calculate the Average Temperature for each location
        #Loop through each row in temps
        #Loop through each column in temps
        #Add the temperature to a total
        #Divide the total by the number of columns - 1 (the first column is the city name)
        #Append the result to the end of the row in the temps array (just convert the average to an integer)
#Print the Results
    #Create and display a heading
    #Loop through the number of rows in the temps array
    #Loop through the number of columns in temp and display the data in the array (city, temperature data, and average).













#HW Output: 
# City     Mo       Tu       We       Th       Fr       Sa       Su       Avg     
# Benton   65       68       67       65       69       70       71       67       
# Conway   68       73       67       69       71       73       73       70       
# Lonoke   67       72       70       71       73       74       75       71  