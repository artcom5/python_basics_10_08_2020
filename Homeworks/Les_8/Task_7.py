"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение 
и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, real_p, imaginary_p):
        self.real_p = real_p
        self.imaginary_p = imaginary_p

    def __complex__(self):
        self.x = complex(self.real_p, self.imaginary_p)
        return self.x

    def __add__(self, other):
        return self.x + other.x

    def __rmul__(self, other):
        return self.x * other.x


c_1 = Complex(1, 4)
c_2 = Complex(2, 3)
print(complex(c_1) + complex(c_2))
print(complex(c_1) * complex(c_2))


