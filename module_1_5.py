# Неизменяемые и изменяемые объекты. Кортежи и списки
uni = 'Urban' # один из элементов кортежа
immutable_var ='Dmitry', 1968, 'male', 'student', uni, True
print('Кортеж:\n',immutable_var)
# immutable_var [1] = 2001 - не сработает, так как кортеж не поддерживает замену элементов
mutable_list = list(immutable_var)
print('Список:\n',mutable_list)
mutable_list [1] = 2001
print('Список после замены элемента:\n', mutable_list)
