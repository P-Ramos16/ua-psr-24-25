from readchar import readkey

def printAllCharsUpTo(stop_char):
    
    for charID in range(ord(' '), ord(stop_char)):
        print(chr(charID), end="-")

    print(stop_char)

    return

def main():
    key = readkey()
    printAllCharsUpTo(key)

if __name__ == '__main__':
    main()
