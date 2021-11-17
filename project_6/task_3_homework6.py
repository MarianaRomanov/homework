f = open('test3_1.txt', 'w')
r = ['test', 'apple', 'Book', 'mouse', 'book', 'big', 'pet', 'home']
for i in r:
    print(i, file=f, end='\n')
f.close()

f = open('test3_1.txt')
f1 = open('test3_2.txt', 'w')
d = {}
for line in f:
    line = line.lower().rstrip()
    if d.get(line):
        d[line] += 1
    else:
        d[line] = 1
for j in sorted(d.keys()):
    print(j, ':', d[j], file=f1, end='\n')
f.close()
f1.close()
