"""
3. Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    """
    Класс Worker (работник) имеет конструктор
    атребутов и словарь.
    """
    _income = {'оклад': float, 'бонус': float}
    def __init__(self, name, surname, position):
        """
        Конструктор класса с атрибутами.
        :param name:
        :param surname:
        :param position:
        """
        self.name = name
        self.surname = surname
        self.position = position



class Position(Worker):
    """
    Дочерний класс Position от родителя Worker
    с двумя методами.
    """
    def get_full_name(self):
        """Метод получения полного имени сотрудника"""
        print(f'Имя: {self.name}, Фамилия: {self.surname}, должность: {self.position}')

    def _get_total_income(self):
        """Метод получения полного дохода"""
        result = 0
        for key in self._income:
            self._income[key] = float(input(f'Введите {key}: '))
            result += self._income[key]
        return result

# Создать экземпляр дочернего класса.
work_1 = Position('Вася', 'Петров', 'инженер')
# Вызвать метод.
work_1.get_full_name()
print(f'Доход составляет: {work_1._get_total_income()}')
