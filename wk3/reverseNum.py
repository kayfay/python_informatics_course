 #These lines are Python3 comments
 #File: reverseNum.py 
 #Programmer: Allen Tools
 #Date: 01/27/2017
 #Course ID: LIS 4930 Python for Informatics
 #Purpose: Write a function that takes in an integer of any size, and returns
 #         the number with the digits reversed.


def reverseNums(n):
    """
    Builds a reversed list into a new string
    """
    L = [] # initalizes L as an empty list
    RL = '' # initalizes RL as a string
    for i in str(n): L.append(i) # this makes an iterable
    for i in str(n): RL += L.pop() # this concatinates the list into a string
    print(RL)

print("The reverse of 123 is ", end='')
reverseNums(123)
print("\n")


def reversedNums(n):
    """
    Uses the builtin functions list() on str(n) as an array
    to makes an iterable with list() and the builtin reversed()

    Printing each digit in the list with function arguments sep and end
    blank to appear as a single number
    """
    for i in list(reversed(list(str(n)))):
       print(i, sep='', end='')

print("The reverse of 123 is ", end='')
reversedNums(123)
print("\n")
