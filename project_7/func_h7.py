import requests
import json


def is_year_leap(c):
    if (c % 4 == 0 and c % 100 != 0) or c % 400 == 0:
        return True
    else:
        return False


def triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True


def triangle_kind(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            return 'Equilateral triangle'
        elif a == b or b == c or a == c:
            return 'Isosceles triangle'
        else:
            return 'Versatile triangle'
    else:
        return 'Not a triangle'


def post_book(base_url, book_data):
    return requests.post(f'{base_url}books/',
                         headers={'Content-Type': 'application/json'},
                         data=json.dumps(book_data))


def put_book(base_url, book_id, book_data_changed):
    return requests.put(f'{base_url}books/{book_id}',
                        data=book_data_changed)


def post_role(base_url, role_data):
    return requests.post(f'{base_url}roles/',
                         headers={'Content-Type': 'application/json'},
                         data=json.dumps(role_data))
