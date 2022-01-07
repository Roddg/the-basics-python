# Задача 4.
__author__ = "Дмитрий Родионов"

number = int(input('Введите целое положительное число: '))
maximum = 0  # эталон, заведомо меньше любой цифры

while number:  # любое значение неравное нулю это true, а 0 это false(прекращает выполнение цикла)
    d = number % 10  # выделим последнюю цифру в числе
    if d > maximum:  # сравним цифру с эталоном, если цифра больше эталона
        maximum = d  # то она становится эталоном
    number //= 10  # сотрем поледнюю цифру, т.е. заменим число на целую часть от деления числа на 10

print('Максимальная цифра в числе: ', maximum)
