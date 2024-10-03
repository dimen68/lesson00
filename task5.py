# Найдите сумму элементов списка.
base = [1, 2, 3, 4, 5, 6]
sum_ = 0
for i in base:
    sum_ += i
print(sum_)

# Найдите сумму квадратов элементов  списка.
base = [1, 2, 3, 4, 5, 6]
sum_kw = 0
for i in base:
    sum_kw += i**2
print(sum_kw)

# Найдите сумму квадратных корней элементов этого списка.
base = [1, 2, 3, 4, 5, 6]
sum_kw = 0
for i in base:
    sum_kw += i**(1/2)
print(sum_kw)

# Найдите сумму положительных элементов этого списка.
base_1 = [1, 2, -3, 4, -5]
sum_pol = 0
for i in base_1:
    if i > 0:
        sum_pol += i
print(sum_pol)

# Найдите сумму тех элементов этого списка, которые больше нуля и меньше десяти.
base_2 = [-1, 2, -3, 4, 5, 11]
sum_pol10 = 0
for i in base_2:
    if 0 < i < 10:
        sum_pol10 += i
print(sum_pol10)

# Переберите и выведите в консоль по очереди все символы с конца строки.
str_ = list('abcde')
print(str_[::-1])