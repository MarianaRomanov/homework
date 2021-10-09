# 1
a = input('Enter string:')
if len(a) < 3:
    print('String is too short')
else:
    print(a[2], a[-2], a[:5], a[:-2], a[::2], a[1::2], a[::-1], a[::-2], a[-2::-2], a[-2:0:-1], len(a), sep='\n')

# 2
b = input('Enter string:')
if len(b) > 2:
    if len(b) % 2 == 0:
        b1 = b[:len(b) // 2]
        b2 = b[len(b) // 2:]
    else:
        b1 = b[:len(b) // 2 + 1]
        b2 = b[len(b) // 2 + 1:]
    newB = b2 + b1
    print('New string: ', newB)
elif len(b) == 2:
    newB = b[::-1]
    print('New string: ', newB)
else:
    # len(b) < 2:
    print('String is too short!')

# 3
c = float(input('Enter number:'))
if (c % 4 == 0 and c % 100 != 0) or c % 400 == 0:
    print('YES')
else:
    print('NO')

# 4
a = float(input('Enter number:'))
b = float(input('Enter number:'))
c = float(input('Enter number:'))
if a >= b + c or b >= a + c or c >= a + b:
    print('NO')
else:
    print('YES')

# 5
a = float(input('Enter number:'))
b = float(input('Enter number:'))
c = float(input('Enter number:'))
if a >= b >= c:
    a, b, c = c, b, a
elif a >= c >= b:
    a, b, c = b, c, a
elif b >= a >= c:
    a, b, c = c, a, b
elif b >= c >= a:
    a, b, c = a, c, b
elif c >= a >= b:
    a, b, c = b, a, c
elif c >= b >= a:
    a, b, c = a, b, c
print(a, b, c)

# 6
a = float(input('Enter number:'))
b = float(input('Enter number:'))
c = float(input('Enter number:'))
if a == b == c:
    print('2')
elif (a == b or b == c or a == c) and (a != b or b != c or a != c):
    print('1')
else:
    print('0')

# 7
# 7.1
i = 0
while i <= 10:
    print(i)
    i = i + 1

# 7.2
a = ''
j = 20
while j > 0:
    a = a + str(j) + ' '
    j = j - 1
print(a)

# 7.3
a = float(input('Enter number:'))
count = 0
while a % 2 == 0:
    count = count + 1
    a = a // 2
print(count)

# 8
# 8.1
li = [1, 3, 65, 4, 76, 77, 86, 2, 90]
while li:
    print(li.pop(0))

# 8.2
s = '1q2w3e3r4t5y678h'
while s:
    s = s[1:]
    print(s)

# 8.3
# 1st
li1 = [1, 3, 65, 4, 76, 77, 86, 2, 90]
li1 = sorted(li1)
while li1:
    print(li1.pop(0))
# 2nd
li2 = [1, 3, 65, 4, 76, 77, 86, 2, 90]
while li2:
    print(min(li2))
    li2.remove(min(li2))

# 8.4
li = [1, 12, 14, 5, 5, 85, 55, 66, 66, 66, 12, 0]
s = m = 1
for i in range(len(li) - 1):
    if li[i] == li[i + 1]:
        s += 1
    else:
        m = max(s, m)
        s = 1
print(m)

# 9
# 9.1
c = float(input('Enter number:'))


def is_year_leap(c):
    if (c % 4 == 0 and c % 100 != 0) or c % 400 == 0:
        return 'True'
    else:
        return 'False'


print(is_year_leap(c))

# 9.2
a = float(input('Enter number:'))
b = float(input('Enter number:'))
c = float(input('Enter number:'))


def triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return 'False'
    else:
        return 'True'


print(triangle(a, b, c))


# 10
t = 'We are not what we should be!\n\
We are not what we need to be.\n\
But at least we are not what we used to be\n\
 (Football Coach)'
# 10.1
p = list(t.split())
print(len(p))

# 10.2
char = '!().'
for i in range(len(p)):
    p[i] = p[i].strip(char)
print(p)

# 10.3
for i in range(len(p)):
    p[i] = p[i].lower()
p.sort()
print(p)

# 10.4
d = {}
for i in p:
    if d.get(i):
        d[i] += 1
    else:
        d[i] = 1
print(d)
