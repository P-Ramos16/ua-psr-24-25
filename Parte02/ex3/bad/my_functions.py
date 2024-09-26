import math

def getDividers(value):
    """
    Return a list of dividers for the number value
    :param value: the number to test
    :return: a list of dividers.
    """

    squareRoot = math.ceil( value ** (1/2) )

    print("val: " + str(value) +  " | root: " + str(squareRoot))

    return [x for x in range(1, squareRoot + 1) if value % x == 0]

def isPerfect(value):
    """
    Checks whether the number value is perfect.
    :param value: the number to test.
    :return: True or False
    """
    
    divisorList = getDividers(value)

    return sum(divisorList) == value
