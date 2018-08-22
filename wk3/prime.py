 #These lines are Python3 comments
 #File: prime.py 
 #Programmer: Allen Tools
 #Date: 01/28/2017
 #Course ID: LIS 4930 Python for Informatics
 #Purpose: Write a function that takes an argument for input and
 #         prime or not prime.

def prime(num):
    print(num, "is Prime") if num%2 == 0 else print(num, "is Not Prime")

prime(3)
