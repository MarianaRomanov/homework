from datetime import datetime


class Person:
    """Class with information about person"""
    def __init__(self, full_name='', year_of_birth=None):
        self.full_name = full_name
        self.year_of_birth = year_of_birth

        if full_name == '' or len(full_name.strip().split(' ')) != 2:
            raise ValueError('Expected name and surname separated by space')

        if year_of_birth is None or 1990 >= year_of_birth or year_of_birth >= datetime.now().year:
            raise ValueError('Expected year between 1990 and current year')

    def get_name(self):
        """Returns person name"""
        name = self.full_name.strip().split(' ')[0]
        return name

    def get_surname(self):
        """Returns person surname"""
        surname = self.full_name.strip().split(' ')[1]
        return surname

    def count_years(self, year=None):
        """Returns person age"""
        current_year = datetime.now().year
        if year is None:
            age = current_year - self.year_of_birth
        else:
            age = year - self.year_of_birth
        return age

    def __str__(self):
        return f'Persons name is {self.get_name()}, ' \
               f'surname is {self.get_surname()}, ' \
               f'age is {self.count_years()}'


if __name__ == '__main__':
    p = Person('Test Prer', 1999)
    print(p)
# print(p.get_name())
# print(p.get_surname())
# print(p.count_years())
