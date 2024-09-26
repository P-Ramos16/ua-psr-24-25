#!/usr/bin/env python3
# --------------------------------------------------
# A simple python script to check perfect numbers
# Eurico Pedrosa.
# PSR, September 2024.
# --------------------------------------------------

maximum_number = 100  # maximum number to test.

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

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')

if __name__ == "__main__":
    main()
