#The USPopulation.txt file contains the midyear population of United States, in thousands, during the years 1950 through 1990. 
# The first line in the file contains the population for 1950, the second line contains the population for 1951, and so forth. 
# Create an application that reads the file's contents into a list. 
# The application should do the following:
    #Read the file into an list of integers (multiply by 1000)
    #Iterate through the array and display:
        #(10 points) Year
        #Population
        #(10 points) Change from previous year (subtract current year minus previous year)
        #(10 points) Percent change in population over last year (change in population divided by previous year population)
    #When complete, display the following based on the changes in population (not changes in percent):
        #(10 points) Average Population Change
        #(10 points) Minimum Population Change and Year
        #(10 points) Maximum Population Change and Year
    #Do not use the list or string functions or methods for this assignment.
    #Do not use the for x in y iterator; use for x in range(n)
openfile = open("/workspace/IFSC1202/Text Files/08.11 USPopulation.txt","r")


while x != []:
    uspop = openfile.readline()
    p = int(x) *1000
    p.append(x)


change = 
perchange = {15.2f}













print("{:<10} {:<10} {:<10}".format("Population","Change","Percent Change"))









    
#Example: 
#Year    Population    Change    Percent Change
#1950    151868000     N/A       N/A
#1951    153982000     2114000   1.39%
#1952    156393000     2411000   1.57%
#1953    158956000     2563000   1.64%
#1954    161884000     2928000   1.84%
#1955    165069000     3185000   1.97%
#1956    168088000     3019000   1.83%
#1957    171187000     3099000   1.84%
#1958    174149000     2962000   1.73%
#1959    177135000     2986000   1.71%
#1960    179979000     2844000   1.61%
#1961    182992000     3013000   1.67%
#1962    185771000     2779000   1.52%
#1963    188483000     2712000   1.46%
#1964    191141000     2658000   1.41%
#1965    193526000     2385000   1.25%
#1966    195576000     2050000   1.06%
#1967    197457000     1881000   0.96%
#1968    199399000     1942000   0.98%
#1969    201385000     1986000   1.00%
#1970    203984000     2599000   1.29%
#1971    206827000     2843000   1.39%
#1972    209284000     2457000   1.19%
#1973    211357000     2073000   0.99%
#1974    213342000     1985000   0.94%
#1975    215465000     2123000   1.00%
#1976    217563000     2098000   0.97%
#1977    219760000     2197000   1.01%
#1978    222095000     2335000   1.06%
#1979    224567000     2472000   1.11%
#1980    227225000     2658000   1.18%
#1981    229466000     2241000   0.99%
#1982    231664000     2198000   0.96%
#1983    233792000     2128000   0.92%
#1984    235825000     2033000   0.87%
#1985    237924000     2099000   0.89%
#1986    240133000     2209000   0.93%
#1987    242289000     2156000   0.90%
#1988    244499000     2210000   0.91%
#1989    246819000     2320000   0.95%
#1990    249623000     2804000   1.14%

#Average Change = 2443875.0
#Minimum Change = 1881000 (1967)
#Maximum Change = 3185000 (1955)