 #File: ch9_3Exercise.py 
 #Programmer: Allen Tools
 #Date: 02/09/2017
 #Course ID: LIS 4930 Python for Informatics
 #Purpose: a set of functions to search through a wordlist for strings 
 #         of letters and display results

# Inputs the wordlist
infile = '/home/atools/Downloads/pythonLIS/sourcefiles/wk5/words.txt'

# reads a word from the wordlist
fin = open(infile)

# creates a global counter
global totalNumberOfWords
totalNumberOfWords = 0

def has_no_e(word):
    """
    Book function for has no e
    """
    for letter in word:
        if letter == 'e':
            return False
        return True

def avoids(word, forbidden):
    """
    Book function for avoids forbidden letters in a word
    """
    for letter in word:
        if letter in forbidden:
            return False
    return True

def uses_only(word, available):
    """
    Book function for uses only available letters in a word
    """
    for letter in word:
        if letter not in available:
            return False
    return True

def uses_all(word, required):
    """
    Book function for uses all of the required letters in a word
    """
    for letter in required:
        if letter not in word:
            return False
    return True

def uses_all2(word, required):
    """
    Book function to preform uses all with the uses only function
    """
    return uses_only(required, word)

def checklist(forThis, function):
    """
    a function to check a list of words for a string of letters
    """
    global totalNumberOfWords
    totalNumberOfWords = 0
    fin = open(infile)
    for word in fin:
        word = word.strip()
        if function(word, forThis):
            totalNumberOfWords += 1

def printChecklist(forThis, function):
    """
    a function to print the words and how many and what function was used
    """
    checklist(forThis, function)
    print("There are", totalNumberOfWords, "words that", function, forThis)

# a loop to use the 'has_no_e' function with the wordlist
for word in fin:
    line = fin.readline()
    word = line.strip()
    if has_no_e(word):
        totalNumberOfWords += 1
print("There are", totalNumberOfWords, "words that have no e")

# function calls on the different functions through the printChecklist function
printChecklist('aeiou', avoids)
printChecklist('acefhlo', uses_only)
printChecklist('aeiou', uses_all)
printChecklist('aeiouy', uses_all2)
