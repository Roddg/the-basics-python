'''
Задача 5.
__author__ = "ДР"

Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''

# проверка в качестве безопастности, на неверный формат числа
while True:
    rating = [7, 5, 3, 3, 2]
    new_el = input('Введите число >> ')
    pos = 0
    if new_el.isdigit():
        el = int(new_el)  # преобразуем пользователький ввод в целое число
        for x in rating:  # запишем в переменную x элемент последовательности
            if el <= x:  # сравним введенное число с элементом последовательности, если элемент меньше либо равен числу
                pos += 1  # переместим позицию элемента на одно место влево

        rating.insert(pos, el)  # добавляет указанный элемент в список на указанную позицию
        print(f"Результат: {rating}")
        break

    print('Ошибка ввода, это не число')
