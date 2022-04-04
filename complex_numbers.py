from __future__ import annotations


class Complex:
    def __init__(self, real=0.0, img=0.0):
        self.real = real
        self.img = img

    def __add__(self, other: Complex):
        return Complex(self.real + other.real, self.img + other.img)

    def __sub__(self, other: Complex):
        return Complex(self.real - other.real, self.img - other.img)

    def __mul__(self, other: float):
        return Complex(self.real * other, self.img * other)

    def __truediv__(self, other: float):
        return Complex(self.real/other, self.img/other)

    def __str__(self):
        if self.img < 0:
            return f'{self.real} - {-self.img}i'
        else:
            return f'{self.real} + {self.img}i'


c1 = Complex(5, 10)
c2 = Complex(-2, 14)


print(f'Complex Number c1: {c1}')
print(f'Complex Number c2: {c2}')

print(f'c1 + c2 = {c1 + c2}')
print(f'c1 - c2 = {c1 - c2}')
print(f'c1 * 5 = {c1 * 5}')
print(f'c1 / 2 = {c1 / 2}')
