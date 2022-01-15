# 1) Создать переменную типа String
a = 'Ulyana'
print(type(a), a)

# 2) Создать переменную типа Integer
b = 10
print(type(b), b)

# 3) Создать переменную типа Float
c = 1.5
print(type(c), c)

# 4) Создать переменную типа Bytes
d = b'bytes'
print(type(d), d)

# еще вариант
e = bytes([50, 100, 120])
print(chr(50))
print(type(e), e)

# 5) Создать переменную типа List
f = list('people')
print(type(f), f)

# 6) Создать переменную типа Tuple
g = tuple('world')
print(type(g), g)

# 7) Создать переменную типа Set
h = set('hello')
print(type(h), h)

# 8) Создать переменную типа Frozen set
i = frozenset('pizza')
print(type(i), i)

# 9) Создать переменную типа Dict
j = dict(first='first', second='second')
print(type(j), j)

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
# сделала сразу в заданиях выше

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
k = 'every'
l = 'day'
m = k + l
print(m)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
n = 'Artem'
o = 15
print(n, o)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
p = 'Mike '
r = str(25)
print(p + r)
