from readchar import readkey

def readAllUpTo(stop_char):
    key = ''

    while (key != stop_char):
        key = readkey()
        print(f"\nRead: {key}", end="")

    print(", stopping")

def main():
    key = readkey()
    print(f"Read to: {key}")
    readAllUpTo(key)

if __name__ == '__main__':
    main()
