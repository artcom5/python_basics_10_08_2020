"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    """
    Класс машина
    """
    def __init__(self, color, name, speed, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def get_car(self):
        """
        Метод вывода всех значений
        """
        print(f'Машина: {self.name}, цвет: {self.color}, скорость {self.speed}, полиция {self.is_police}')

    def go(self):
        """
        Метод движения
        """
        print('поехала')

    def stop(self):
        """
        Метод останова
        """
        print('остановилась')

    def direction(self):
        """
        Метод останова
        """
        print('повернула')

    def speed_max(self):
        """
        Вывод максимальной скорости.
        """
        print(f'Максимальная скорость автомобиля {self.speed}')

    def police_show(self):
        """
        Метод проверки машины
        """
        if self.is_police:
            print('Полицейская машина')
        else:
            print('Обычная машина')

class TownCar(Car):
    """
    Дочерний класс городской машины.
    """
    def __init__(self, color, name, speed, speed_show, is_police):
        super().__init__(color, name, speed, is_police)
        self.speed_show = speed_show

    def show_speed(self):
        """
        Метод превышения скорости.
        """
        if self.speed_show > 60:
            print(f'{self.name} превысела скорость')

class WorkCar(Car):

    def __init__(self, color, name, speed, speed_show, is_police):
        super().__init__(color, name, speed, is_police)
        self.speed_show = speed_show

    def show_speed(self):

        if self.speed_show > 40:
            print(f'{self.name} превысела скорость')

class PoliceCar(Car):

    pass

class SportCar(Car):

    pass

auto_mazda = Car('красный металик', 'Мазда 3', 300, False)
auto_mazda.get_car()
auto_mazda.police_show()
auto_mazda.speed_max()
auto_mazda.go()
auto_mazda.direction()

auto_honda = TownCar('красный', 'honda', 300, 62, False)
auto_honda.get_car()
auto_honda.show_speed()

auto_toyota = WorkCar('белый', 'toyota', 220, 42, False)
auto_toyota.get_car()
auto_toyota.show_speed()

auto_police = PoliceCar('Спе цвет', 'volvo', 260, True)
auto_police.get_car()
auto_police.police_show()

auto_sport = SportCar('Красный', 'Porsche', 320, False)
auto_sport.get_car()
auto_sport.police_show()

