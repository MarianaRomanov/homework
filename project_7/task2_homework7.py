import unittest
import requests
import json


class BookCreateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/'

    def test_book_create(self):
        book_data = {'title': 'book1', 'author': 'test1'}
        resp = requests.post(f'{self.base_url}books/',
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(book_data))
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.headers['Content-Type'], 'application/json')
        body = resp.json()
        self.assertIn('id', body)
        self.book_id = body['id']

    def test_book_create_fail_data(self):
        book_data = {'title': 'book2'}
        resp = requests.post(f'{self.base_url}books/',
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(book_data))
        self.assertNotEqual(resp.status_code, 201)
        body = resp.json()
        self.assertNotIn('id', body)
        self.book_id = None

    def tearDown(self) -> None:
        if self.book_id:
            requests.delete(f'{self.base_url}/books/{self.book_id}')


class BookGetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/'
        self.book_data = {'title': 'book2', 'author': 'test2'}

    def test_get_book(self):
        resp = requests.post(f'{self.base_url}books/',
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(self.book_data))
        self.assertEqual(resp.status_code, 201)
        body = resp.json()
        self.assertIn('id', body)
        self.book_id = body['id']
        self.book_data['id'] = self.book_id
        get_book = requests.get(f'{self.base_url}books/{self.book_id}')
        self.assertEqual(get_book.status_code, 200)
        self.assertDictEqual(self.book_data, get_book.json())

    def test_book_in_the_list(self):
        resp = requests.post(f'{self.base_url}books/',
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(self.book_data))
        self.assertEqual(resp.status_code, 201)
        body = resp.json()
        self.assertIn('id', body)
        self.book_id = body['id']
        self.book_data['id'] = self.book_id
        get_books = requests.get(f'{self.base_url}books/')
        self.assertTrue(self.book_data in get_books.json())

    def tearDown(self) -> None:
        if self.book_id:
            requests.delete(f'{self.base_url}/books/{self.book_id}')


class BookChangeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/'
        self.book_data = {'title': 'book3', 'author': 'test3'}

    def test_change_book(self):
        resp = requests.post(f'{self.base_url}books/',
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(self.book_data))
        self.assertEqual(resp.status_code, 201)
        body = resp.json()
        self.assertIn('id', body)
        self.book_id = body['id']
        book_data_changed = {'title': 'book3edited', 'author': 'test3edited'}
        change_book = requests.put(f'{self.base_url}books/{self.book_id}',
                                   data=book_data_changed)
        self.assertEqual(change_book.status_code, 200)
        body_changed = change_book.json()
        self.assertEqual(self.book_id, body_changed['id'])
        book_data_changed['id'] = body_changed['id']
        self.assertDictEqual(book_data_changed, body_changed)

    def test_change_book_fail_no_book(self):
        self.book_id = 20
        book_data_changed = {'title': 'book3edited', 'author': 'test3edited'}
        change_book = requests.put(f'{self.base_url}books/{self.book_id}',
                                   data=book_data_changed)
        self.assertNotEqual(change_book.status_code, 200)
        body_changed = change_book.json()
        self.assertNotIn('id', body_changed)

    def tearDown(self) -> None:
        if self.book_id:
            requests.delete(f'{self.base_url}/books/{self.book_id}')


class BookGetChangedTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/'
        self.book_data = {'title': 'book4', 'author': 'test4'}
        self.book_data_changed = {'title': 'book4edited', 'author': 'test4edited'}

    def test_get_changed_book(self):
        resp = requests.post(f'{self.base_url}books/',
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(self.book_data))
        self.assertEqual(resp.status_code, 201)
        body = resp.json()
        self.assertIn('id', body)
        self.book_id = body['id']
        change_book = requests.put(f'{self.base_url}books/{self.book_id}', data=self.book_data_changed)
        self.assertEqual(change_book.status_code, 200)
        self.book_data_changed['id'] = self.book_id
        get_changed_book = requests.get(f'{self.base_url}books/{self.book_id}')
        self.assertEqual(get_changed_book.status_code, 200)
        self.assertDictEqual(self.book_data_changed, get_changed_book.json())

    def test_changed_book_in_the_list(self):
        resp = requests.post(f'{self.base_url}books/',
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(self.book_data))
        self.assertEqual(resp.status_code, 201)
        body = resp.json()
        self.assertIn('id', body)
        self.book_id = body['id']
        change_book = requests.put(f'{self.base_url}books/{self.book_id}', data=self.book_data_changed)
        self.assertEqual(change_book.status_code, 200)
        self.book_data_changed['id'] = self.book_id
        get_books_with_changed = requests.get(f'{self.base_url}books/')
        self.assertTrue(self.book_data_changed in get_books_with_changed.json())

    def tearDown(self) -> None:
        if self.book_id:
            requests.delete(f'{self.base_url}/books/{self.book_id}')


