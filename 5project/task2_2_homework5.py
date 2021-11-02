from datetime import datetime


class Student:
    """Class with information about student"""
    def __init__(self, full_name='', speciality='', start_year=None, scores=None):
        self.full_name = full_name
        self.speciality = speciality
        self.start_year = start_year
        if scores is None:
            self.scores = []
        else:
            self.scores = scores

    def new_score(self, new_score):
        """Adds new score to list"""
        try:
            self.scores.append(new_score)
        except AttributeError:
            self.scores = [new_score]

    def average_score(self):
        """Average score calculation"""
        count, sc = 0, 0
        for i in self.scores:
            sc += i
            count += 1
        average = sc / count
        return average

    def years(self):
        """Count years of studying"""
        if self.start_year is None:
            return 'Unknown'
        else:
            years = datetime.now().year - self.start_year
        return years

    def __str__(self):
        return f'Student {self.full_name}, speciality {self.speciality}, ' \
               f'scores {self.scores}, average score {self.average_score()}, year {self.years()}'


s = Student('Test Yes', 'Math', 2018, scores=[1, 2, 8])
s.new_score(4)
print(s)
