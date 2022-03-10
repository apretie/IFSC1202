
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
        if int(p % 2 != 0) and int(p % 3 != 0) and int(p % 5 != 0) and int(p % 7 != 0) and int(p % 11 != 0) or (p == 2) or (p == 3) or (p == 5) or (p == 7) or (p == 11):
            return True
        else:
            return False


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
