"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroError(Exception):
    def __init__(self, text):
        self.text = text


def main():

    try:
        num_1 = float(input('Введите делимое: '))
        num_2 = float(input('Ведите делимое: '))
        if num_2 == 0:
            raise ZeroError('Вы ввели 0!')
        print(f'Результат равен {num_1 / num_2}')
    except ZeroError as err:
        print(err)
    except ValueError:
        print('Вы ввели не число')


main()
