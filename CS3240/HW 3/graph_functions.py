__author__ = 'rmb3yz'

from graph import Graph


def is_complete(grph):
    try:
        if not isinstance(grph, Graph):
            raise TypeError
        fullList = []
        for n in grph:
            fullList.append(n)
        complete = [True]
        if len(grph) == 0 or len(grph) == 1:
            return True
        for g in grph:
            adjlist = grph.get_adjlist(g)
            adjlist.append(g)
            if (set(fullList) == set(adjlist)):
                complete.append(True)
            else:
                complete.append(False)
        return all(complete)
    except TypeError:
        print("The value passed was not of the type Graph!")


def nodes_by_degree(grph):
    try:
        if not isinstance(grph, Graph):
            raise TypeError
        l = []
        for n in grph:
            l.append((n, len(grph.get_adjlist(n))))
        sortedL = sorted(l, key=lambda x: (-x[1], x[0]))
        return sortedL
    except TypeError:
        print("The value passed was not of the type Graph!")
