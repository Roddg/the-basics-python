# Задача 3.
__author__ = "Дмитрий Родионов"

number = input("Введите число >>> ")
sum_ = int(number) + int(number + number) + int(number + number + number)
print(f"Cумма чисел {number} "
      f"+ {number}{number} "
      f"+ {number}{number}{number} = {sum_}")
