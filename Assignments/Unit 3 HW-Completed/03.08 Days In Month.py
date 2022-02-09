x = int(input("Enter Month: "))
#1, 3, 5, 7, 8, 10, 12 are months with 31 days
#(11, 4, 6, 9)Thirty days have November, April, June, and September. :)
if x % 2 != 0 and  0 < x < 8 or x % 2 == 0 and  7 < x < 13:
    print(31)
elif x == 11 or x == 4 or x == 6 or x == 9:
    print(30)
else:
    print(28)
