# Тема 6. Работа с кортежами
'''# 1
def  tpl_sort(cort_):
    list_ = list(cort_)
    flag_ = 'Отсортированный кортеж:'
    for i in range(0, len(cort_)):
        if type(list_[i]) != int:
            flag_ = 'Кортеж ослался без изменений:'
            print(f'В кортеже присутствует не целое число - {list_[i]}')
            return flag_, cort_
    list_.sort()
    return flag_, tuple(list_)

a = (4,7,88,2,43,8,3, 5 )
sort_cort = tpl_sort(a)
print(f'{sort_cort[0]}\n{sort_cort[1]}')


# 2
def slicer(*cort_2, rnd_):
    list_ = list(cort_2)
    pos_ = []
    for i in range(0, len(cort_2)):
        if cort_2[i] == rnd_:
            pos_.append(i)
    if len(pos_) < 1:
        return tuple()
    elif len(pos_) == 1:
        return tuple(list_[pos_[0]::])
    else:
        return tuple(list_[pos_[0]:pos_[1]+1])


a= slicer(4,3 ,4,7,88,2,3,43,8,9,3, 5, rnd_=3)
print(a)


# 3
def sieve(list_int):
    t = set(list_int)
    r = list(t)
    r.sort(reverse=True)
    return tuple(r)


a = [1,9,2,8,3,7,4,6,5,6,5,7,4,8,3,9,2,1]
b= sieve(a)
print(b)
'''

# 4
def  del_from_tuple(c, kon_):
    print(type(c))
    if kon_ in c:
        param = c.index(kon_)
        del c[param]
        return c
    else:
        return c

e = (1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0)
d = del_from_tuple(e, 4) # Так делать нельзя!!!
print(d)


