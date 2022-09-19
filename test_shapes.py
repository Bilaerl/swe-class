# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:54:04 2022

@author: ABUBAKAR BENII
"""

from shapes import Circle, Triangle, Square, Rectangle
n = 5

def test_circle():
    
    circle = Circle(n)
    area = circle.area()
    area = '{:.2f}'.format(area)
    perimeter = circle.perimeter()
    perimeter = '{:.2f}'.format(perimeter)
    
    assert area == "78.50", f"result should be '78.50 not {area}"
    assert perimeter == '31.40', f"result should be 31.40 not {perimeter}"
    
def test_triange():
    
    triangle = Triangle(n, n, n)
    perimeter = triangle.perimeter()
    area = triangle.area(6)
    
    assert perimeter == 15, f"result should be 15 not {perimeter}"
    assert area ==  15, f"result should be 15 not {area}"
    
def test_square():
    
    square = Square(n)
    area = square.area()
    perimeter = square.perimeter()
    
    assert area == 25, f"result should be 25 not {square}"
    assert perimeter == 20, f"result should be 20 not {square}"
    
def test_rectangle():
    
    rectangle =Rectangle(n, 10)
    area = rectangle.area()
    perimeter = rectangle.perimeter()
    
    assert area == 50, f"result should be 50 not {area}"
    assert perimeter == 30, f"result should be 30 not {perimeter}"