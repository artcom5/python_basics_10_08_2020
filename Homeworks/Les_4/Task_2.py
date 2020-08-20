"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

list_num = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_new = []

# Вариант 1

try:
    for itm in range(0, (len(list_num))+1):
        if list_num[itm+1] > list_num[itm]:
            print(list_num[itm+1])
except IndexError:
    pass

# Вариант 2

try:
    for idx, itm in enumerate(list_num, 1):
        if list_num[idx] > itm:
            list_new.append(list_num[idx])
except:
    pass
print(list_new)

# Вариант 3

list_1 = [itm for idx, itm in zip(list_num, list_num[1:]) if itm > idx]
print(list_1)