'''Напишите функцию change(lst), которая принимает список и меняет местами
его первый и последний элемент. В исходном списке минимум 2 элемента.

def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
    print(lst)


a = [1,2,3,4,5,6,7,8,9]
change(a)
'''

#Функция to_list() принимает неограниченное количество параметров.
#Обработайте их так, чтобы на выходе получить список из этих элементов.
'''def to_list():
    list_ =[]
    b = int(input(f'Введите количество элементов: '))
    for i in range(1,b+1):
        a = input(f'Введите элемент ({i} из {b}): ')
        list_.append(a)
        print(list_)
    return list_
    print(list_)

to_list()

def to_list(*args):
    return list(args)

print(to_list(1, 5, 77))
print(to_list('Молоко', 5, '2020 год'))
print(to_list([3, 4, 7], 8.3, True, 'Строка'))

# поиске «бесполезного» числа
def useless(s):
    num_ = max(s) / len(s)
    print(num_)  
    return num_

useless([1,2,3,4,5,10,20,50,100,200])
print(useless([1, 5, 77]))
print(useless([19, 8.3, -4, 11, 0, 5]))
print(useless([-33, -0.05, -4.18, 11.2, 13.12, 55, 7.1]))

# сортирует список чисел по убыванию их абсолютного значения.
def list_sort(lst):
    lst.sort(key= lambda x: abs(x), reverse=True)
    return lst

print(list_sort([1, 5, 77]))
print(list_sort([19, 8.3, -4, 11, 0, 5]))
print(list_sort([-33, -0.05, -4.18, 11.2, 13.12, 55, 7.1]))
'''

# вернет новый список из строк одинаковой длины
def all_eq(lst):
    lst1 = list(lst)
    max_ = 0
    for k in lst1:
        if max_ < len(k):
            max_ = len(k)
        for i in range(0, len(lst1)):
            for j in range(len(lst1[i]),max_):
                if len(lst1[i]) < max_:
                    lst1[i] +='_'
    return lst1

a= list(all_eq(['awefawert', 'iol,jk,', 'tdfgh', 'awerwerwtgqwer']))
for i in a:
    print(i)