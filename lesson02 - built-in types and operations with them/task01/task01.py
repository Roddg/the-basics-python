"""
Задача 1.
__author__ = "ДР"

Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

type_ = [2, 'text', 456, 45.3, [4, 8, 15, 16, 23, 42],
         {"name": "John", "age": 10}, (bool(0)), b"Hello, world!",
         set('abrakadabra'), frozenset('abrakadabra'),
         dict(key_1='val_1', key_2='val_2'),
         None]

# Скрипт проверки типов данных
type_ = [print(f"Элемент {i}, тип {type(i)}") for i in type_]
