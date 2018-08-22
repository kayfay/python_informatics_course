"""
 These lines are Python3 comments
 File: mypolygon.py
 Programmer: Allen Tools
 Date: 01/19/2017
 Course ID: LIS 4930 Python for Informatics
 Purpose: write a function that draws a line,
 write a function that takes a parameter named t,
 which is a turtle, draws a square,
 allow length and sides to be passed as paramaters,

"""
import turtle
import math

# initilize variable bob as turtle function
bob = turtle.Turtle()


def line(t, length=100, angle=90):
    t.fd(length)
    t.lt(angle)


def square(t, sides, length=100):
    for i in range(sides):
        line(t)


def polygon(t, sides):
    for i in range(sides):
        line(t, angle=360 / sides)


def circle(t, radius):
    sides = int(2 * math.pi * radius / 4) + 1
    angle = 360 / sides
    length = (2 * math.pi * radius) / sides
    for i in range(sides):
        line(t, length, angle)


def arc(t, radius, angle):
    arcLength = 2 * math.pi * radius * abs(angle) / 360
    sides = int(arcLength / 4) + 1
    lineLength = arcLength / sides
    lineAngle = float(angle) / sides
    for i in range(sides):
        line(t, length=lineLength, angle=lineAngle)


bob.down
square(bob, 4)
polygon(bob, 7)
circle(bob, 200)
arc(bob, 100, 180)
turtle.mainloop()
