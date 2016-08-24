__author__ = 'Reid'

import sys

grid = []
long = []
rM = None
cM = None

def pathRecurse(r, c):
    global long
    #print("Enter: pathRecurse")
    #print("Looking at " + str(r) + " " + str(c) + " with value " + str(grid[r][c]))
    if (long[r][c] == 0):
        m = 0
        #print("Value at " + str(r) + " " + str(c) + " is 0")
        up, right, down, left = 0,0,0,0
        if (c-1 >= 0):
            if (grid[r][c-1] < grid[r][c]):
                #print( str(grid[r][c-1]) + " is less than " + str(grid[r][c]))
                left = pathRecurse(r,c-1)
                #print("left is " + str(left))
        if (r+1 < rM):
            if (grid[r+1][c] < grid[r][c]):
                #print( str(grid[r+1][c]) + " is less than " + str(grid[r][c]))
                down = pathRecurse(r+1,c)
                #print("down is " + str(down))
        if (c+1 < cM):
            if(grid[r][c+1] < grid[r][c]):
                #print( str(grid[r][c+1]) + " is less than " + str(grid[r][c]))
                right = pathRecurse(r,c+1)
                #print("right is " + str(right))
        if (r-1 >= 0):
            if(grid[r-1][c] < grid[r][c]):
                #print( str(grid[r-1][c]) + " is less than " + str(grid[r][c]))
                up = pathRecurse(r-1,c)
                #print("up is " + str(up))
        m = max(up, right, down, left)
        long[r][c] = m + 1
        #print("max value is " + str(long[r][c]))
        #print(long)
    return long[r][c]

def main(argv):
    filename = sys.argv[1]
    try:
        fp = open(filename)
        numCases = int(fp.readline())
        for line in fp:
            infoString = line.split()
            title = infoString[0]
            rows = int(infoString[1])
            cols = int(infoString[2])
            if rows > 100 or cols > 100:
                print("The rows and columns must be no greater than 100")
                sys.exit()
            if rows < 1 or cols < 1:
                print("The rows and columns must be positive integers")
                sys.exit()
            global grid
            global long
            global rM
            global cM
            rM = rows
            cM = cols
            long = [[0 for x in range(rows)] for x in range(cols)]
            for r in range(rows):
                row = (fp.readline()).split()
                rowNum = [int(rx) for rx in row]
                grid.append(rowNum)
            max = 0
            for i in range(rM):
                for j in range(cM):
                    v = pathRecurse(i,j)
                    if (v > max):
                        max = v
            print(title + ": " + str(max))
            grid.clear()
            long.clear()

    except:
        print("File not found")
        sys.exit()

if __name__ == "__main__":
     main(sys.argv[1:])