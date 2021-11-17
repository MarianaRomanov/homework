import requests

base_url = 'http://pulse-rest-testing.herokuapp.com/'
book_data = {'title': 'book1', 'author': 'test1'}

r = requests.post(base_url + 'books/', data=book_data)
book_id = r.json()['id']
print(book_id)

role_data = {'name': 'role1', 'type': 'test1', 'level': 3, 'book': book_id}

r1 = requests.post(base_url + 'roles/', data=role_data)
role_id = r1.json()['id']
print(role_id)


get_role = requests.get(base_url + 'roles/' + str(role_id))
print(get_role.status_code)
print(get_role.json())

get_roles = requests.get(base_url + 'roles/')
role_data['id'] = role_id
if role_data in get_roles.json():
    print('Role is on the list')
else:
    print('Role is not on the list')

role_data_changed = {'name': 'role1_edited', 'type': 'test1_edited', 'level': 5}
change_role = requests.put(base_url + 'roles/' + str(role_id), data=role_data_changed)
print(change_role.status_code)

get_changed_role = requests.get(base_url + 'roles/' + str(role_id))
print(get_changed_role.json())

get_roles_with_changed = requests.get(base_url + 'roles/')
role_data_changed['id'] = role_id
if role_data_changed in get_roles_with_changed.json():
    print('Changed role is on the list')
else:
    print('Changed role is not on the list')

delete_role = requests.delete(base_url + 'roles/' + str(role_id))
print(delete_role.status_code)
