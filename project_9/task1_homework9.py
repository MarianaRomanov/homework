import requests

base_url = 'http://pulse-rest-testing.herokuapp.com/'
book_data = {'title': 'book1', 'author': 'test1'}
# get token for authorization
r_token = requests.post(f'{base_url}api-token-auth/',
                        data={'username': 'admin', 'password': 'pass'})
token = r_token.json()['token']
header_token = {'Authorization': f'Token {token}'}

# 1
resp_post_book = requests.post(f'{base_url}books2/', data=book_data, headers=header_token)
book = resp_post_book.json()
book_data['id'] = book['id']

# 2
resp_get_book = requests.get(f'{base_url}books2/{book_data["id"]}', headers=header_token)

role_data = {'name': 'role1', 'type': 'test1', 'level': 3, 'book': book_data['id']}
# using session with basic authorization
s = requests.Session()
s.auth = ('admin', 'pass')
s.headers.update({'Authorization': f'Token {token}'})
# 3
resp_post_role = s.post(f'{base_url}roles2/', data=role_data)
role = resp_post_role.json()
role_data['id'] = role['id']

# 4
resp_get_role_by_book = s.get(f'{base_url}roles/?book_id={book_data["id"]}')

# 5
resp_delete_book = requests.delete(f'{base_url}books2/{book_data["id"]}', headers=header_token)

# 6
resp_delete_role = s.delete(f'{base_url}roles2/{role_data["id"]}')


if __name__ == '__main__':
    print(token)
    print(resp_post_book.status_code)
    print(resp_post_book.json())
    print(resp_post_book.headers)
    print(resp_get_book.status_code)
    print(resp_get_book.json())
    print(resp_post_role.status_code)
    print(resp_post_role.json())
    print(resp_post_role.headers)
    print(resp_get_role_by_book.status_code)
    print(resp_get_role_by_book.json())
    print(resp_delete_book.status_code)
    print(resp_delete_role.status_code)
