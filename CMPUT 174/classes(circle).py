import math
class Circle:
    def __init__(self, my_radius):
        # - self is the circle object
        self.radius = my_radius
    def display(self):
        # - self is the circle object
        
        print(f'Circle with a radius of {self.radius}')
    def get_area(self):
        # - self is the circle object
        
        return math.pi * self.radius ** 2
def main():
    c1 = Circle(5)
    c1.display()
    print(c1.get_area())

    c2 = Circle(2)
    c2.display()
    print(c2.get_area())
main()