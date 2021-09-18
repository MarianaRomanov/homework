a = {'title': 'Book', 'price': 20, 'ingredients': ['water', 'sugar', 'lemon', 'ginger']}
print(a)
a['description'] = 'some text'
print(a)
a['price'] += 100
print(a)
a['ingredients'].append('salt')
print(a)
print(len(a['ingredients']))
a.pop('description')
print(a)