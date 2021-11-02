from task1_2_homework5 import Employee


class ITEmployee(Employee):
    """Class for adding skills to employee"""
    def __init__(self, full_name='', year_of_birth=None, position='', work_experience=0, salary=0, skills=None):
        super().__init__(full_name, year_of_birth, position, work_experience, salary)
        if skills is None:
            self.skills = []
        else:
            self.skills = skills

    def add_skill(self, new_skill):
        """Adds skill to employee"""
        try:
            self.skills.append(new_skill)
        except AttributeError:
            self.skills = [new_skill]

    def add_skills(self, new_skill=[]):
        """Adds skill to employee"""
        for i in new_skill:
            try:
                self.skills.append(i)
            except AttributeError:
                self.skills = [i]

    def __str__(self):
        return f'Employee skills: {self.skills}'


e1 = ITEmployee('Test Prer', 1999, 'engineer', 2, 110)
e1.add_skill('yei')
e1.add_skills(['ter', 453, 'trr'])
print(e1)
