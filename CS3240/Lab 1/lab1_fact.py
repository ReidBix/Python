__author__ = 'Reid'

def factorial1(n):
    try:
        if (n<0):
            raise ValueError
        elif (n==0):
            return 1
        else:
            return factorial1(n-1)*n
    except ValueError:
        print("You cannot have a factorial of a negative number!")

def factorial2(n):
    nums = []
    for i in range (0,n+1):
        nums.append(factorial1(i))
    return nums

def test_fact1():
    x = 10
    num = factorial2(x)
    for i in range (x+1):
        assert factorial1(i) == num[i]

if __name__ == "__main__":
    print(factorial1(0))
    print(factorial1(1))
    print(factorial1(5))
    print(factorial1(-4))
    print(factorial2(5))
    print(test_fact1())
