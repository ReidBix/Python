__author__ = 'Reid'

import sys, math

def main(argv):
    filename = sys.argv[1]
    try:
        fp = open(filename)
        numCases = int(fp.readline())
        caseNum = 1
        for line in fp:
            print("Case " + str(caseNum))
            infoString = line.split()
            infoNum = [int(x) for x in infoString]
            boxesToMove = infoNum[0]
            mustTake = infoNum[1]
            compNum = infoNum[2]
            mapping = {}
            for i in range(compNum):
                compString = fp.readline().split()
                company = compString[0]
                chargeX = int(compString[1])
                chargeY = int(compString[2])
                charge = 0
                b = boxesToMove
                #print(company)
                #print("Boxes to move is " + str(boxesToMove))
                #print("Must take " + str(mustTake))
                #print("Number of companies " + str(compNum) + "\n")
                while(b != mustTake):
                    half = math.ceil(b/2)
                    #print("Half of " + str(b) + " boxes is " + str(half))
                    if (b-half)>mustTake:
                        #print(str(b) + " - " + str(half) + " > " + str(mustTake))
                        #print(str(b-half) + " > " + str(mustTake))
                        charge += chargeY
                        #print("Charging " + str(chargeY) + " for half")
                        b -= half
                    elif b > mustTake:
                        #print(str(b) + " > " + str(mustTake))
                        while b > mustTake:
                            #print("Charging " + str(chargeX) + " for one")
                            charge += chargeX
                            b -= 1
                            #print(str(b) + " boxes remain")
                    else:
                        brk = 1
                    #print("Charge is " + str(charge) + "\n")
                #print(company + " " + str(charge))
                mapping.update({company : charge})

            sorted_m = sorted(mapping.items(), key=lambda l: (l[1], l[0]))
            for k,v in sorted_m:
                print(str(k) + " " + str(v))
            caseNum += 1

    except:
        print("File not found")
        sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])