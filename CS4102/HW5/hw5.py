__author__ = 'Reid'

import sys

from collections import defaultdict

def dfs_recurse(m, s, t, p):
    if s == t:
        return p
    for key, value in m.items():
        if (key[0] == s):
            rCap = m[key][1] - m[key][0]
            if key not in p:
                if rCap > 0:
                    nS = key[1]
                    nP = p + [key]
                    fP = dfs_recurse(m, nS, t, nP)
                    if fP != None:
                        return fP

def main(argv):
    filename = sys.argv[1]
    fp = open(filename)
    for line in fp:
        infoString = line.split()
        infoNum = [int(x) for x in infoString]
        r = infoNum[0]
        c = infoNum[1]
        n = infoNum[2]
        matrix = defaultdict(int)
        flow = defaultdict(int)
        res = defaultdict(int)
        maxList = []
        edges = []
        final = "Yes"
        if (r == 0 and c == 0 and n == 0):
            break
        for i in range(r):
            regString = fp.readline().split()
            name = regString[0]
            className = "_" + regString[1]
            edges.append((name, className))
            if (not ('s', name) in edges):
                edges.append(('s', name))
            if (not (className, 't') in edges):
                edges.append((className, 't'))
        for j in range(c):
            classString = fp.readline().split()
            className = "_" + classString[0]
            max = int(classString[1])
            maxList.append((className, max))
        fp.readline()
        for e in edges:
            matrix[e] += 1
            if (e[0] == 's'):
                flow[e] = (0,n)
                flow[e[1],e[0]] = (0,0)
                res[e] = n
            elif (e[1] == 't'):
                for m in maxList:
                    if m[0] == e[0]:
                        flow[e] = (0,m[1])
                        flow[e[1],e[0]] = (0,0)
                        res[e] = m[1]
            else:
                flow[e] = (0,1)
                flow[e[1],e[0]] = (0,0)
                res[e] = 1
        check = defaultdict(int)
        for key, value in matrix.items():
            if ((not (key[0] == 's')) and (not (key[1] == 't'))):
                check[key[0]] += 1
        for key, value in check.items():
            if (check[key] < n):
                final = "No"
        path = []
        path = dfs_recurse(flow, 's', 't', path)
        while (path != None):
            rNums = []
            for p in path:
                rNums += [flow[p][1] - flow[p][0]]
            f = min(rNums)
            for p in path:
                flow[p] = (flow[p][0] + f, flow[p][1])
                flow[p[1],p[0]] = (flow[p[1],p[0]][0]-f, flow[p[1],p[0]][1])
            path.clear()
            path = dfs_recurse(flow, 's', 't', path)
        stud = len(check)
        total = stud * n
        sum = 0
        for key, value in flow.items():
            if (key[0] == 's'):
                sum += flow[key][0]
        if (total == sum):
            final = "Yes"
        elif (total < sum or total > sum):
            final = "No"
        print(final)
        
if __name__ == "__main__":
     main(sys.argv[1:])