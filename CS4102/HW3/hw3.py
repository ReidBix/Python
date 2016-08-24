__author__ = 'Reid'

import sys, math
from operator import itemgetter

def dist(x1, y1, x2, y2):
    d = round(math.hypot(x2 - x1, y2 - y1),4)
    return d

def closestP(list):
    minL = 10001
    minR = 10001
    minM = 10001
    numPoints = len(list)
    if numPoints <= 3:
        if numPoints == 2:
            minM = dist(list[0][0], list[0][1], list[1][0], list[1][1])
        if numPoints == 3:
            d01 = dist(list[0][0], list[0][1], list[1][0], list[1][1])
            d02 = dist(list[0][0], list[0][1], list[2][0], list[2][1])
            d12 = dist(list[1][0], list[1][1], list[2][0], list[2][1])
            minM = min(d01,d02,d12)
    else:
        cdsL = list[:int(len(list)/2)]
        cdsR = list[int(len(list)/2):]
        cdsM = []
        minL = closestP(cdsL)
        minR = closestP(cdsR)
        delta = min(minL,minR)
        for p in list:
            if abs(p[0]) < delta:
                cdsM.append(p)
        numM = len(cdsM)
        distsM = []
        if numM > 1:
            for i in range(numM-1):
                for j in range(i+1,min(i+8,numM)):
                    distsM.append(dist(cdsM[i][0],cdsM[i][1],cdsM[j][0],cdsM[j][1]))
            minM = min(distsM)
    return min(minL,minR,minM)


def main(argv):
    filename = sys.argv[1]
    try:
        fp = open(filename)
        for line in fp:
            cds = []
            numPoints = int(line)
            if numPoints == 0:
                break
            if numPoints < 2 or numPoints > 10000:
                print("The number of points must be between 2 and 10000")
                sys.exit()
            for i in range(numPoints):
                cString = fp.readline().split()
                cNums = [float(x) for x in cString if x]
                if cNums[0] < -50000 or cNums[0] > 50000 or cNums[1] < -50000 or cNums[1] > 50000:
                    print("The coordinates must be between -50000 and 50000")
                    sys.exit()
                tup = (cNums[0], cNums[1])
                cds.append(tup)
            sorted_c = sorted(cds, key=lambda x: x[1])
            #print(sorted_c)
            minN = closestP(sorted_c)
            if minN <= 10000:
                print("%.4f" % minN)
            else:
                print("infinity")
    except:
        print("File not found")
        sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
