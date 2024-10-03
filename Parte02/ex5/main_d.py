from readchar import readkey

def countNumbersUpto(stop_char):
    key = ''
    inputs = []

    while (key != stop_char):
        key = readkey()
        inputs += key
        print(f"\nRead: {key}", end="")


    numericInputs = []
    otherInputs = {}

    for inputID in range(0, len(inputs)):
        
        input = inputs[inputID]

        if (input.isnumeric()):
            numericInputs.append(int(input))
        else:
            otherInputs[inputID] = input

    print(", stopping\n")
    print('You entered ' + str(len(numericInputs)) + ' numbers.')
    print('You entered ' + str(len(otherInputs.items())) + ' others.')
    numericInputs.sort()
    print(otherInputs)
    print(numericInputs)


def main():
    print("Press a key: ", end="", flush=True)
    key = readkey()
    print(key)
    print(f"\nReading until '{key}' is pressed")
    countNumbersUpto(key)

if __name__ == '__main__':
    main()
