# Задача 1.
__author__ = "Дмитрий Родионов"

from math import *

a = 1
b = -2.5
name = "Вася"

print("%.1f \n%.1f \n%s" % (a, b, name))

name = input("Введите ваше имя: ")

print(name, "найдем значение выражения (x+y)/2*log(x+y)/x*y), введите числа:")
x = float(input("x = "))
y = float(input("y = "))

res = (x + y) / 2 * (log(x + y) / x / y) ** 0.5
print(f"Ответ: {res:.2f}")
