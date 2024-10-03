from readchar import readkey

def countNumbersUpto(stop_char):
    key = ''
    inputs = []

    while (key != stop_char):
        key = readkey()
        inputs += key
        print(f"\nRead: {key}", end="")


    otherInputs = []
    numericInputs = []


    [numericInputs.append(inp) if inp.isnumeric() else otherInputs.append(inp) for inp in inputs ]


    print(", stopping\n")
    print('You entered ' + str(len(numericInputs)) + ' numbers.')
    print('You entered ' + str(len(otherInputs)) + ' others.')
    print(numericInputs)
    print(otherInputs)

def main():
    print("Press a key: ", end="", flush=True)
    key = readkey()
    print(key)
    print(f"\nReading until '{key}' is pressed")
    countNumbersUpto(key)

if __name__ == '__main__':
    main()
