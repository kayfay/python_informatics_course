# These lines are Python3 comments
# File: simpleProgram.py
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

firstname = name[:count]  # use [i:j:k] string slicing
lastname = name[count:]  # to seperate the names

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
ALPHABET = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]


def upperCase(nameChange):
    """
    A function to iterate over the alphabet adding to a counter
    and using the counter to index an uppercase alphabet.
    returns a concatination the uppercase alphabet indexed letter
    and name change with the first letter sliced off
    """
    count = 0
    for i in alphabet:
        if i == nameChange[0]:
            return ALPHABET[count] + nameChange[1:]
        else:
            count += 1


firstname = upperCase(firstname)
lastname = upperCase(lastname)

print("Method 1:")
print(firstname, "\n", lastname, sep='')

L = name.split()  # split() returns a list ['firstname', 'lastname']
print("Method 2:")
print(L[0].capitalize(), "\n", L[1].capitalize(), sep='')



def myfunction(arg1, arg2, **kwargs)
    """TODO: Docstring for myfunction.

    :arg1: TODO
    :returns: TODO

    """
    pass
