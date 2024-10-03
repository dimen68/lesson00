# Найдите сумму элементов этого словаря.
dict_ ={'a': 1,	'b': 2,	'c': 3,	'd': 4}
sum_ = 0
for i in dict_:
    sum_ += dict_[i]
print(sum_)

# Найдите сумму квадратов элементов этого словаря.
dict_ ={'a': 1,	'b': 2,	'c': 3,	'd': 4}
sum_kw = 0
for i in dict_:
    sum_kw += dict_[i]**2
print(sum_kw)

# Получите список букв этой строки.
alp_ = list('abcde')
print(alp_)

# Получите список цифр этого числа.
num_ = list(map(int, str(12345)))
print(num_)

# Переверните число (1):
num_ = list(str(12345))
back_ = list(num_[::-1])
res_str = str()
for i in back_:
    res_str += i
res_int = int(res_str)
print(res_int)

# Переверните число(2):
num_1 = list(str(12345))
num_1.reverse()
res_str = str()
for i in num_1:
    res_str += i
res_int = int(res_str)
print(res_int)

# Найдите сумму цифр этого числа.
str_2 = list(str(12345))
num_2 = sum(list(map(int, str_2)))
print(num_2)