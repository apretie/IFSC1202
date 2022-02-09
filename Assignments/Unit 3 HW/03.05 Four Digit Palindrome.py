num = int(input("Enter a Number: "))
one = (num % 10)
ten = (num // 10)%10
hun = (num // 100)%10
thou = (num // 1000)%10

if [one,ten,hun,thou] == [thou,hun,ten,one]:
    print("YES")

else:
    print("NO")