class RoleCreateTests(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/'

    def test_role_create(self):
        book_data = {'title': 'book1', 'author': 'test1'}
        resp_book = requests.post(f'{self.base_url}books/',
                                  headers={'Content-Type': 'application/json'},
                                  data=json.dumps(book_data))
        self.assertEqual(resp_book.status_code, 201)
        book_body = resp_book.json()
        self.assertIn('id', book_body)
        self.book_id = book_body['id']
        role_data = {'name': 'role1', 'type': 'test1', 'level': 3, 'book': self.book_id}
        resp_role = requests.post(f'{self.base_url}roles/',
                                  headers={'Content-Type': 'application/json'},
                                  data=json.dumps(role_data))
        self.assertEqual(resp_role.status_code, 201)
        role_body = resp_role.json()
        self.assertIn('id', role_body)
        self.role_id = role_body['id']

    def test_role_create_fail_no_book(self):
        self.book_id = 20
        role_data = {'name': 'role2', 'type': 'test2', 'level': 2, 'book': self.book_id}
        resp_role = requests.post(f'{self.base_url}roles/',
                                  headers={'Content-Type': 'application/json'},
                                  data=json.dumps(role_data))
        self.assertNotEqual(resp_role.status_code, 201)
        role_body = resp_role.json()
        self.assertNotIn('id', role_body)
        self.role_id = None

    def test_role_create_fail_data(self):
        book_data = {'title': 'book1', 'author': 'test1'}
        resp_book = requests.post(f'{self.base_url}books/',
                                  headers={'Content-Type': 'application/json'},
                                  data=json.dumps(book_data))
        book_body = resp_book.json()
        self.assertIn('id', book_body)
        self.book_id = book_body['id']
        role_data = {'type': 'test3', 'level': 3, 'book': self.book_id}
        resp_role = requests.post(f'{self.base_url}roles/',
                                  headers={'Content-Type': 'application/json'},
                                  data=json.dumps(role_data))
        self.assertNotEqual(resp_role.status_code, 201)
        role_body = resp_role.json()
        self.assertNotIn('id', role_body)
        self.role_id = None

    def tearDown(self) -> None:
        if self.book_id:
            requests.delete(f'{self.base_url}/books/{self.book_id}')
        if self.role_id:
            requests.delete(f'{self.base_url}/roles/{self.role_id}')


class RoleDeleteTests(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/'
        self.book_data = {'title': 'book2', 'author': 'test2'}
        self.role_data = {'name': 'role1', 'type': 'test1', 'level': 3}

    def test_role_delete(self):
        resp_book = requests.post(f'{self.base_url}books/',
                                  headers={'Content-Type': 'application/json'},
                                  data=json.dumps(self.book_data))
        self.assertEqual(resp_book.status_code, 201)
        book_body = resp_book.json()
        self.assertIn('id', book_body)
        self.book_id = book_body['id']
        self.role_data['book'] = self.book_id
        resp_role = requests.post(f'{self.base_url}roles/',
                                  headers={'Content-Type': 'application/json'},
                                  data=json.dumps(self.role_data))
        self.assertEqual(resp_role.status_code, 201)
        role_body = resp_role.json()
        self.assertIn('id', role_body)
        role_id = role_body['id']
        delete_role = requests.delete(f'{self.base_url}roles/{role_id}')
        self.assertEqual(delete_role.status_code, 204)

    def test_role_delete_fail_no_role(self):
        resp_book = requests.post(f'{self.base_url}books/',
                                  headers={'Content-Type': 'application/json'},
                                  data=json.dumps(self.book_data))
        self.assertEqual(resp_book.status_code, 201)
        book_body = resp_book.json()
        self.assertIn('id', book_body)
        self.book_id = book_body['id']
        self.role_data['book'] = self.book_id
        self.role_data.pop('type')
        resp_role = requests.post(f'{self.base_url}roles/',
                                  headers={'Content-Type': 'application/json'},
                                  data=json.dumps(self.role_data))
        self.assertNotEqual(resp_role.status_code, 201)
        role_body = resp_role.json()
        self.assertNotIn('id', role_body)
        role_id = None
        delete_role = requests.delete(f'{self.base_url}roles/{role_id}')
        self.assertEqual(delete_role.status_code, 404)

    def tearDown(self) -> None:
        if self.book_id:
            requests.delete(f'{self.base_url}/books/{self.book_id}')


if __name__ == '__main__':
    unittest.main()
