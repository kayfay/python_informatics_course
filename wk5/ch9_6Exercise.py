 #File:       ch9_6Exercise.py 
 #Programmer: Allen Tools
 #Date:       02/09/2017
 #Course ID:  LIS 4930 Python for Informatics
 #Purpose:    Write a function called is_abcecedarian that returns True
 #            if the letters are in alphabetical order, how many are there?


# reads a word from the wordlist
wordlist = open('/home/atools/Downloads/pythonLIS/sourcefiles/wk5/words.txt')

totalAbecedarians = 0 # here's our counter

def is_abecedarian(word):
    """
    a function to compare last letter to current letter in a loop
    """
    previousLetter = word[0]                 # sets the starting letter
    for currentLetter in word:
        if currentLetter < previousLetter:   # tests iteration letter
            return False
        previousLetter = currentLetter       # updates the starting letter
    return True

for word in wordlist:
    word = word.strip()
    if is_abecedarian(word):
        totalAbecedarians += 1

print("The total number of Abecedarians in the wordlist is", totalAbecedarians)
