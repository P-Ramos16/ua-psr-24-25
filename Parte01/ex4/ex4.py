#!/usr/bin/env python3

maximum_number = 100

def isPerfect(value):
   
    halfway = int( (value + 1) / 2 ) + 1

    diviList = [x for x in range(1, halfway) if value % x == 0]

    return sum(diviList) == value

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')

if __name__ == "__main__":
    main()
