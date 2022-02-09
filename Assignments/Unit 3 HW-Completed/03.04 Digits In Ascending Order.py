num = int(input("Enter a Number: "))
one = (num % 10)
ten = (num // 10)%10
hun = (num // 100)%10
lst = [hun,ten,one]
if sorted(lst) == lst:
    print("YES")

else:
    print("NO")