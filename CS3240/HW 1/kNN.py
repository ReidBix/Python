__author__ = 'Reid'

import math, sys, random

class Point:
    def __init__(self, category, x, y):
        self.cat = category
        self.x = x
        self.y = y
        self.neighbors = []

    def dist(self,point):
        d = math.hypot(point.x - self.x, point.y - self.y)
        return d
    def printPointt(self, d):
        print("\t\t" + str(self.cat) + " " + str(self.x) + " " + str(self.y), d)
    def printPoint(self):
        string = str(self.cat) + " " + str(self.x) + " " + str(self.y) + "\n"
        #print("\t\t" + str(self.cat) + " " + str(self.x) + " " + str(self.y))
        return string

def randomPoints():
    textFile = open("testR.txt", "w")
    randomList = []
    num = random.randint(1,50)
    for n in range(num):
        x = random.uniform(-50,50)
        y = random.uniform(-50,50)
        if random.choice((True,False)):
            cat = "cat1"
        else:
            cat = "cat2"
        p = Point(cat,x,y)
        randomList.append(p)
    for r in randomList:
        string = r.printPoint()
        textFile.write(string)
    textFile.close()
    return

def main():
    #randomPoints()
    k = 'a'
    kFail = True
    while (kFail):
        try:
            k = int(input("Value of k: "))
            if (k > 0):
                kFail = False
        except:
            kFail = True
    k = int(k)
    M = 'a'
    MFail = True
    while (MFail):
        try:
            M = int(input("Value of M: "))
            if (M > 0):
                MFail = False
        except:
            MFail = True
    M = int(M)
    fileNotFound = True
    while fileNotFound:
        filename = input("Data file name: ")
        try:
            fp = open(filename)
            fileNotFound = False
        except:
            print("File not found")
            fileNotFound = True
    pointMap = []
    count = 0
    for line in fp:
        if count >= M:
            break
        infoString = line.split()
        point = Point(infoString[0],float(infoString[1]),float(infoString[2]))
        pointMap.append(point)
        count += 1
    pointList = []
    num = 1
    print("Type \"1.0 1.0\" to finish inputting points")
    while (True):
        xyString = input("________________\nNew Data Point " + str(num) + " \nx y: ")
        xy = xyString.split()
        if (len(xy) == 2):
            try:
                x = float(xy[0])
                try:
                    y = float(xy[1])
                    if (x == 1.0 and y == 1.0):
                        break
                    newPoint = Point("cat0",x,y)
                    pointList.append(newPoint)
                    num += 1
                except ValueError:
                    print("y was not a float value")
            except ValueError:
                print("x was not a float value!")
        else:
            print("Too many or too few values!")
    for p1 in pointList:
        for p2 in pointMap:
            d = p1.dist(p2)
            pair = (p2, d)
            p1.neighbors.append(pair)
    nm = 1
    print("\n")
    for p1 in pointList:
        print("For unclassified data value " + str(nm) + " at point (" + str(p1.x) + "," + str(p1.y) + "):")
        p1.neighbors = sorted(p1.neighbors,key=lambda x: x[1])
        print("\tThe " + str(k) + " nearest neighbors are:")
        cat1ct = 0
        cat1avg = 0

        cat2ct = 0
        cat2avg = 0
        for ne in range(k):
            ne = p1.neighbors[ne]
            ne[0].printPointt(("%.5f" % ne[1]).rstrip('0').rstrip('.'))
            if(ne[0].cat == "cat1"):
                cat1ct += 1
                cat1avg += ne[1]
            elif(ne[0].cat == "cat2"):
                cat2ct += 1
                cat2avg += ne[1]
            else:
                print("\t\tThis was not cat1 or cat2!")
        if (cat1ct > cat2ct):
            p1.cat = "cat1"
        elif (cat2ct > cat1ct):
            p1.cat = "cat2"
        else:
            print("There was an equal number of categories!")
            p1.cat = "cat0"
        print("\tData item (" + str(p1.x) + "," + str(p1.y) + ") assigned to: " + p1.cat)
        try:
            cat1avg = float(cat1avg/cat1ct)
        except:
            cat1avg = float(cat1avg)
        try:
            cat2avg = float(cat2avg/cat2ct)
        except:
            cat2avg = float(cat2avg)
        print("\tAverage distance to cat1 items: " + ("%.5f" % cat1avg).rstrip('0').rstrip('.'))
        print("\tAverage distance to cat2 items: " + ("%.5f" % cat2avg).rstrip('0').rstrip('.'))
        nm += 1
    print("Done")
    return

if __name__ == "__main__":
    main()
