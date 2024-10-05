# Тема 5. Работа со словарями
#1
'''
def to_dict(*lst):
    dict_ = {}
    for i in lst:
        dict_[i] = i
    return dict_


sp = to_dict(1,2,3,4,'q','a')
for i in sp.keys():
    print(i,':',sp[i])

#2
def biggest_dict(**kwargs):
    my_dict = {'first_one':'we can do it'}
    my_dict.update(kwargs)
    return my_dict

new_dict = {'1':1, '2' : 2, '3' : 3, '4' : 4, 'q' : 'q', 'a' : 'a'}
new_dict = biggest_dict(**new_dict)
for i, val in new_dict.items():
    print(i,':',val)
'''
from audioop import reverse


#3
def count_it(*sequence):
    count_ = []
    seq_ ={}
    for i in range(0,10):
        j = sequence.count(i)
        count_.append(j)
        seq_[str(i)] = j
    count_.sort(reverse=True)
    max_3 = count_[:3]
    seq_2 ={}
    for k in max_3:
        for l, val in seq_.items():
            if val == k:
                seq_2[str(l)] = val
    return seq_2


from random import randint
list_ =[]
for i in range(1, 101):
    list_.append(randint(0, 9))
list_.sort()
print(list_)
seq_1 = count_it(*list_)
for j, val in seq_1.items():
    print(j, val)
