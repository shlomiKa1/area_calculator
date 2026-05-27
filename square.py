from calculator import Shape


class Square(Shape):
    def __init__(self, side):
        super().__init__(self)
        self.side = side

    def get_area(self):
        return self.side ** 2
    
    def get_perimeter(self):
        return self.side * 4
    
    def __str__(self):
        return f"Type shape: Square\nArea: {self.get_area()}\nPerimeter: {self.get_perimeter()}\n"
    

# --- Main ---
if __name__ == "__main__":
    s1 = Square(9)
    s2 = Square(7)

    print(s1)
    print(s2)