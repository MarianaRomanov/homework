a = 'aaabbb cccddd'
b = '11223'
print('a =', a)
print('b =', b)
print('a - запись числа?', a.isdigit())
print('b - запись числа?', b.isdigit())

c = '11 222 33 444 55'
print('c =', c)
print('Количество  пробелов в c :', c.count(' '))

d = 'aa.bb.1.2.3.ccc'
print('d =', d)
print('Количество точек в d :', d.count('.'))

e = 'Homework'
print('e =', e)
print('Строка 100 символов -', e.center(100, ' '))
print('Длина строки -', len(str(e.center(100, ' '))))

f = 'this IS My second HomeWork, I am at The park'
print('f =', f)
print('Первые буквы большые в f', f.title())
print('f заканчивается на -ing?', f.endswith('ing'))
print('Индекс первой "a" в f:', f.index('a'))
print('f разбита на подстроки -', f.split())

g = '   tabs is present here  '
print('g =', g)
print('g без пробелов -', g.strip(' '))
