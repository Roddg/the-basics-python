"""
Задача 2.
__author__ = "ДР"

Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

my_list = input("Введите элементы списка: ").split()
my_list[:-1:2], my_list[1::2] = my_list[1::2], my_list[:-1:2]  # сделаем срез элементов
print(f"Обмен значениями {my_list}")
