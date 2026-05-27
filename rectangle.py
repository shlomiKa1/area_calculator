from calculator import Shape


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()

        self._validate_number(width, "width")
        self._validate_number(height, "height")

        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Type shape: Rctangle\nArea: {self.get_area()}\nPerimeter: {self.get_perimeter()}\n"
    
    def __repr__(self):
        return f"Rectangle(width = {self.width}, height = {self.height})"
    

# --- Main ---
if __name__ == "__main__":
    r1 = Rectangle(2, 3)
    r2 = Rectangle(2, 5)

    print(r1)
    print(r2)