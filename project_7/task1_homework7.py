import unittest
from project_7.func_h7 import is_year_leap, triangle, triangle_kind
from project_5.task1_3_homework5 import ITEmployee


class YearTests(unittest.TestCase):

    def test_year_1(self):
        res = is_year_leap(400)
        self.assertTrue(res)

    def test_year_2(self):
        res = is_year_leap(2000)
        self.assertTrue(res)

    def test_year_3(self):
        res = is_year_leap(2001)
        self.assertFalse(res)

    def test_year_4(self):
        self.assertRaises(TypeError, is_year_leap, 'gfd')


class TriangleTests(unittest.TestCase):

    def test_triangle_1(self):
        res = triangle(2, 5, 4)
        self.assertTrue(res, True)

    def test_triangle_2(self):
        res = triangle(2, 2, 2)
        self.assertTrue(res, True)

    def test_triangle_3(self):
        res = triangle(2, 7, 1)
        self.assertFalse(res, False)

    def test_triangle_4(self):
        self.assertRaises(TypeError, triangle, (1, 8))

    def test_triangle_5(self):
        with self.assertRaises(TypeError) as context:
            res = triangle(1, 8, 'ttt')
        self.assertIn('unsupported operand type', str(context.exception))


class TriangleKindTests(unittest.TestCase):

    def test_triangle_kind_1(self):
        res = triangle_kind(2, 2, 2)
        self.assertEqual(res, 'Equilateral triangle')

    def test_triangle_kind_2(self):
        res = triangle_kind(2, 2, 3)
        self.assertEqual(res, 'Isosceles triangle')

    def test_triangle_kind_3(self):
        res = triangle_kind(4, 5, 3)
        self.assertEqual(res, 'Versatile triangle')

    def test_triangle_kind_4(self):
        res = triangle_kind(2, 0, 3)
        self.assertEqual(res, 'Not a triangle')

    def test_triangle_kind_5(self):
        self.assertRaises(TypeError, triangle_kind, (1, 2))

    def test_triangle_kind_6(self):
        with self.assertRaises(TypeError):
            res = triangle_kind(2, 'fd', 1)


class ITEmployeeTests(unittest.TestCase):

    def setUp(self):
        self.emp = ITEmployee('Test Prer', 1999, 'engineer', 2, 110, ['QA'])

    def test_employee_1(self):
        res = ITEmployee.add_skill(self.emp, 'Test')
        self.assertIn('Test', self.emp.skills)

    def test_employee_2(self):
        skill_add = ['JS', 'Python']
        res = ITEmployee.add_skills(self.emp, skill_add)
        for i in skill_add:
            self.assertIn(i, self.emp.skills)

    def test_employee_3(self):
        self.assertNotEqual('test', self.emp.name_position())

    def test_employee_4(self):
        self.assertEqual('Junior engineer', self.emp.name_position())

    def test_employee_5(self):
        self.assertIn('engineer', self.emp.name_position())

    def test_employee_6(self):
        self.assertEqual('Test', self.emp.get_name())

    def test_employee_7(self):
        self.assertRaises(TypeError, self.emp.increase_salary(10))


suite1 = unittest.TestLoader().loadTestsFromTestCase(YearTests)
suite2 = unittest.TestLoader().loadTestsFromTestCase(TriangleTests)
suite3 = unittest.TestLoader().loadTestsFromTestCase(TriangleKindTests)
suite4 = unittest.TestLoader().loadTestsFromTestCase(ITEmployeeTests)


if __name__ == '__main__':
    result = unittest.TestResult()
    suite1.run(result)
    suite2.run(result)
    suite3.run(result)
    suite4.run(result)
    print(result)
