"""
 These lines are Python3 comments
 File: mypolygon.py 
 Programmer: Allen Tools
 Date: 01/19/2017
 Course ID: LIS 4930 Python for Informatics
 Purpose: A function called square that takes a parameter called t which is
 turtle, it should draw a square
 Version: 1.1
 Changes: 1.0 -> 1.1 change a for loop to accept argument n and draws an
 n-sided regular polygon
"""
import turtle
import math

bob = turtle.Turtle()   # make a bob turtle
print("bob is: ", bob)  # show bob

def polygon(t, n):
    """
    Draw a square with number of sides given defined as n.
    """
    angle = 360/n
    for i in range(n):
        t.fd(100)
        t.lt(angle)

def circle(t, r):
    circumference = int(2 * math.pi * r)
    n = int(circumference /4) + 1
    polygon(t, n)


circle(bob, 10)
turtle.mainloop()       # keep the window open
