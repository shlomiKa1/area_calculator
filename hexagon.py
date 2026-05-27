from math import sqrt
from square import Shape


class Hexagon(Shape):
    def __init__(self, side):
        super().__init__(self)
        self.side = side

    def get_area(self):
        return (3 * sqrt(3) * (self.side) ** 2) / 2
    
    def get_perimeter(self):
        return 6 * self.side
    
    def __str__(self):
        return f"Type shape: Hexagon\nArea: {self.get_area()}\nPerimeter: {self.get_perimeter()}\n"
    

# --- Main ---
if __name__ == "__main__":
    h1 = Hexagon(1)
    h2 = Hexagon(7)

    print(h1)
    print(h2)