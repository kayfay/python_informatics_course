# These lines are Python3 comments
# File: sort.py
# Programmer: Allen Tools
# Date: 01/19/2017
# Course ID: LIS 4930 Python for Informatics
# Purpose: alphabetize a list of strings using strings compaing to strings

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
str3 = input("Enter the third string: ")

if str1 < str2 and str1 < str3:

    if str2 < str3:

        print(str1, str2, str3)

    else:

        print(str1, str3, str2)

elif str2 < str1 and str2 < str3:

    if str1 < str3:

        print(str2, str1, str3)

    else:

        print(str2, str3, str1)

else:

    if str1 < str2:

        print(str3, str1, str2)

    else:

        print(str3, str2, str1)
