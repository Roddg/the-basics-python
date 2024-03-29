"""
Задача 2.
__author__ = "Дмитрий Родионов"

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

# проверка в качестве безопастности, на неверный формат числа
while True:
    user_time = input('введите количество секунд\n')
    if user_time.isdigit():
        user_time = int(user_time)  # преобразуем пользователький ввод в целое число
        break

    print('ошибка ввода, это не число')

hours = user_time // 3600
minutes = (user_time % 3600) // 60
seconds = (user_time % 3600) % 60

# кортежный синтаксис для примера краткой записи
# hours, minutes, seconds = time_second // 3600, (time_second % 3600) // 60, time_second % 60

print(f"{hours:>02}:{minutes:>02}:{seconds:>02}")
