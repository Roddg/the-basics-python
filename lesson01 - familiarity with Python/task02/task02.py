# Задача 2.
__author__ = "Дмитрий Родионов"

time = int(input("Введите время в секундах >>> "))

hours = time // 3600
minutes = (time // 60) % 60
seconds = time % 60

print('Время в формате чч:мм:сс {0}:{1}:{2}'.format(hours, minutes, seconds))
