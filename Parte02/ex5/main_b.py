from readchar import readkey

def countNumbersUpto(stop_char):
    key = ''
    inputs = []

    while (key != stop_char):
        key = readkey()
        inputs += key
        print(f"\nRead: {key}", end="")


    numericInputs = []
    otherInputs = []

    for input in inputs:
        if (input.isnumeric()):
            numericInputs += input
            
        else:
            otherInputs += input

    print(", stopping\n")
    print('You entered ' + str(len(numericInputs)) + ' numbers.')
    print('You entered ' + str(len(otherInputs)) + ' others.')

def main():
    print("Press a key: ", end="", flush=True)
    key = readkey()
    print(key)
    print(f"\nReading until '{key}' is pressed")
    countNumbersUpto(key)

if __name__ == '__main__':
    main()
