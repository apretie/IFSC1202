def isEven(e):
    if int(e % 2 == 0):
        return True
    else:
        return False
def isOdd(o):
    if int(o % 2 != 0):
        return True
    else:
        return False
def isPrime(p):
    half = (p // 2) + 1
    for i in range(2, half):
        # If the number is divisible by any number
        # other than 1 and self then it is not prime
        if p % i == 0:
            return False

    return True


numfile = open("/workspace/IFSC1202/Assignments/Unit 6 HW/Text Files/06.06 Numbers.txt", "r")
num = numfile.readline()

enumfile = open("/workspace/IFSC1202/Assignments/Unit 6 HW/Text Files/06.06 Evennumbers.txt", "w")
onumfile = open("/workspace/IFSC1202/Assignments/Unit 6 HW/Text Files/06.06 Oddnumbers.txt", "w")
pnumfile = open("/workspace/IFSC1202/Assignments/Unit 6 HW/Text Files/06.06 Primenumbers.txt", "w")

ncount = 0
ecount = 0
ocount = 0
pcount = 0
while num != "":
    num = int(num)
    if isEven(num):
        enum = str(num)
        enumfile.write(enum)
        enumfile.write("\n")
        ecount += 1
    if isOdd(num):
        onum = str(num)
        onumfile.write(onum)
        onumfile.write("\n")
        ocount += 1
    if isPrime(num):
        pnum = str(num)
        pnumfile.write(pnum)
        pnumfile.write("\n")
        pcount += 1
    ncount += 1
    num = numfile.readline()

numfile.close()
enumfile.close()
onumfile.close()
pnumfile.close()

print("{} even numbers".format(ecount))
print("{} odd numbers".format(ocount))
print("{} prime numbers".format(pcount))
print("{} numbers read".format(ncount))
