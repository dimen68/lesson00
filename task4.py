# Найдите сумму всех целых чисел от 1 до 100.
sum_ = 0
for i in range(1,101):
    sum_ += i
print(i)
print(sum_)

# Найдите сумму всех целых четных чисел в промежутке от 1 до 100.
sum_ = 0
for i in range(1,101):
    if i % 2 == 0:
        sum_ += i
print(i)
print(sum_)

# Найдите сумму всех целых нечетных чисел в промежутке от 1 до 100.
sum_ = 0
for i in range(1,101):
    if i % 2 != 0:
        sum_ += i
print(i)
print(sum_)

# Получите каждый второй элемент
base = [1, 2, 3, 4, 5, 6]
print(base[::2])

# Даны два целых числа. Найдите остаток от деления первого числа на второе.
a = int(input('Введите число А: '))
b = int(input('Введите число Б: '))
c = a % b
print(f'Остаток от деления {a} на {b} равно {c}')


