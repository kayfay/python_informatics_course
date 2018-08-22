# File: webScraper.py
# Programmer: Allen Tools
# Date: 02/16/2017
# Course ID: LIS 4930 Python for Informatics
# Purpose: Write a program that uses urllib to display a city name and
#          population given a url using uszip.com

import urllib.request

print("Provide me a zipcode to look up the name and")
print("population of the city and state")
zipcode = input()
requestURL = 'http://www.uszip.com/zip/' + zipcode

# creates a list of each line of HTML from the website
HTMLlinesClean = []
with urllib.request.urlopen(requestURL) as url:
    for HTMLlines in url:
        HTMLlines = HTMLlines.decode('utf-8')  # changes from bytecode to ascii
        HTMLlines = HTMLlines.strip()  # strips out whitespace
        HTMLlinesClean.append(HTMLlines)  # builds the clean HTML list


def lookMeUp(lookUp, lineByLineList):
    """
    This is a function to look up an HTML tag and print it's contents
    Given the arguments lookUp term and a list of HTML strings

    Starts by building indexes from the lookUp word
    """
    endWordIndex = len(lookUp) + 1
    printStartIndex = endWordIndex + 1
    printEndIndex = -(endWordIndex + 2)

    for listitem in lineByLineList:
        if listitem[1:endWordIndex] == lookUp:
            print(listitem[printStartIndex:printEndIndex], end='')


# Displays the name of the location
print('\nThe city and state you looked up is: ', end='')
lookMeUp('title', HTMLlinesClean)
print('', zipcode, '\n')

# End of name parsing and displaying

#################################################################
#
# population technique reduces the HTMLlinesClean list
# down to it's zip-code component and splits that component into
# a list then locates the index for total population
# and parses the population for display
#
#################################################################

# build's population list by searching for zip's in HTML
population = []
for line in HTMLlinesClean:
    if line[11:14] == 'zip':
        line = line.split('<')
        population.append(line)

# segments specific to the zip-code population portion
population = population[0]

# the index for the population is two indicies more than the index
# returned for by searching for 'Total population' in the HTML
popIndex = population.index('dt>Total population') + 2

# Displays the population of the location
print("The total population is", population[popIndex][3:])

url.close()
