from rectangle import Rectangle


class Triangle(Rectangle):
    def __init__(self, base, height, side_a, side_b, side_c):
        super().__init__(base, height)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        return (self.width * self.height) / 2
    
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
    
    def __str__(self):
        return f"Type shape: Triangle\nArea: {self.get_area()}\nPerimeter: {self.get_perimeter()}\n"
    

# --- Main ---
if __name__ == "__main__":
    t1 = Triangle(9, 2, 4, 2, 1)
    t2 = Triangle(7, 1, 3, 2, 1)

    print(t1)
    print(t2)