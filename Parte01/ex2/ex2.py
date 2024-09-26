#!/usr/bin/env python3

m = 10000

def isPrime(val):
    for num in range (2, int(val+1/2)):

        if val % num == 0:
            return False

    return True


def main():
    for i in range(0, m):
        if isPrime(i):
            print(f"Num {i} is prime!")

        else:
            print(f"Num {i} is not prime!")

if __name__ == "__main__":
    main()
