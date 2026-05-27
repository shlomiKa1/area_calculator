from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon

    
def main():
    try:
        num1, num2, num3, num4, num5 = (2, 3, 5, 9, 3)

        rectangle = Rectangle(num1, num4)
        square = Square(num4)
        triangle = Triangle(num1, num5, num2, num3, num4)
        circle = Circle(num4)
        hexagon = Hexagon(num5)

        shapes  = [rectangle, square, triangle, circle, hexagon]

        for shape in shapes:
            print(shape)
            
    except (ValueError, TypeError) as e:
        print(e)


# --- Main ---
if __name__ == "__main__":
    main()