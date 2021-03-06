"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


def get_max_digits_after_current_in_list(l):
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            yield l[i]


test_list = [12, 300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 60]
new_list = [el for el in get_max_digits_after_current_in_list(test_list)]
print(new_list)
