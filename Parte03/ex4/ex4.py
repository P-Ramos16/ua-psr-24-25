class Complex:
    def __init__(self, r, i):
        self.r = r #  Store the real part of the number
        self.i = i #  Store the imaginary part of the number

    def add(self, y):
        #  Seperate the real from the imaginary part
        yr, yi = y.r, y.i

        self.r += yr
        self.i += yi


    def multiply(self, y):
        #  Seperate the real from the imaginary part
        yr, yi = y.r, y.i

        realPart = self.r * yr - self.i * yi
        imagPart = self.r * yi + self.i * yr

        self.r = realPart
        self.i = imagPart


    def __str__(self):
        #  Seperate the real from the imaginary part

        if self.i >= 0:
            return f"{self.r} + {self.i}i"
        else:
            return f"{self.r} - {-self.i}i"

def main():
    # declare two instances of class two complex numbers as tuples of size two
    c1 = Complex(5, 3) # use order when not naming
    c2 = Complex(i=7, r=-2) # if items are names order is not relevant
    # Test add
    print(c1) # uses the __str__ method in the class
    c1.add(c2)
    print(c1) # uses the __str__ method in the class
    # test multiply
    print(c2) # uses the __str__ method in the class
    c2.add(c1)
    print(c2) # uses the __str__ method in the class

if __name__ == '__main__':
    main()