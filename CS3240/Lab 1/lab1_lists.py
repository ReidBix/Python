__author__ = 'Reid'
def maxmin(list):
    if len(list) == 0:
        return None
    if (list[0] > list[1]):
        max = list.pop(0)
        min = list.pop(0)
    elif (list[0] < list[1]):
        min = list.pop(0)
        max = list.pop(0)
    else:
        max = list.pop(0)
        min = list.pop(0)
    size = len(list)
    for i in range (size):
        if max < list[0]:
            max = list.pop(0)
        elif min > list[0]:
            min = list.pop(0)
        else:
            list.pop(0)
    return (max,min)

def commonitems(list1, list2):
    complist = []
    for item1 in list1:
        for item2 in list2:
            if (item1 == item2):
                if item1 not in complist:
                    complist.append(item1)
    return complist

if __name__ == "__main__":
    print(maxmin([1,3,3]))
    print(maxmin([3,1,-2]))
    print(maxmin(['Q','Z','C','A']))
    print(commonitems([1,3,3],[3,1,-2]))