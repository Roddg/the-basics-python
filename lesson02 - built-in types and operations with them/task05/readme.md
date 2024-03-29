# Условие задачи

<p>Реализовать структуру «Рейтинг», 
представляющую собой не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга. 
Если в рейтинге существуют элементы с одинаковыми значениями, 
то новый элемент с тем же значением должен разместиться после них.</p>

<p>Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.</p>

- Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
- Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
- Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

<p>Набор натуральных чисел можно задать непосредственно в коде например</p>

    my_list = [7, 5, 3, 3, 2]

![](img/Screenshot_1.png)
***
<p>Добавляет указанный элемент в список на указанную позицию. 
Разместить на позиции pos (индекс элемента списка) элемент el</p>

    result_list.insert(pos, el) -> None

- pos : Позиция (индекс), на которую требуется поместить элемент. Нумерация ведётся с нуля. Поддерживается отрицательная индексация.

- el: Элемент, который требуется поместить в список.

<p>Метод модифицирует</p>

    my_list = [1, 3]

    my_list.insert(1, 2)
    my_list  # [1, 2, 3]

    my_list.insert(-1, 4)
    my_list  # [1, 2, 4, 3]

<p>Данный метод модифицирует исходный объект на месте, возвращая при этом None.</p>