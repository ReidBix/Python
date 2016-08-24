__author__ = 'Reid'


"""maxmin is used to return the maximum and minimum of a given list"""
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

"""common_items is used to return all of the common items found in two lists"""
def common_items(list1, list2):
    compList = []
    for item1 in list1:
        for item2 in list2:
            if (item1 == item2):
                if item1 not in compList:
                    compList.append(item1)
    return compList
"""notcommon_items is used to return all of the not common items found in two lists"""
def notcommon_items(list1, list2):
    nonList = list1 + list2
    comList = common_items(list1, list2)
    for item1 in comList:
        if item1 in nonList:
            nonList = [x for x in nonList if x != item1]
    return nonList

"""count_list_items is used to return the count of the individual items in a list"""
def count_list_items(list):
    dict = {}
    for item in list:
        if item not in dict:
            dict[item] = 0
        if item in dict:
            num = dict[item]
            num += 1
            dict[item] = num
    return dict

if __name__ == "__main__":
    print(maxmin([1,3,3]))
    print(maxmin([3,1,-2]))
    print(maxmin(['Q','Z','C','A']))
    print(common_items([1,3,3],[3,1,-2]))
    print(notcommon_items([1,3,3,5,6,3,2,4,5],[3,1,-2,1,5,6,3,4,-1]))
    print(count_list_items([1,3,3,5,6,3,2,4,5,3,1,-2,1,5,6,3,4,-1]))