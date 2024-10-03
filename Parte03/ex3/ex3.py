from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])

def addComplex(x,y):
    #  Seperate the real from the imaginary part
    xr, xi = x
    yr, yi = y

    return Complex(xr + yr, xi + yi)


def multiplyComplex(x,y):
    #  Seperate the real from the imaginary part
    xr, xi = x
    yr, yi = y

    realPart = xr * yr - xi * yi
    imagPart = xr * yi + xi * yr

    return Complex(realPart, imagPart)


def printComplex(x):
    #  Seperate the real from the imaginary part
    xr, xi = x

    if xi >= 0:
        print(f"{xr} + {xi}i")
    else:
        print(f"{xr} - {-xi}i")
    
    print(str(x))

def main():
    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3) # use order when not naming
    c2 = Complex(i=7, r=-2) # if items are names order is not relevant
    print('c1 = ' + str(c1)) # named tuple looks nice when printed
    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)
    # test multiply
    printComplex(multiplyComplex(c1, c2))
    
if __name__ == '__main__':
    main()