"""
 These lines are Python3 comments
 File: tictacto.py 
 Programmer: Allen Tools
 Date: 01/19/2017
 Course ID: LIS 4930 Python for Informatics
 Purpose: write a function to output a tictacto grid 
"""

def rowOfVert():
    """
    Draw the column rows.
    """
    print(' ' * 6, '|', ' ' * 7, '|', ' ' * 6)

def rowOf_():
    """
    Draw the cross sections
    """
    print('_' * 6, '|', '_' * 7, '|', '_' * 6)

column = rowOfVert()
for i in range(5):
    rowOfVert()
rowOf_()
for i in range(5):
    rowOfVert()
rowOf_()
for i in range(5):
    rowOfVert()
