"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json
from pathlib import Path

# Назначить имя файла.
file_name = 'Task_7.txt'
file_name_json = 'Task_7.json'
# Путь к файлу.
file_path = Path(__file__).parent.joinpath(file_name)
file_path_json = Path(__file__).parent.joinpath(file_name_json)
# Создать файловый объект с режимом чтения.
file_object = open(file_path, 'r', encoding='UTF-8')

dict_firm = {}    # Словарь для фирм.
list_profit = []    # Список для средней прибыли.
result = []    # Список для результата
aver_profit = {'everage_profit': ''}    # Словарь для средней прибыли.

# Перебрать файл.
for line in file_object:
    list_0 = line.rstrip('\n').split(' ')    # Получить список из строки.
    profit = float(list_0[2]) - float(list_0[3])    # Расчитать прибыль.
    if profit > 0:     # Если прибыль.
        dict_firm[list_0[0]] = profit    # Добавить фирму и прибыль.
        list_profit.append(profit)    # Добавить прибыль в список.
        average = sum(list_profit) / len(list_profit)     # Получить среднее
        aver_profit['everage_profit'] = round(average, 2)    # Добавить среднее в словарь.
list_profit.clear()
result.append(dict_firm)    # Добавить словари в список.
result.append(aver_profit)

print(result)
file_object.close()

with open(file_path_json, 'w') as f_p_json:
    json.dump(result, f_p_json)

