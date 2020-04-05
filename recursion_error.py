import math


# This class is made properly
class Figure:
    def __init__(self):
        self.is_filled = False
        self.color = None

    # Output of print()
    def __str__(self):
        return f'Figure\nis_filled: {self.is_filled}\ncolor: {self.color}'

    # Output of .repr()
    def __repr__(self):
        return f'Figure[{self.is_filled}, {self.color}]'


# This class in not made properly something is wrong
# but i don't know what at this moment
# super() calls constructor of base class?
class Circle(Figure):
    def __init__(self):
        super().__init__()

    def __str__(self):
        super().__str__()
        return f"""Circle()
radius: 
area: {self.area}
diameter: {self.diameter}
perimeter: {self.perimeter}
"""

    def __repr__(self, value):
        return super().__repr__()
        self.radius = value

    @property
    def radius(self):
        return self.radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self.radius = value
        else:
            print('Input not valid')

    @radius.deleter
    def radius(self):
        del self.radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def diameter(self):
        return 2 * self.radius


class Rectangle(Figure):

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __init__(self):
        super(Rectangle, self).__init__()

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if value <= 0:
            value = float(input('Input correct height: '))
        else:
            self.height = value

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if value <= 0:
            value = float(input('Input correct width: '))
        else:
            self.width = value

    @property
    def diagonal(self):
        return self.width ** 2 + self.height ** 2


if __name__ == __name__:
    circle = Circle()
    print(circle)
