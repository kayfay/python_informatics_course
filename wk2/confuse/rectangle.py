"""
 These lines are Python3 comments
 File: rectangle.py 
 Programmer: Allen Tools
 Date: 01/19/2017
 Course ID: LIS 4930 Python for Informatics
 Purpose: A function called square that takes a parameter called t which is
 turtle, it should draw a square.
 Version: 1.1
 Changes: 1.0 -> 1.1 add a paramater, length argument modify the function to
 draw a rectangele
"""
import turtle

bob = turtle.Turtle()   # make a bob turtle
print("bob is: ", bob)  # show bob

def square(t, length):          # define a square function
        t.fd(100)
        t.lt(90)
        t.fd(length)
        t.lt(90)
        t.fd(100)
        t.lt(90)
        t.fd(length)

square(bob, 20)         # call the function with paramater bob
turtle.mainloop()       # keep the window open
