import requests

base_url = 'http://pulse-rest-testing.herokuapp.com/'
book_data = [{'title': 'book2'}, {'author': 'book3'}, {'name': 'test'}]
role_data = [{'name': 'role2', 'type': 'test2', 'level': 2, 'book': 5555},
             {'level': 2, 'book': 4110},
             {'title': 'role2', 'type': 'test2', 'book': ''}]

for item in book_data:
    r = requests.post(base_url + 'books/', data=item)
    print(r.status_code)
    print(r.json())

for item1 in role_data:
    r1 = requests.post(base_url + 'roles/', data=item1)
    print(r1.status_code)
    print(r1.json())
