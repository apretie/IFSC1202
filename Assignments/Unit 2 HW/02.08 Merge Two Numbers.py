x = int(input("Enter First 2 Digit Number: "))
y = int(input("Enter Second 2 Digit Number: "))
onex = (x % 10)
tenx = (x // 10)%10
oney = (y % 10)
teny = (y // 10)%10
print("Merged Number: {1:1d}{3:1d}{0:1d}{2:1d}".format(onex,tenx,oney,teny))
