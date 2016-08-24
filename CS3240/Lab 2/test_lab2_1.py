__author__ = 'Reid'

from hw2_p2 import OurSet

def test_add():
    """Q1,Q2,Q3,Q5,Q5: test adding to queues"""
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

def test_set():
    """Q6: test calling remove on empty queue"""
    newSet = OurSet([1,2,3,4,5])
    assert newSet.set == [1,2,3,4,5]

def test_string():
    """Q7: test calling remove on queue of size 1"""
    newSet = OurSet([1,2,3,4,5])
    assert str(newSet) == "<1, 2, 3, 4, 5>"

def main():
   test_add()
   test_set()
   test_string()

if __name__ == '__main__':
    main()
