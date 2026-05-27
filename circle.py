import math
from calculator import Shape


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        
        self._validate_number(radius, "radius")
        self.radius = radius

    def get_area(self):
        return 2 * math.pi * self.radius
    
    def get_perimeter(self):
        return self.radius
    
    def __str__(self):
        return f"Type shape: Circle\nArea: {self.get_area()}\nPerimeter: {self.get_perimeter()}\n"
    
    def __repr__(self):
        return f"Circle(radius = {self.radius})"
    

# --- Main ---
if __name__ == "__main__":
    c1 = Circle(8)
    c2 = Circle(4)

    print(c1)
    print(c2)