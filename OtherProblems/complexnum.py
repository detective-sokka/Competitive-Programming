class ComplexNumber:
    """ This is a class ComplexNumber that is implementing complex numbers """
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def __add__(self, complexNum):
        result = ComplexNumber(self.real, self.imag)
        result.real += complexNum.real
        result.imag += complexNum.imag
        return result

    def getData(self):
        print("{0}+{1}j".format(self.real, self.imag))

    def changeNum(self, r, i):
        self.real = r
        self.imag = i


complexNum1 = ComplexNumber(10, 5)

complexNum1.getData()

complexNum2 = ComplexNumber(2, 3)

complexNum2.changeNum(10, 20)

complexSum = complexNum1 + complexNum2
complexSum.getData()

del complexNum1.real
del complexNum1.imag
del complexNum2
# the binding to the object is removed however it continues to
# remain in memory. Later during garbage collection it gets deleted

