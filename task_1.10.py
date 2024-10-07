# Получите каждый второй символ этой строки:
str_ = 'abcdef'
print(str_[0::2])

# Выведите в консоль все его символы с конца.
a = 12345
str_ = list(str(a))
str_.sort(reverse=True)
for i in str_:
    print(i)

a = 12345
str_ = str(a)
print(str_[::-1])

