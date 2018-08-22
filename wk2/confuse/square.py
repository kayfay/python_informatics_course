"""
 These lines are Python3 comments
 File: square.py 
 Programmer: Allen Tools
 Date: 01/19/2017
 Course ID: LIS 4930 Python for Informatics
 Purpose: A function called square that takes a parameter called t which is
 turtle, it should draw a square
"""
import turtle

bob = turtle.Turtle()   # make a bob turtle
print("bob is: ", bob)  # show bob

def square(t):          # define a square function
    for i in range(4):
        t.fd(100)
        t.lt(90)

def polygon(t, n):          # define a square function
    for i in range(n):
        t.fd(100)
        t.lt(360/n)

def polyline(t, length, angle):
    t.fd(length)
    t.lt(angle)

square(bob)
turtle.mainloop()       # keep the window open
