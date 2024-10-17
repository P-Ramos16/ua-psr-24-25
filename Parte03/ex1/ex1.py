from time import time, ctime, sleep
from colorama import Fore, Back, Style

#  Python rich can also be used instead of colorama

global ticTime, tocTime

def tic():
    global ticTime
    ticTime = time()
    print(f"\n -> {Fore.GREEN}Start time: {Back.GREEN}{Fore.BLACK}{ctime()}{Back.RESET}{Fore.RESET}")

def toc():
    global ticTime, tocTime
    tocTime = time()

    print(f" -> {Fore.GREEN}Stop time:  {Back.GREEN}{Fore.BLACK}{ctime()}{Back.RESET}{Fore.RESET}")
    print(f" => {Fore.RED}Time spent: {Back.RED}{Fore.BLACK}{tocTime - ticTime}{Back.RESET} seconds{Fore.RESET}\n")


def calcSqRootUntil(max_value):
    print(f"{Fore.CYAN}")
    for num in range(0, max_value + 1):
        v = num**(1/2)
        if (num % 500000 == 0):
            print(f"   √{num : 8} = {v : >6.1}\n", end="")
        #  Go to start of line
        #print("\033[F", end="", flush=True)
    print(f"\n => √{max_value} = {v}{Fore.RESET}\n")


def main():
    #  Pretty print: 56.743205547332764
    #  Format print: 35.2231707572937
    #  Ugly print:   31.837557077407837
    #  No print:      1.0035498142242432
    #  Every 100:     1.83366060256958
    #  Every 1000:    1.4782805442810059
    #  Every 10000:   1.4789955615997314
    #  Every 500000: 1.4691739082336426

    tic()

    calcSqRootUntil(5000000)

    toc()

if __name__ == '__main__':
    main()
