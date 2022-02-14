FromValue = float(input("Enter From Value: "))
FromUnit = (input("Enter From Unit (in, ft, yd, mi): "))
ToUnit = (input("Enter To Unit (in, ft, yd, mi): "))

if FromUnit == "in":
    if ToUnit == "ft":
        xply = 0.08333333333333
    elif ToUnit == "yd":
         xply = 0.02777777777778
    elif ToUnit == "mi":
         xply = 0.00001578282828283
    else:
        print("ToUnit is not valid")
        exit

elif FromUnit == "ft":
     if ToUnit == "in":
         xply = 12
     elif ToUnit == "yd":
         xply = 0.33333333333333
     elif ToUnit == "mi":
        xply = 0.0001893939393939
     else:
            print("ToUnit is not valid")
            exit

elif FromUnit == "yd":
    if ToUnit == "in":
        xply = 36
    elif ToUnit == "ft":
        xply = 3
    elif ToUnit == "mi":
        xply = 0.0005681818181818
    else:
        print("ToUnit is not valid")
        exit
elif FromUnit == "mi":
                if ToUnit == "in":
                 xply = 63360
                elif ToUnit == "ft":
                 xply = 5280
                elif ToUnit == "yd":
                 xply = 1760
                else:
                     print("ToUnit is not valid")
                     exit
else:

    print("FromUnit is not valid")
    exit   

ToValue = round(float(FromValue) * xply,6)

print("{0:.1f} {1} => {2} {3}".format(FromValue,FromUnit,ToValue,ToUnit))
