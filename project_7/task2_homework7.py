import unittest
import requests
from project_7.func_h7 import post_book, put_book, post_role


class CreateBookTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/'
        self.book_data = {'title': 'book1', 'author': 'test1'}

    def test_book_create(self):
        resp = post_book(self.base_url, self.book_data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.headers['Content-Type'], 'application/json')
        book = resp.json()
        self.assertIn('id', book)
        self.book_data['id'] = book['id']
        self.assertDictEqual(self.book_data, book)

    def test_book_create_fail_data(self):
        self.book_data.pop('author')
        resp = post_book(self.base_url, self.book_data)
        self.assertNotEqual(resp.status_code, 201)

    def tearDown(self) -> None:
        if 'id' in self.book_data:
            requests.delete(f'{self.base_url}/books/{self.book_data["id"]}')


class GetBookTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/'
        self.book_data = {'title': 'book2', 'author': 'test2'}
        book = post_book(self.base_url, self.book_data).json()
        self.book_data['id'] = book['id']

    def test_get_book(self):
        get_book = requests.get(f'{self.base_url}books/{self.book_data["id"]}')
        self.assertEqual(get_book.status_code, 200)
        self.assertDictEqual(self.book_data, get_book.json())

    def test_book_in_the_list(self):
        get_books = requests.get(f'{self.base_url}books/')
        self.assertTrue(self.book_data in get_books.json())

    def tearDown(self) -> None:
        requests.delete(f'{self.base_url}/books/{self.book_data["id"]}')


class ChangeBookTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/'
        book_data = {'title': 'book3', 'author': 'test3'}
        book = post_book(self.base_url, book_data).json()
        self.book_id = book['id']

    def test_change_book(self):
        book_data_changed = {'title': 'book3edited', 'author': 'test3edited'}
        change_book = put_book(self.base_url, self.book_id, book_data_changed)
        self.assertEqual(change_book.status_code, 200)
        body_changed = change_book.json()
        self.assertEqual(self.book_id, body_changed['id'])
        book_data_changed['id'] = self.book_id
        self.assertDictEqual(book_data_changed, body_changed)

    def test_change_book_fail_no_book(self):
        book_data_changed = {'id': self.book_id, 'title': '', 'author': ''}
        change_book = put_book(self.base_url, self.book_id, book_data_changed)
        self.assertNotEqual(change_book.status_code, 200)

    def tearDown(self) -> None:
        requests.delete(f'{self.base_url}/books/{self.book_id}')


class GetChangedBookTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/'
        book_data = {'title': 'book4', 'author': 'test4'}
        self.book = post_book(self.base_url, book_data).json()
        book_data_changed = {'title': 'book4edited', 'author': 'test4edited'}
        self.book = put_book(self.base_url, self.book['id'], book_data_changed).json()

    def test_get_changed_book(self):
        get_changed_book = requests.get(f'{self.base_url}books/{self.book["id"]}')
        self.assertEqual(get_changed_book.status_code, 200)
        self.assertDictEqual(self.book, get_changed_book.json())

    def test_changed_book_in_the_list(self):
        get_books_with_changed = requests.get(f'{self.base_url}books/')
        self.assertTrue(self.book in get_books_with_changed.json())

    def tearDown(self) -> None:
        requests.delete(f'{self.base_url}/books/{self.book["id"]}')


class CreateRoleTests(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/'
        book_data = {'title': 'book1', 'author': 'test1'}
        self.book = post_book(self.base_url, book_data).json()
        self.role_data = {'name': 'role1', 'type': 'test1', 'level': 3, 'book': self.book['id']}

    def test_role_create(self):
        resp_role = post_role(self.base_url, self.role_data)
        self.assertEqual(resp_role.status_code, 201)
        role = resp_role.json()
        self.assertIn('id', role)
        self.role_data['id'] = role['id']
        self.assertDictEqual(role, self.role_data)

    def test_role_create_fail_no_book(self):
        self.role_data['book'] = -1
        resp_role = post_role(self.base_url, self.role_data)
        self.assertNotEqual(resp_role.status_code, 201)

    def test_role_create_fail_data(self):
        self.role_data.pop('name')
        resp_role = post_role(self.base_url, self.role_data)
        self.assertNotEqual(resp_role.status_code, 201)

    def tearDown(self) -> None:
        requests.delete(f'{self.base_url}/books/{self.book["id"]}')
        if 'id' in self.role_data:
            requests.delete(f'{self.base_url}/roles/{self.role_data["id"]}')


class DeleteRoleTests(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/'
        book_data = {'title': 'book2', 'author': 'test2'}
        self.book = post_book(self.base_url, book_data).json()
        self.role_data = {'name': 'role1', 'type': 'test1', 'level': 3, 'book': self.book['id']}
        self.role = post_role(self.base_url, self.role_data).json()

    def test_role_delete(self):
        delete_role = requests.delete(f'{self.base_url}roles/{self.role["id"]}')
        self.assertEqual(delete_role.status_code, 204)
        self.role_data = None

    def test_role_delete_fail_no_role(self):
        delete_role = requests.delete(f'{self.base_url}roles/-1')
        self.assertEqual(delete_role.status_code, 404)

    def tearDown(self) -> None:
        requests.delete(f'{self.base_url}/books/{self.book["id"]}')
        if self.role_data is not None:
            requests.delete(f'{self.base_url}/roles/{self.role["id"]}')


if __name__ == '__main__':
    unittest.main()
