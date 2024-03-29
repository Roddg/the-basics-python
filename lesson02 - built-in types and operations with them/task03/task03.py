'''
Задача 3.
__author__ = "ДР"

Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

# проверка в качестве безопастности, на неверный формат числа
while True:
    month_number = input('Введите номер месяца\n')
    if month_number.isdigit():
        month = int(month_number)  # преобразуем пользователький ввод в целое число
        print(f"Вы ввели {month_number}")

        # решение через список (list)
        seasons = ['Зима', 'Весна', 'Лето', 'Осень', 'Зима']

        if 1 <= month <= 12:
            print(f"По списку месяц относится к времени года {seasons[month // 3]}")

        # решение через словарь (dict)
        seasons = {'Зима': [1, 2, 12],
                   'Весна': [3, 4, 5],
                   'Лето': [6, 7, 8],
                   'Осень': [9, 10, 11]}

        for key in seasons.keys():
            if month in seasons[key]:
                print(f"По словарю месяц относится к времени года {key}")
        break

    print('Ошибка ввода, это не число')
