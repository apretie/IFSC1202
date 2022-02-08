flt = float(input("Enter a Number: "))
num = int(flt)
frac = flt - num

ten = (frac // 0.1)%10
ten = int(ten)
print(ten)
