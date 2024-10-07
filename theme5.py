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

#4
dict_ = {'key1': 654, 'key2' : 67546,'key3' : 89,'key4' : 123, 'key5' : 9808,'key6' : 55}
for i, val in dict_.items():
    print(i,':',val)
print('________________')
keys_ = list(dict_.keys())
values_ = list(dict_.values())
keys_[0], keys_[-1] = keys_[-1], keys_[0]
values_[0], values_[-1] = values_[-1], values_[0]
dict_.clear()
dict_ = dict(zip(keys_, values_))
dict_['new_key'] = 'new_value'
for i, val in dict_.items():
    print(i,':',val)
'''

#5
dict_1 = {'key1': 654, 'key2' : 67546,'key3' : 89,'key4' : 123, 'key5' : 9808,'key6' : 55}
dict_2 = {'key1': 17, 'key2' : 67,'key3' : 9,'key4' : 12}
dict_3 = {'key1': 170, 'key2' : 670,'key3' : 90}

def max_dct(*dicts):
    all_keys = []
    for i in range(0, len(dicts)):
        all_keys += (dicts[i].keys())
    all_keys_once = set(all_keys)
    max_val = dict()
    for k in all_keys_once:
        maxi =[]
        for l in range(0, len(dicts)):
            if k in dicts[l].keys():
                maxi.append(dicts[l][k])
        max_val[k] = max(maxi)
    return max_val

def sum_dct(*dicts):
    all_keys = []
    for i in range(0, len(dicts)):
        all_keys += (dicts[i].keys())
    all_keys_once = set(all_keys)
    sum_val = dict()
    for k in all_keys_once:
        sum_ = 0
        for l in range(0, len(dicts)):
            if k in dicts[l].keys():
                sum_ += dicts[l][k]
        sum_val[k] = sum_
    return sum_val

result_ = max_dct(dict_1, dict_2, dict_3)
print(result_)

result_1 = sum_dct(dict_1, dict_2, dict_3)
print(result_1)