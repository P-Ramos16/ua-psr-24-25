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
    print(otherInputs)
    print(numericInputs)
    print(numericInputs.sort())


def main():
    key = readkey()
    print(f"Read to: {key}")
    countNumbersUpto(key)

if __name__ == '__main__':
    main()
