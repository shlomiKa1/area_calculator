# Link to gitHub project: 

from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon

    
def main():
    try:
        rect1 = Rectangle(5, 10)
        circle1 = Circle(4)
        square1 = Square(4)

        rect2 = Rectangle(2, 8)
        hexagon1 = Hexagon(3)
        triangle = Triangle(2, 3, 5, 9, 3)

        shapes  = [rect1, circle1, square1, rect2, hexagon1, triangle]

        for shape in shapes:
            print(shape)

        print(f"Is Rectangle 1 bigger than Square 1? {rect1 > square1}")
        print(f"Is Circle 1 smaller than Rectangle 1? {circle1 < rect1}")

        print(f"Is Square 1 equal in area to Rectangle 2? {square1 == rect2}")
        
        combined_area = rect1 + square1
        print(f"The combined area of Rectangle 1 and Square 1 is: {combined_area:.2f}")

        print(f"\nDeveloper representation (repr) of Circle 1: {repr(circle1)}")

    except (ValueError, TypeError) as e:
        print(e)


# --- Main ---
if __name__ == "__main__":
    main()