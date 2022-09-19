class Circle:
    
    def __init__(self, r, pi = 3.14):
        self.r = r
        self.pi = pi

    def area(self):
        return self.r ** 2 * self.pi

    def perimeter(self):
        return 2 * self.r * self.pi

class Triangle:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimeter(self):
        return self.a + self.b + self.c

    def area(self, h):
        return 1/2 * self.b * h

class Square:
    
    def __init__(self, side):
        self.s = side
        
    def area(self):
        return self.s ** 2
    
    def perimeter(self):
        return self.s * 4
    
class Rectangle:
    
    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth
    
    def area(self):
            return self.l * self.b
        
    def perimeter(self):
            return 2 * (self.l + self.b)
        
circle = Circle(5)
circle.area()