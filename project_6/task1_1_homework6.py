import requests

base_url = 'http://pulse-rest-testing.herokuapp.com/'
book_data = {'title': 'book1', 'author': 'test1'}

r = requests.post(base_url + 'books/', data=book_data)
print(r.status_code)
book_id = r.json()['id']
print(book_id)

get_book = requests.get(base_url + 'books/' + str(book_id))
print(get_book.status_code)
print(get_book.json())

get_books = requests.get(base_url + 'books/')
book_data['id'] = book_id
if book_data in get_books.json():
    print('Book is on the list')
else:
    print('Book is not on the list')

book_data_changed = {'title': 'book1edited', 'author': 'test1edited'}
change_book = requests.put(base_url + 'books/' + str(book_id), data=book_data_changed)
print(change_book.status_code)

get_changed_book = requests.get(base_url + 'books/' + str(book_id))
print(get_changed_book.json())

get_books_with_changed = requests.get(base_url + 'books/')
book_data_changed['id'] = book_id
if book_data_changed in get_books_with_changed.json():
    print('Changed book is on the list')
else:
    print('Changed book is not on the list')

delete_book = requests.delete(base_url + 'books/' + str(book_id))
print(delete_book.status_code)
