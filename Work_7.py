class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        result_1 = self.a * other.a
        result_2 = self.a * other.b
        result_3 = self.b * other.a
        result_4 = other.b * self.b
        return ComplexNumber(result_1 - result_4, result_2 + result_3)

    def __str__(self):
        return f'{self.a} + {self.b}i'


num1 = ComplexNumber(2, 5)
num2 = ComplexNumber(7, 3)
print(num1 + num2)
print(num1 * num2)
