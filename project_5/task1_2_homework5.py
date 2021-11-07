from task1_1_homework5 import Person


class Employee(Person):
    """Class with information about employee"""
    def __init__(self, full_name='', year_of_birth=None, position='', work_experience=0, salary=0):
        super().__init__(full_name, year_of_birth)
        self.position = position
        self.work_experience = work_experience
        self.salary = salary

        if work_experience < 0 or salary < 0:
            raise ValueError('Expected work experience and salary > 0')

    def name_position(self):
        """Returns employee position with prefix"""
        if self.work_experience <= 3:
            return f'Junior {self.position}'
        elif 3 < self.work_experience <= 6:
            return f'Middle {self.position}'
        else:
            return f'Senior {self.position}'

    def increase_salary(self, increase=0):
        """Returns employee salary with increase"""
        self.salary += increase

    def __str__(self):
        return f'Employee position is {self.name_position()}, ' \
               f'work experience is {self.work_experience}, ' \
               f'salary is {self.salary}'


e = Employee('Test Prer', 1999, 'engineer', 2, 110)
e.increase_salary(40)
print(e)
