import pytest
import requests
from project_7.func_h7 import post_book, put_book, post_role


def test_book_create(f_base_url, f_book_data):
    resp = post_book(f_base_url, f_book_data)
    assert resp.status_code is 201
    assert resp.headers['Content-Type'] == 'application/json'
    book = resp.json()
    assert 'id' in book
    f_book_data['id'] = book['id']
    assert f_book_data == book


def test_book_create_fail_data(f_base_url, f_book_data):
    f_book_data.pop('author')
    resp = post_book(f_base_url, f_book_data)
    assert resp.status_code != 201


def test_get_book(f_base_url, f_post_book):
    get_book = requests.get(f'{f_base_url}books/{f_post_book["id"]}')
    assert get_book.status_code == 200
    assert f_post_book == get_book.json()


def test_book_in_the_list(f_base_url, f_post_book):
    assert f_post_book in requests.get(f'{f_base_url}books/').json()


def test_change_book(f_base_url, f_post_book, f_book_data_changed):
    change_book = put_book(f_base_url, f_post_book["id"], f_book_data_changed)
    assert change_book.status_code == 200
    body_changed = change_book.json()
    assert f_post_book['id'] == body_changed['id']
    f_book_data_changed['id'] = f_post_book['id']
    assert f_book_data_changed == body_changed


def test_change_book_fail_no_book(f_base_url, f_post_book):
    book_data_changed = {'id': f_post_book["id"], 'title': '', 'author': ''}
    change_book = put_book(f_base_url, f_post_book["id"], book_data_changed)
    assert change_book.status_code != 200


def test_get_changed_book(f_base_url, f_change_book):
    get_changed_book = requests.get(f'{f_base_url}books/{f_change_book["id"]}')
    assert get_changed_book.status_code == 200
    assert f_change_book == get_changed_book.json()


def test_changed_book_in_the_list(f_base_url, f_change_book):
    assert f_change_book in requests.get(f'{f_base_url}books/').json()


def test_role_create(f_base_url, f_post_book, f_role_data):
    resp_role = post_role(f_base_url, f_role_data)
    assert resp_role.status_code == 201
    role = resp_role.json()
    assert 'id' in role
    f_role_data['id'] = role['id']
    assert role == f_role_data


def test_role_create_fail_no_book(f_base_url, f_role_data):
    f_role_data['book'] = -1
    resp_role = post_role(f_base_url, f_role_data)
    assert resp_role.status_code != 201


def test_role_create_fail_data(f_base_url, f_role_data):
    f_role_data.pop('name')
    resp_role = post_role(f_base_url, f_role_data)
    assert resp_role.status_code != 201


def test_role_delete(f_base_url, f_post_role):
    delete_role = requests.delete(f'{f_base_url}roles/{f_post_role["id"]}')
    assert delete_role.status_code == 204


def test_role_delete_fail_no_role(f_base_url, ):
    delete_role = requests.delete(f'{f_base_url}roles/-1')
    assert delete_role.status_code == 404


@pytest.mark.parametrize('book_id', [4070])
def test_get_role_by_book(f_base_url, book_id):
    get_role_by_book = requests.get(f'{f_base_url}roles/?book_id={book_id}')
    res = get_role_by_book.json()
    assert get_role_by_book.status_code == 200
    assert res != []


@pytest.mark.parametrize('book_id', [0])
def test_get_role_by_zero_book_fail(f_base_url, book_id):
    get_role_by_book = requests.get(f'{f_base_url}roles/?book_id={book_id}')
    res = get_role_by_book.json()
    assert get_role_by_book.status_code == 200
    assert res == []


@pytest.mark.parametrize('text', ['test2'])
def test_get_role_by_type(f_base_url, text):
    get_role_by_type = requests.get(f'{f_base_url}roles/?type={text}')
    res = get_role_by_type.json()
    assert get_role_by_type.status_code == 200
    assert res != []


@pytest.mark.parametrize('number', [3])
def test_get_role_by_level(f_base_url, number):
    get_role_by_level = requests.get(f'{f_base_url}roles/?level={number}')
    res = get_role_by_level.json()
    assert get_role_by_level.status_code == 200
    assert res != []


@pytest.mark.parametrize('number,number_2', [(3, 4)])
def test_get_role_by_dif_level(f_base_url, number, number_2):
    get_role_by_dif_level = requests.get(f'{f_base_url}roles/?level__lte={number_2}&level__gte={number}')
    res = get_role_by_dif_level.json()
    assert get_role_by_dif_level.status_code == 200
    assert res != []


@pytest.mark.parametrize('text,name', [('test2', 'role2')])
def test_get_role_by_name_book(f_base_url, text, name):
    get_role_by_name_book = requests.get(f'{f_base_url}roles/?type={text}&name={name}')
    res = get_role_by_name_book.json()
    assert get_role_by_name_book.status_code == 200
    assert res != []


@pytest.mark.parametrize('text,book_id', [('test2', 4070)])
def test_get_role_by_type_book_fail(f_base_url, text, book_id):
    get_role_by_type_book = requests.get(f'{f_base_url}roles/?type={text}&book_id={book_id}')
    res = get_role_by_type_book.json()
    assert get_role_by_type_book.status_code == 200
    assert res == []


@pytest.mark.parametrize('name,text,book_id', [('Francis Wayland Thurston', 'Anthropologist', 4070)])
def test_get_role_by_name_book_type(f_base_url, name, text, book_id):
    get_role_by_name_book_type = requests.get(f'{f_base_url}roles/?name={name}&book_id={book_id}&type={text}')
    res = get_role_by_name_book_type.json()
    assert get_role_by_name_book_type.status_code == 200
    assert res != []
