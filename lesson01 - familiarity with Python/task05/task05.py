# Задача 5.
__author__ = "Дмитрий Родионов"

proceeds = int(input("Введите значение выручки >>> "))
costs = int(input("Введите значение издержек >>> "))

profit = proceeds - costs

if profit > costs:
    print("Прибыль")
    profitability = profit / proceeds * 100
    print(f"Рентабельность {profitability:.0f} %")
    population = int(input("Введите численность сотрудников фирмы >>> "))
    profit_population = profit / population
    print(f"Прибыль фирмы в расчете на одного сотрудника {profit_population:.0f} $")
elif proceeds == costs:
    print("В ноль")
else:
    print("Убыток")
