mon = int(input("Enter Month: "))
day = int(input("Enter Day: "))

if mon % 2 != 0 and  0 < mon < 8 or mon % 2 == 0 and 7 < mon < 13:
    #mon = months31
    if day == 31:
        nday = 1
        if mon == 12:
            nmon = 1
        else:
            nmon = mon + 1
    elif day == 31:
        nday = 1
        nmon = 1
    else:
        nday = day + 1
        nmon = mon
elif mon == 11 or mon == 4 or mon == 6 or mon == 9:
    #mon = months30
    if day == 30:
        nday = 1
        nmon = mon + 1
    else:
        nday = day + 1
        nmon = mon
else:
    #only for feb, the only month with 28 days
    if day == 28:
        nday = 1
        nmon = 3
    else:
        nday = day + 1
        nmon = mon

print("Next Day: {0:2d}/{1:2d}".format(nmon,nday))