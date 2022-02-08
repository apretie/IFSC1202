num = int(input("Enter a 3 Digit Number: "))
one = (num % 10)
ten = (num // 10)%10
hun = (num // 100)%10
print("Reverse of Digits: {0:1d}{1:1d}{2:1d}".format(one,ten,hun))
