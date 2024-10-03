def addComplex(x,y):
    #  Seperate the real from the imaginary part
    xr, xi = x
    yr, yi = y

    return (xr + yr, xi + yi)


def multiplyComplex(x,y):
    #  Seperate the real from the imaginary part
    xr, xi = x
    yr, yi = y

    realPart = xr * yr - xi * yi
    imagPart = xr * yi + xi * yr

    return (realPart, imagPart)


def printComplex(x):
    #  Seperate the real from the imaginary part
    xr, xi = x

    if xi >= 0:
        print(f"{xr} + {xi}i")
    else:
        print(f"{xr} - {-xi}i")

def main():
    #  Define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    #  Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    #  Test multiply
    printComplex(multiplyComplex(c1, c2))



    x = (3, 2)
    y = (1, 7)

    z = addComplex(x, y)
    w = multiplyComplex(x, y)

    printComplex(z)
    printComplex(w)

    a = (1, 1)
    a2 = multiplyComplex(a, a)
    printComplex(a2)


if __name__ == '__main__':
    main()