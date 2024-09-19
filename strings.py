# "Строки и индексация строк"
example = 'Disneyland'
print(example[0])
print(example[-1])
print(example[(int((len(example)/2)-1+((len(example)/2)%2))):]) # или использовать (len(example)//2) вместо (int((len(example)/2)
print(example[::-1])
print(example[1::2])