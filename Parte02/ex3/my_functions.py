import math

def isPrimo(value):
    """
    Return a list of dividers for the number value
    :param value: the number to test
    :return: a list of dividers.
    """

    squareRoot = math.ceil(value ** (1/2)) 

    for num in range (2, squareRoot):
        if value % num == 0:
            return False

    return True
