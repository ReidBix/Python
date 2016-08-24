__author__ = 'Reid'

import sys, locale

def main(argv):
    x = 0
    filename = sys.argv[1]
    try:
        fp = open(filename)

    except:
        print("File not found")
        x = -1
    while x != -1.00:
        x = 0
        broke = False
        while(x < 0 or x > 1000000000 or not isinstance(x, float)):
            try:
                x = float(fp.readline())
                if x == -1:
                    broke = True
                    break
            except:
                print("That was not a valid input.")
                x = -0.1
        if broke:
            break
        numQ = 0
        numD = 0
        numN = 0
        numP = 0
        y = round(x%1, 2)
        while y > .24:
            y -= .25
            numQ += 1

        while y > .09:
            y -= .10
            numD += 1

        while y > .04:
            y -= .05
            numN += 1

        while y > .00:
            y-= .01
            numP += 1

        stringQ = ""
        stringD = ""
        stringN = ""
        stringP = ""

        while numQ > 0:
            stringQ += " Q"
            numQ -= 1

        while numD > 0:
            stringD += " D"
            numD -= 1

        while numN > 0:
            stringN += " N"
            numN -= 1

        while numP > 0:
            stringP += " P"
            numP -= 1

        locale.setlocale(locale.LC_ALL, '')
        'English_United States.1252'
        stringMoney = locale.currency(x, grouping=True)
        if round(x%1,2) != 0:
         print(stringMoney + stringQ + stringD + stringN + stringP)
        else:
            print(stringMoney.strip())


if __name__ == "__main__":
    main(sys.argv[1:])