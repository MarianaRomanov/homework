a = ['abc', 'bcd', 'cat', 'dog', 'elephant', 'forest']
print(a)
print(a[-3])
print(a[1][0])
print(a[-1][-1])
a.append('ginger')
print(a)
a.pop(0)
print(a)
if 'world' in a:
    a.remove('world')
