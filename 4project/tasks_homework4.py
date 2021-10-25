from math import sqrt, pow
from string import punctuation, digits, whitespace


# 1
input1 = input('Enter word/number:')
input2 = input('Enter word/number:')
try:
    input1, input2 = int(input1), int(input2)
except ValueError:
    pass
finally:
    result = input1 + input2
    print(result)


# 2
# 2.1
def enter_number():
    while True:
        number = input('Enter number:')
        try:
            number = float(number)
        except ValueError:
            print('Input is not number')
        else:
            break
    return number


print(enter_number())


# 2.2
def enter_string():
    while True:
        string = input('Enter string without space:')
        string = string.strip()
        if string.find(' ') != -1:
            print('Input contains space')
        else:
            break
    return string


print(enter_string())


# 2.3
def triangle_kind(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            return 'Equilateral triangle'
        elif a == b or b == c or a == c:
            return 'Isosceles triangle'
        else:
            return 'Versatile triangle'
    else:
        return 'Not a triangle'


print(triangle_kind(14, 5, 7))


# 2.4
def distance(x1, y1, x2, y2):
    try:
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        dist = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    except ValueError:
        return 'Input is not number'
    return dist


z1 = input('Enter x1:')
z2 = input('Enter y1:')
z3 = input('Enter x2:')
z4 = input('Enter y2:')
print(distance(z1, z2, z3, z4))


# 2.5
def delete_symbols(s):
    for x in punctuation:
        s = s.replace(x, '')
    for y in digits:
        s = s.replace(y, '')
    for z in whitespace:
        s = s.replace(z, '')
    return s


t = input('Enter string:')
print(delete_symbols(t))


# 3
def song(a1=3, a2=3, a3=0):
    word = 'la'
    ver1 = (word + '-') * a2
    ver1 = ver1.rstrip('-')
    ver2 = (ver1 + '\n') * a1
    ver2 = ver2.rstrip('\n')
    if a3 == 0:
        out = ver2 + '.'
    else:
        out = ver2 + '!'
    return out


print(song(2, 4, 1))


# 4
def post_min(*numbers):
    li = list(numbers)
    m = min(li)
    while m in li:
        li.remove(m)
    return min(li)


print(post_min(1, 5, 6, 7, 1, 2, 1))
