class Shape:
    def __init__(self):
        pass

    def get_area(self):
        pass

    def get_perimeter(self):
        pass
    
    def __str__(self):
        pass

    def __repr__(self):
        pass
    
    def __eq__(self, other_shape):
        if not isinstance(other_shape, Shape):
            return False
        return self.get_area() == other_shape.get_area()
    
    def __lt__(self, other_shape):
        if not isinstance(other_shape, Shape):
            raise TypeError("We can compere only with another shape")
        return self.get_area() < other_shape.get_area()

    def __gt__(self, other_shape):
        if not isinstance(other_shape, Shape):
            raise TypeError("We can compere only with another shape")
        return self.get_area() > self.get_area()
    
    def __add__(self, other_shape):
        if not isinstance(other_shape, Shape):
            raise TypeError("We can add with another shape")
        return self.get_area() + other_shape.get_area()

    @staticmethod
    def _validate_number(value, name="Property"):
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError(f"Error: {name} must be a number")
        
        if value <= 0:
            raise ValueError("Error: num most be positive")