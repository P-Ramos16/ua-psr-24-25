#!/usr/bin/env python3
# --------------------------------------------------
# A simple python script to check perfect numbers
# Eurico Pedrosa.
# PSR, September 2024.
# --------------------------------------------------

import argparse
from my_functions import isPrimo 

maximum_number = 100  # maximum number to test.

def main(maximum_number):
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPrimo(i):
            print('Number ' + str(i) + ' is perfect.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--max_number', dest='max_number', type=int, help='Set max_number')
    args = parser.parse_args()

    main(args.max_number)

