__author__ = 'Reid'

"""The OurSet class is a user defined class of a set using the list class in Python"""
"""It contains the initializer, add, add_list, string, length, iterator, union, intersection"""
"""The class can be used in place of a mathematical representation of a set"""
class OurSet:

    """This constructor is used to initialize an empty set."""
    def __init__(self):
        self.set = []
        self.length = 0

    """If the parameter to this method is not already in the set object, add it to the set.  Return True or False to indicate if the item was added to the set."""
    def add(self, item):
        if item not in self:
            self.set.append(item)
            self.length += 1
            return True
        else:
            return False

    """Add each item in the list to the set, unless it already is in the set. Return True if any item was added the set, otherwise False."""
    def add_list(self, list):
        added = [False]
        for item in list:
            added.append(self.add(item))
        return any(added)

    """Return a string representation of the set, in a format like this:  <2, 5, 7, 11>"""
    def __str__(self):
        setString = "<"
        try:
            for item in self.set[:-1]:
                setString = setString + str(item) + ", "
            setString = setString + str(self.set[-1]) + ">"
        except:
            setString = "<>"
        return setString

    """Returns the number of items in the set object."""
    def __len__(self):
        return self.length

    """To allow you to use in and not in to process items in an OurSet object"""
    def __iter__(self):
        return iter(self.set)

    """Carry out a set-union operation between the current set object and the parameter. Return the union as the return value."""
    def union(self, set2):
        return self + set2

    """Carry out a set-intersection operation between the current set object and the parameter.  Return the intersection as the return value."""
    def intersection(self, set2):
        intList = OurSet()
        for item1 in self:
            for item2 in set2:
                if (item1 == item2):
                    intList.add(item1)
        return intList

    """Used to carry out the union by adding two sets together"""
    def __add__(self, set2):
        newSet = OurSet()
        for item1 in self:
            newSet.add(item1)
        for item2 in set2:
            newSet.add(item2)
        return newSet

def main():
    newSet = OurSet()
    newSet.add(1)
    assert len(newSet) == 1
    newSet.add(2)
    assert len(newSet) == 2
    newSet.add(3)
    assert len(newSet) == 3
    newSet.add(4)
    assert len(newSet) == 4
    newSet.add(5)
    assert len(newSet) == 5
    assert newSet.set == [1,2,3,4,5]
    assert str(newSet) == "<1, 2, 3, 4, 5>"
    newSet.add(1)
    assert len(newSet) == 5
    assert newSet.set == [1,2,3,4,5]
    assert str(newSet) == "<1, 2, 3, 4, 5>"
    newSet.add(2)
    assert len(newSet) == 5
    assert newSet.set == [1,2,3,4,5]
    assert str(newSet) == "<1, 2, 3, 4, 5>"
    newSet.add(-1)
    assert len(newSet) == 6
    assert newSet.set == [1,2,3,4,5,-1]
    assert str(newSet) == "<1, 2, 3, 4, 5, -1>"
    newSet2 = OurSet()
    newSet2.add_list([2,4,6,8,-10])
    assert len(newSet2) == 5
    assert newSet2.set == [2,4,6,8,-10]
    assert str(newSet2) == "<2, 4, 6, 8, -10>"
    unionSet = newSet.union(newSet2)
    assert len(unionSet) == 9
    assert unionSet.set == [1,2,3,4,5,-1,6,8,-10]
    assert str(unionSet) == "<1, 2, 3, 4, 5, -1, 6, 8, -10>"
    intersectionSet = newSet.intersection(newSet2)
    assert len(intersectionSet) == 2
    assert intersectionSet.set == [2,4]
    assert str(intersectionSet) == "<2, 4>"
    dupeSet = OurSet()
    dupeSet.add_list([44,8,6,3,22,5,-10,-1,1,17])
    unionSet2 = unionSet.union(dupeSet)
    assert len(unionSet2) == 12
    assert unionSet2.set == [1,2,3,4,5,-1,6,8,-10,44,22,17]
    assert str(unionSet2) == "<1, 2, 3, 4, 5, -1, 6, 8, -10, 44, 22, 17>"
    intersectionSet2 = dupeSet.intersection(newSet2)
    assert len(intersectionSet2) == 3
    assert intersectionSet2.set == [8,6,-10]
    assert str(intersectionSet2) == "<8, 6, -10>"
    return 0

if __name__ == "__main__":
        main()