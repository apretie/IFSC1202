class Sketch ():
    def __init__(self, size):
        self.Size = size
        self.Xpos = 0
        self.Ypos = 0
        self.Direction = "U"
        self.Pen = "U"
        self.Canvas = []
        for i in range(self.Size):
            self.Canvas.append([" "] * self.Size)
    def printsketch(self):
        print("+{}+".format("-"*self.Size))
        for i in range(len(self.Canvas)-1,-1,-1):
            lines = str(i)
            print("|", end='')
            for j in range(len(self.Canvas[i])):
                print(self.Canvas[i][j], end='')
            print("|")
        print("+{}+".format("-"*self.Size))
        print("X = {}  Y = {}  Direction = {}".format(self.Xpos,self.Ypos,self.Direction))
    def penup(self):
        self.Pen = "U"
    def pendown(self):
        self.Pen = "D"
    def turnleft(self):
        if self.Direction == "U":
            self.Direction = "L"
        elif self.Direction == "L":
            self.Direction = "D"
        elif self.Direction == "D":
            self.Direction = "R"
        elif self.Direction == "R":
            self.Direction = "U"
    def turnright(self):
        if self.Direction == "U":
            self.Direction = "R"
        elif self.Direction == "R":
            self.Direction = "D"
        elif self.Direction == "D":
            self.Direction = "L"
        elif self.Direction == "L":
            self.Direction = "U"
    def move(self, distance):
        min = 0
        max = self.Size - 1
        if self.Direction == "R":
            if self.Ypos + distance < max:
                max = self.Ypos + distance
            while self.Ypos < max:
                if self.Pen == "D":
                    self.Canvas[self.Xpos][self.Ypos] = "*"
                self.Ypos += 1
        elif self.Direction == "U":
            if self.Xpos + distance < max:
                max = self.Xpos + distance
            while self.Xpos < max:
                if self.Pen == "D":
                    self.Canvas[self.Xpos][self.Ypos] = "*"
                self.Xpos += 1
        elif self.Direction == "L":
            if self.Ypos - distance > min:
                min = self.Ypos - distance
            while self.Ypos > min:
                if self.Pen == "D":
                    self.Canvas[self.Xpos][self.Ypos] = "*"
                self.Ypos -= 1
        elif self.Direction == "D":
            if self.Xpos - distance > min:
                min = self.Xpos - distance
            while self.Xpos > min:
                if self.Pen == "D":
                    self.Canvas[self.Xpos][self.Ypos] = "*"
                self.Xpos -= 1
#main start
textfile = open("/workspace/IFSC1202/Cshape.txt", 'r')
line = textfile.readline()
Cshape = Sketch(int(line))

line = textfile.readline()
y=[]
while line != "":
    y = line.split(",")
    command = int(y[0].strip())
    if command == 1:
        Cshape.penup()
    elif command == 2:
        Cshape.pendown()
    elif command == 3:
        Cshape.turnright()
    elif command == 4:
        Cshape.turnleft()
    elif command == 5:
        Cshape.move(int(y[1].strip()))
    elif command == 6:
        Cshape.printsketch()
    line = textfile.readline()

textfile.close()

Cshape.printsketch()