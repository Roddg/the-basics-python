# Условие задачи

Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать
явно, в программе.
![](img/Screenshot_1.png)
***

### Встроенные типы данных в Python:

###### NoneType:

    login = None

###### Числа:

    numbers = 34

###### Исключения:

    try:
        a = 100 / 0
    except ZeroDivisionError:
        print("Zero !!!")    

###### Строки:

    first_name = "John"

###### Байты:

    byte_string = b"Hello, world!"

###### Множества:

    perem_1 = set('abrakadabra')
    perem_2 = frozenset('abrakadabra')

###### Списки:

    print(list('обычная строка'))

###### Кортежи:

    print(tuple('обычная строка'))

###### Словари:

    my_dict = dict(key_1='val_1', key_2='val_2')
    print(my_dict)