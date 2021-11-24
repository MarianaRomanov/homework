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
