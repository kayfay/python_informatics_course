"""
 These lines are Python3 comments
 File: sumANumsDigits.py 
 Programmer: Allen Tools
 Date: 01/19/2017
 Course ID: LIS 4930 Python for Informatics
 Purpose: takes a number and sums its digits
"""

value = input("Enter a number bigger than 10: ")
sum = 0
for i in list(str(value)): # this isn't that weird I promise just
    sum += int(i)          # makes 999999 into ['9','9','9','9','9','9','9']
                           # then adds each one by one
print(sum)
