import unittest
import requests


class GetBookTests(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://pulse-rest-testing.herokuapp.com/'

    def test_get_role_by_book(self):
        book_id = 4070
        get_role_by_book = requests.get(f'{self.base_url}roles/?book_id={book_id}')
        res = get_role_by_book.json()
        self.assertEqual(get_role_by_book.status_code, 200)
        self.assertNotEqual(res, [])

    def test_get_role_by_zero_book_fail(self):
        book_id = 0
        get_role_by_book = requests.get(f'{self.base_url}roles/?book_id={book_id}')
        res = get_role_by_book.json()
        self.assertEqual(get_role_by_book.status_code, 200)
        self.assertEqual(res, [])

    def test_get_role_by_type(self):
        text = 'test2'
        get_role_by_type = requests.get(f'{self.base_url}roles/?type={text}')
        res = get_role_by_type.json()
        self.assertEqual(get_role_by_type.status_code, 200)
        self.assertNotEqual(res, [])

    def test_get_role_by_level(self):
        number = 3
        get_role_by_level = requests.get(f'{self.base_url}roles/?level={number}')
        res = get_role_by_level.json()
        self.assertEqual(get_role_by_level.status_code, 200)
        self.assertNotEqual(res, [])

    def test_get_role_by_dif_level(self):
        number = 3
        number_2 = 4
        get_role_by_dif_level = requests.get(f'{self.base_url}roles/?level__lte={number_2}&level__gte={number}')
        res = get_role_by_dif_level.json()
        self.assertEqual(get_role_by_dif_level.status_code, 200)
        self.assertNotEqual(res, [])

    def test_get_role_by_name_book(self):
        text = 'test2'
        name = 'role2'
        get_role_by_name_book = requests.get(f'{self.base_url}roles/?type={text}&name={name}')
        res = get_role_by_name_book.json()
        self.assertEqual(get_role_by_name_book.status_code, 200)
        self.assertNotEqual(res, [])

    def test_get_role_by_type_book_fail(self):
        text = 'test2'
        book_id = 4070
        get_role_by_type_book = requests.get(f'{self.base_url}roles/?type={text}&book_id={book_id}')
        res = get_role_by_type_book.json()
        self.assertEqual(get_role_by_type_book.status_code, 200)
        self.assertEqual(res, [])

    def test_get_role_by_name_book_type(self):
        name = "Francis Wayland Thurston"
        text = "Anthropologist"
        book_id = 4070
        get_role_by_name_book_type = requests.get(f'{self.base_url}roles/?name={name}&book_id={book_id}&type={text}')
        res = get_role_by_name_book_type.json()
        self.assertEqual(get_role_by_name_book_type.status_code, 200)
        self.assertNotEqual(res, [])


if __name__ == '__main__':
    unittest.main()
