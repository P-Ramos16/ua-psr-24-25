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
    key = readkey()
    print(f"Read to: {key}")
    countNumbersUpto(key)

if __name__ == '__main__':
    main()
