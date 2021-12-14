import pytest
from project_7.func_h7 import is_year_leap, triangle, triangle_kind
from project_5.task1_3_homework5 import ITEmployee


@pytest.fixture(scope='session')
def f_employee():
    emp = ITEmployee('Test Prer', 1999, 'engineer', 2, 110, ['QA'])
    return emp


@pytest.mark.parametrize('year', [400, 2000])
def test_year_1(year):
    res = is_year_leap(year)
    assert res is True


@pytest.mark.parametrize('year', [2001])
def test_year_3(year):
    res = is_year_leap(year)
    assert res is False


@pytest.mark.parametrize('year', ['hht'])
def test_year_4(year):
    with pytest.raises(TypeError) as context:
        is_year_leap(year)
    assert 'not all arguments converted' in str(context.value)


@pytest.mark.parametrize('a,b,c', [(2, 2, 2), (2, 5, 4)])
def test_triangle_1(a, b, c):
    res = triangle(a, b, c)
    assert res is True


@pytest.mark.parametrize('a,b,c', [(2, 7, 1)])
def test_triangle_3(a, b, c):
    res = triangle(a, b, c)
    assert res is False


@pytest.mark.parametrize('a,b', [(1, 8)])
def test_triangle_4(a, b):
    with pytest.raises(TypeError) as context:
        triangle(a, b)
    assert 'missing 1 required positional argument' in str(context.value)


@pytest.mark.parametrize('a,b,c', [(1, 8, 'ttt')])
def test_triangle_5(a, b, c):
    with pytest.raises(TypeError) as context:
        triangle(a, b, c)
    assert 'unsupported operand type' in str(context.value)


@pytest.mark.parametrize('a,b,c', [(2, 2, 2)])
def test_triangle_kind_1(a, b, c):
    res = triangle_kind(a, b, c)
    assert 'Equilateral triangle' in res


@pytest.mark.parametrize('a,b,c', [(2, 2, 3)])
def test_triangle_kind_2(a, b, c):
    res = triangle_kind(a, b, c)
    assert 'Isosceles triangle' in res


@pytest.mark.parametrize('a,b,c', [(4, 5, 3)])
def test_triangle_kind_3(a, b, c):
    res = triangle_kind(a, b, c)
    assert 'Versatile triangle' in res


@pytest.mark.parametrize('a,b,c', [(2, 0, 3)])
def test_triangle_kind_4(a, b, c):
    res = triangle_kind(a, b, c)
    assert 'Not a triangle' in res


@pytest.mark.parametrize('a,b', [(1, 2)])
def test_triangle_kind_5(a, b):
    with pytest.raises(TypeError) as context:
        triangle_kind(a, b)
    assert 'missing 1 required positional argument' in str(context.value)


@pytest.mark.parametrize('a,b,c', [(2, 'fd', 1)])
def test_triangle_kind_6(a, b, c):
    with pytest.raises(TypeError):
        triangle_kind(a, b, c)


def test_employee_1(f_employee):
    ITEmployee.add_skill(f_employee, 'Test')
    assert 'Test' in f_employee.skills


def test_employee_2(f_employee):
    skills = ['JS', 'Python']
    ITEmployee.add_skills(f_employee, skills)
    for i in skills:
        assert i in f_employee.skills


def test_employee_4(f_employee):
    assert 'Junior engineer' == f_employee.name_position()


def test_employee_7(f_employee):
    with pytest.raises(TypeError) as context:
        f_employee.increase_salary('fd')
    assert 'unsupported operand type' in str(context.value)
