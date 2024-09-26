#!/usr/bin/env python3
# --------------------------------------------------
# A simple python script to check perfect numbers
# Eurico Pedrosa.
# PSR, September 2024.
# --------------------------------------------------

import argparse
from my_functions import isPerfect 

def main(maximum_number):
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')
            #print(" + ".join([str(x) for x in [1, 2, 3]]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--max_number', dest='max_number', type=int, help='Set max_number')
    args = parser.parse_args()

    main(args.max_number)
