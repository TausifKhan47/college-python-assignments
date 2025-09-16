import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


circle = Circle(5) 

print(f"Area of circle: {circle.area():.2f}")
print(f"Perimeter of circle: {circle.perimeter():.2f}")
