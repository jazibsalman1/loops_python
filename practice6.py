class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)


    def __mul__(self, other):
        return complex(
            self.real * other.real - self.imag * other.imag,self.real * other.imag + self.imag * other.real)

    def __str__(self):
        return f"{self.real} + {self.imag}i"
jazib = complex(2, 3)
jazib2 = complex(4, 5)   
print(jazib + jazib2)    
print(jazib * jazib2)