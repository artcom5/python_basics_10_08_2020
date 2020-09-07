"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Storage:
    """
    Класс склад
    """
    def __init__(self, title_quantity_0):
        """Конструктор описывает наименование, и количество.
        """
        self.title_quantity_0 = title_quantity_0
        self.base = []    # Список склада.
        self.company = []    # Список товаров отпущенных со склада.
        self.quantity = 0

    def coming(self, equipment):
        """
        Метод принимает оборудование и добавляет его в список.
        :param equipment: оборудование
        """
        self.base.append(equipment)

    def get_quantity(self):
        """
        Метод считает сколько на складе оборудования.
        :return: количество в шт.
        """
        self.quantity = len(self.base)
        return f'Количество оборудования на складе: {self.quantity} шт.'

    def print(self):
        """
        Метод выводит список по позициям.
        """
        for idx, line in enumerate(self.base):
            print(f'{idx + 1} позиция {line}')

    def to_company(self, equipment):
        """
        Метод принимает наименование оборудования,
        ищет его на складе и перемещает в компанию.
        :param equipment: оборудование
        """
        if equipment in self.base:
            print(f'Такая позиция есть, отпускаю...')
            idx = self.base.index(equipment)
            self.company.append(self.base.pop(idx))
            print(self.company)
        else:
            print('Такой позиции нет!')

    def __str__(self):
        return f'Общий список: \n{[i for i in self.base]}'


class OfficeEquipment:
    """
    Класс оргтехника
    """
    def __init__(self, name_equipment, model, color, weigth, price):
        """
        Конструтор описывает параметры такие как:
        :name_equipment: Тип техники
        :param model: модель
        :param color: цвет
        :param weigth: вес
        :param price: цена
        """
        self.name_equipment = name_equipment
        self.model = model
        self.color = color
        self.weigth = weigth
        self.price = price


class Printer(OfficeEquipment):
    """
    Класс принтер наследуемый от оргтехника.
    """
    def __init__(self, name_equipment, model, color, weigth, price, type_color, print_type):
        OfficeEquipment.__init__(self, name_equipment, model, color, weigth, price)
        self. type_color = type_color
        self.print_type = print_type

    def get_printer(self):
        return f'Тип: {self.name_equipment} | ' \
               f'Модель: {self.model} | ' \
               f'Цвет: {self.color} | ' \
               f'Печать: {self.type_color} | ' \
               f'Тип печати: {self.print_type} | ' \
               f'Вес: {self.weigth} кг. | ' \
               f'Цена: {self.price} руб. |'


class Scanner(OfficeEquipment):
    """
    Класс сканер наследуемый от оргтехника.
    """
    def __init__(self, name_equipment, model, color, weigth, price, format_scan):
        OfficeEquipment.__init__(self, name_equipment, model, color, weigth, price)
        self. format_scan = format_scan

    def get_scanner(self):
        return f'Тип: {self.name_equipment} | ' \
               f'Модель: {self.model} | ' \
               f'Цвет: {self.color} | ' \
               f'Формат: {self.format_scan} | ' \
               f'Вес: {self.weigth} кг. | ' \
               f'Цена: {self.price} руб. | '


class MultifunctionalPrinter(OfficeEquipment):
    """
    Класс МФУ наследуемый от оргтехника.
    """
    def __init__(self, name_equipment, model, color, weigth, price, type_color, print_type, format_scan, display):
        OfficeEquipment.__init__(self, name_equipment, model, color, weigth, price)
        self.type_color = type_color
        self.print_type = print_type
        self.format_scan = format_scan
        self.display = display

    def get_mfp(self):
        return f'Тип: {self.name_equipment} | ' \
               f'Модель: {self.model} | ' \
               f'Цвет: {self.color} | ' \
               f'Печать: {self.type_color} | ' \
               f'Тип печати: {self.print_type} | ' \
               f'Формат: {self.format_scan} | ' \
               f'Дисплей: {self.display} | ' \
               f'Вес: {self.weigth} кг. | ' \
               f'Цена: {self.price} руб. | '


if __name__ == '__main__':
    office_equipment_0 = Printer('Принтер', 'Canon', 'Черный', 2, 12300, 'Цветная', 'Cтруйная')
    # print(office_equipment_0.get_printer())
    office_equipment_1 = Scanner('Сканер', 'HP', 'Синий', 0.7, 3500, 'A3')
    # print(office_equipment_1.get_scanner())
    office_equipment_2 = MultifunctionalPrinter('МФУ', 'Xerox', 'Серый',
                                                6, 24000, 'Черно-белая',
                                                'Лазерная', 'A3', 'Есть')
    # print(office_equipment_2.get_mfp())

    base_1 = Storage(office_equipment_0)
    base_1.coming(office_equipment_0.get_printer())
    base_1.coming(office_equipment_1.get_scanner())
    base_1.coming(office_equipment_2.get_mfp())
    base_1.print()
    print(base_1.get_quantity())
    # print(base_1)
    base_1.to_company(office_equipment_0.get_printer())
    print(base_1.get_quantity())
    base_1.print()
