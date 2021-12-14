import pytest
import requests
from project_7.func_h7 import post_book, put_book, post_role


@pytest.fixture()
def f_base_url():
    return 'http://pulse-rest-testing.herokuapp.com/'


@pytest.fixture()
def f_book_data(f_base_url):
    book_data = {'title': 'book1', 'author': 'test1'}
    yield book_data
    if 'id' in book_data:
        requests.delete(f'{f_base_url}/books/{book_data["id"]}')


@pytest.fixture()
def f_post_book(f_base_url, f_book_data):
    book = post_book(f_base_url, f_book_data).json()
    f_book_data['id'] = book['id']
    return f_book_data


@pytest.fixture()
def f_book_data_changed():
    book_data_changed = {'title': 'book3edited', 'author': 'test3edited'}
    return book_data_changed


@pytest.fixture()
def f_change_book(f_base_url, f_post_book, f_book_data_changed):
    f_post_book = put_book(f_base_url, f_post_book['id'], f_book_data_changed).json()
    return f_post_book


@pytest.fixture()
def f_role_data(f_base_url, f_post_book):
    role_data = {'name': 'role1', 'type': 'test1', 'level': 3, 'book': f_post_book['id']}
    yield role_data
    if 'id' in role_data:
        requests.delete(f'{f_base_url}/roles/{role_data["id"]}')


@pytest.fixture()
def f_post_role(f_base_url, f_post_book, f_role_data):
    role = post_role(f_base_url, f_role_data).json()
    f_role_data['id'] = role['id']
    return f_role_data