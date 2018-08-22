 #File: ch9_2Exercise.py 
 #Programmer: Allen Tools
 #Date: 02/09/2017
 #Course ID: LIS 4930 Python for Informatics
 #Purpose: Write a function called use_no_e that returns True if the given word
 #         doesn't have the letter "e"

# Inputs the wordlist
wordlist = "/home/atools/Downloads/pythonLIS/sourcefiles/wk5/words.txt"

# reads a word from the wordlist
listOfWords = open(wordlist)


def use_no_e(word):
    """
    A function to look for a letter in a word
    """
    for letter in word:
        if letter == 'e':
            return False
    return True

percentNumerator = 0

listOfWords = open(wordlist)

for line in listOfWords:
    word = line.strip()
    if use_no_e(word):
        percentNumerator += 1

percentDenominator = 0

listOfWords = open(wordlist)
line = listOfWords.readline()

for line in listOfWords:
    percentDenominator += 1

percent = percentNumerator / percentDenominator * 100
print("The percent is of words without e in the list is ", round(percent), "%", sep='')

