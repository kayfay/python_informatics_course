# These lines are Python3 comments
# File: lastNameFirst.py
# Programmer: Allen Tools
# Date: 01/19/2017
# Course ID: LIS 4930 Python for Informatics
# Purpose: a simple program to print name firstname,
# lastname as lastname, firstname

i = ''
name = ""
count = 0

name = input("What is your name? ")

for i in name:
    count += 1  # while i iterates over the name keep a count of the letters
    if i == " ":  # when the letter is blank stop counting
        break

firstname = name[:count]  # use [i:j:k] slicing method
lastname = name[count:]  # to seperate the names

print("Method 1:")
print(lastname, ', ', firstname, sep='')

# Then I remembered with python builtins
# this can be done with 1 line of code!

L = name.split(" ")  # This is ['firstName', 'lastName']

print("Method 2:")  # Using indicies of a list
print(L[1], ", ", L[0], sep='')  # L[1], L[0] = 'tools',  'allen'

L = [1, 2, 3, 4, 5]
