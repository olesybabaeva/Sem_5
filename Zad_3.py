﻿#Создайте функцию генератор чисел Фибоначчи

a = int(input('Dведите число: '))


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fibonacci(a)))