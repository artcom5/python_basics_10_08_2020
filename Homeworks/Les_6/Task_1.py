"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
— на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""

import time

class TrafficLight:

    def __init__(self, color):
        self.__color = color


    def running(self):
        for color in self.__color:
            if color == 'красный':
                print(color)
                time.sleep(7)
            elif color == 'желтый':
                print(color)
                time.sleep(2)
            else:
                print(color)
                time.sleep(10)
        print('Светофор работу закончил')

    def running_rev(self):
        print(self.__color)
        time.sleep(2)

traf_0 = ['красный', 'желтый', 'зеленый']
traf_1 = 'желтый'

count = 0
while count != 10:

    traf_go = TrafficLight(traf_0)
    traf_go.running()
    traf_rev = TrafficLight(traf_1)
    traf_rev.running_rev()
    count += 1

