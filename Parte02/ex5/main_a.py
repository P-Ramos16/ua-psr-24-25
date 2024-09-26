from readchar import readkey

def countNumbersUpto(stop_char):
    key = ''
    inputs = []

    while (key != stop_char):
        key = readkey()
        inputs += key
        print(f"\nRead: {key}", end="")


    total_numbers = 0
    total_others = 0

    for input in inputs:
        if (input.isnumeric()):
            total_numbers += 1
        else:
            total_others += 1

    print(", stopping\n")
    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')

def main():
    key = readkey()
    print(f"Read to: {key}")
    countNumbersUpto(key)

if __name__ == '__main__':
    main()
