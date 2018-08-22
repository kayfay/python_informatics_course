# File: ch9_1Exercises.py
# Programmer: Allen Tools
# Date: 02/09/2017
# Course ID: LIS 4930 Python for Informatics
# Purpose: Write a program that reads words.txt and prints only the words more
#          than 20 characters (not counting whitespace).

print("Provide file location to use: ")
print(" ex. /home/atools/Downloads/pythonLIS/sourcefiles/wk5/words.txt ")
file = input("")

listOfWords = open(file)

for line in listOfWords:
    word = line.strip()
    if len(word) >= 20:
        print(word)
