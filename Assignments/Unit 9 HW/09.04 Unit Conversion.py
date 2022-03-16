FromValue = input(float("Enter From Value: "))
FromUnit = input(float("Enter From Unit (mm, cm, m, km, in, yd, mi):"))
ToUnit = input(float("Enter To Unit (mm, cm, m, km, in, yd, mi): "))

#Open the file 9.4 Conversion.txt file and read it into a 2 dimensional list.
#The first row contains the names of the valid ToUnits.
#The first column contains the names of the valid FromUnits.
#Using a FOR loop, seach for a match between the entered FromUnit and the first column. Save the index of the row that you find the match.
#If no match was found for the FromUnit, then print "FromUnit is not valid" and exit the program
#Using a FOR loop, seach for a match between the entered ToUnit and the first row. Save the index of the column that you find the match.
#If no match was found for the ToUnit, then print "ToUnit is not valid" and exit the program
#Using the index, get the multiplier from the 2D list, multiply it by the FromValue, round to 7 digits, and displays the result as shown.












# HW Test Cases:
# Your answer may be slightly different due to rounding.
#Enter From Value: 36
#Enter From Unit (mm, cm, m, km, in, yd, mi): in
#Enter To Unit (mm, cm, m, km, in, yd, mi): yd
#36.0 in => 1.0 yd

#Enter From Value: 10000
#Enter From Unit (mm, cm, m, km, in, yd, mi): ft
#Enter To Unit (mm, cm, m, km, in, yd, mi): mi
#10000.0 ft => 1.8939394 mi

#Enter From Value: 100
#Enter From Unit (mm, cm, m, km, in, yd, mi): yd
#Enter To Unit (mm, cm, m, km, in, yd, mi): ft
#100.0 yd => 300.0 ft

#Enter From Value: 250
#Enter From Unit (mm, cm, m, km, in, yd, mi): yd
#Enter To Unit (mm, cm, m, km, in, yd, mi): ft
#250.0 yd => 750.0 ft