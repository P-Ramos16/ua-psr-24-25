def getDividers(value):
    """
    Return a list of dividers for the number value
    :param value: the number to test
    :return: a list of dividers.
    """

    halfway = int( (value + 1) / 2) + 1

    return [x for x in range(1, halfway) if value % x == 0]

def isPerfect(value):
    """
    Checks whether the number value is perfect.
    :param value: the number to test.
    :return: True or False
    """
    
    divisorList = getDividers(value)

    # your code here
    return sum(divisorList) == value

