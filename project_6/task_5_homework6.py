import pandas

f = pandas.read_excel('./test5.xlsx')
# 1
print(len(set(f['Отдел'])))
# 2
print(max(f['Зарплата']))
# 3
max_zp = {}
for i in range(len(f['Отдел'])):
    if f['Отдел'][i] in max_zp.keys():
        max_zp[f['Отдел'][i]] = max(f['Зарплата'][i], max_zp[f['Отдел'][i]])
    else:
        max_zp[f['Отдел'][i]] = f['Зарплата'][i]
print(max_zp)
# 4
for j in f.values:
    if j[3] == max_zp[j[2]]:
        print(f'{f.columns[2]}: {j[2]}, '
              f'{f.columns[3]}: {j[3]}, '
              f'{f.columns[0]}: {j[0]}')
