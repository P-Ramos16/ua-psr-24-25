#!/usr/bin/env python3

from colorama import Fore, Back, Style

m = 100

def isPrime(val):
    
    isP = True

    for num in range (2, int(val+1/2)):
        if val % num == 0:
            if isP:
                print(Fore.RESET + f"Num {val} can be divided by {num}", end = "")
            else:
                print(f", {num}", end="")
            isP = False

    if not isP:
        print("!")
    
    return isP


def main():
    for i in range(0, m):
        if isPrime(i):
            print(Fore.GREEN + f"Num {i} is prime!")

        #else:
            #print(f"Num {i} is not prime!")

if __name__ == "__main__":
    main()
