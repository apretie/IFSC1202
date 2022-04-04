namefile = open("/workspace/IFSC1202/Exam Two Names.txt","r")
nametxt = namefile.readline()
a =[]
rank = 0
found = "no"
while nametxt != "":
    names = nametxt.split(",")
    for i in range(len(names)):
        names[i] = str(names[i]).strip(" ")
        names[i] = str(names[i]).strip("\n")
    a.append(names)
    nametxt = namefile.readline()
namefile.close()

fnandr = str(input("Enter a Name: ")) #find name and rank
fnandr = fnandr.strip(" ")
fnandr = fnandr.title()
if fnandr == "Q":
    exit()
found = 0
for i in range(len(a)):
    rank += 1
    for j in range(len(a[i])):
       if fnandr == a[i][j]:
            if j == 0:
                print("Boy's Name - Rank: {}".format(rank))
                found = 1
            elif j == 1:
                print("Girl's Name - Rank: {}".format(rank))
                found = 1

if found == 0:
    print("Name Not Found")


            
#
