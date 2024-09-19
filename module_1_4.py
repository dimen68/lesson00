# Методы строк
my_string = input('Введите текст для проверки работы методов: ')
print('Количество символов введённого текста:',len(my_string))
print('Строка в верхнем регистре:',my_string.upper())
print('Строка в нижнем регистре:',my_string.lower())
print('Строка без пробелов:',my_string.replace(' ', ''))
print('Первый символ строки:',my_string[0])
print('Последний символ строки:',my_string[-1])