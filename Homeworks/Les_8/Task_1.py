"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Data:
    def __init__(self, data):
        if isinstance(data, str):
            self.data = data
            Data.data_int(data)
        else:
            raise ValueError('Это не строка')

    def __str__(self):
        return self.data

    @classmethod
    def data_int(cls, data):
        result = tuple(map(int, data.split('-')))
        return Data.data_validation(result)

    @staticmethod
    def data_validation(result):
        if result[0] in range(1, 32) and result[1] in range(1, 13) and result[2] in range(1945, 2100):
            print('Формат даты правильный')
        else:
            print('Исправьте дату')



if __name__ == '__main__':
    data_1 = Data('25-23-2020')
    print(data_1)


