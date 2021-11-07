from math import sqrt, pow


class Point:
    """Class with points coordinates"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_to_zero(self):
        """Calculates the distance between point and origin"""
        try:
            x, y = int(self.x), int(self.y)
            dist = sqrt(pow(x, 2) + pow(y, 2))
        except ValueError:
            return 'Input is not number'
        return dist

    def distance_between_points(self, point1):
        """Calculates the distance between two points"""
        try:
            self.x, self.y, point1.x, point1.y = int(self.x), int(self.y), int(point1.x), int(point1.y)
            dist = sqrt(pow(self.x - point1.x, 2) + pow(self.y - point1.y, 2))
        except ValueError:
            return 'Input is not number'
        return f'Distance between points: {dist}'

    def __str__(self):
        return f'x={self.x}, y={self.y}, distance from origin - {self.distance_to_zero()}'


c1 = Point(5, 1)
c2 = Point(9, 4)
print(c1)
print(c1.distance_between_points(c2))
