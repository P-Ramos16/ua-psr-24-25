from readchar import readkey

def readAllUpTo(stop_char):
    key = ''

    while (key != stop_char):
        key = readkey()
        print(f"\nRead: {key}", end="")

    print(", stopping")

def main():
    print("Press a key: ", end="", flush=True)
    key = readkey()
    print(key)
    print(f"\nReading until '{key}' is pressed")
    readAllUpTo(key)

if __name__ == '__main__':
    main()
