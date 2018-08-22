 #These lines are Python3 comments
 #File: lowest.py 
 #Programmer: Allen Tools
 #Date: 01/27/2017
 #Course ID: LIS 4930 Python for Informatics
 #Purpose: Write a function that takes three numbers an returns the lowest
 #         numbers


def whileLowest(*args): # The glob makes a tuple of paramaters
    print("Of", type(args), args,  min(args), "is the lowest")

whileLowest(1, 2, 3)
