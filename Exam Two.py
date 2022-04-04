namefile = open("/workspace/IFSC1202/Exam Two Names.txt","r")
nametxt = namefile.readline()
a =[]
rank = 0
found = "no"
while nametxt != "":
    names = nametxt.split(",")
    for i in range(len(names)):
        names[i] = str(names[i]).strip(" ")
    a.append(names)
    nametxt = namefile.readline()
namefile.close()
#print(a[0][0]) 
fnandr = str(input("Enter a Name: ")) #find name and rank
fnandr = fnandr.strip(" ")
fnandr = fnandr.title()
if fnandr == "Q":
    exit()
j = 5
for i in range(len(a)):
    rank += 1
    for j in range(len(a[i])):
        #print(a[i][j])
        #print("fnandr is {}".format(fnandr))
       if fnandr == a[i][j]:
            if j == 0:
                print("Boy's Name - Rank: {}".format(rank))
            elif j == 1:
                print("Girl's Name - Rank: {}".format(rank))
            #found = "yes"
            #print("Boy's Name - Rank: {}".format(rank))
if j == 5:
    print("Name Not Found")
        #fnandr != a[i][j]

            
#
