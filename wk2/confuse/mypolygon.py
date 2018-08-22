"""
 These lines are Python3 comments
 File: polygon.py 
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

bob = turtle.Turtle()   # make a bob turtle
print("bob is: ", bob)  # show bob

def square(t, n):          # define a square function
    for i in range(n):
        t.fd(100)
        t.lt(360/n)

square(bob, 10)             # call the function with paramater bob

turtle.mainloop()       # keep the window open
