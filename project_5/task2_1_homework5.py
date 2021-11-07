class Rectangle:
    """Class for square and perimeter calculation of rectangle"""
    def __init__(self, side1=None, side2=None):
        self.side1 = side1
        self.side2 = side2

        if side1 is None or side2 is None:
            raise ValueError('Should be given side size')
        if type(side1) != int or type(side2) != int:
            raise ValueError('Should be given numbers')

    def square(self):
        """"Square calculation"""
        square = self.side1 * self.side2
        return square

    def perimeter(self):
        """"Perimeter calculation"""
        perimeter = 2*(self.side1 + self.side2)
        return perimeter

    def __str__(self):
        return f'Sides are: {self.side1}, {self.side2}, ' \
               f'square is {self.square()}, ' \
               f'perimeter is {self.perimeter()}'


r = Rectangle(12, 3)
print(r)
