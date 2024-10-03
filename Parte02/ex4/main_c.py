from readchar import readkey

def countNumbersUpto(stop_char):
    key = ''
    total_numbers = 0
    total_others = 0

    while (key != stop_char):
        key = readkey()
        print(f"\nRead: {key}", end="")

        if (key.isnumeric()):
            total_numbers += 1
        else:
            total_others += 1

    print(", stopping\n")
    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')

def main():
    print("Press a key: ", end="", flush=True)
    key = readkey()
    print(key)
    print(f"\nReading until '{key}' is pressed")
    countNumbersUpto(key)

if __name__ == '__main__':
    main()
