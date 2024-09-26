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
    key = readkey()
    print(f"Read to: {key}")
    countNumbersUpto(key)

if __name__ == '__main__':
    main()
