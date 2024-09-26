#!/usr/bin/env python3
# --------------------------------------------------
# A simple python script to check perfect numbers
# Eurico Pedrosa.
# PSR, September 2024.
# --------------------------------------------------

from my_functions import isPerfect 

maximum_number = 100  # maximum number to test.

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')

if __name__ == "__main__":
    main()
