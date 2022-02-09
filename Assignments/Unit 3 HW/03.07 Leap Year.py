n = int(input("Enter Year: "))

if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("LEAP YEAR")
else:
    print("COMMON YEAR")