"""
 These lines are Python3 comments
 File: pentagonal.py 
 Programmer: Allen Tools
 Date: 01/19/2017
 Course ID: LIS 4930 Python for Informatics
 Purpose: To take a value and print it in the formula for a pentagonal number
"""

n = int(input("What number would you like to display as a pentagonal number? "))

print(n, '(3(', n, ' - 1))/2', ' = ', (n*(3*n-1))/2, sep='')
