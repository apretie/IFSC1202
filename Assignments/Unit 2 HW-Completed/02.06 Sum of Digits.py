num = int(input("Enter a 3 Digit Number: "))
one = (num % 10)
ten = (num // 10)%10
hun = (num // 100)%10
sum = one + ten + hun 

print("Sum of Digits: {:3d}".format(sum))
