#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:       MLBstats.py
# Programmer: Allen Tools
# Date:       2017-03-30 23:17
# Course ID:  LIS 4930 Python for Informatics
# Purpose:    Write a program that reads in the attached file line b line (e.g.
# a tuple). Create a list(array) of tuples. Then calculate the average number
# of 'at bats' (AB column) for each player in the filed


def infile(location):
    """
     Creates a list from a file using list comprehension

    :location: The directory and file eg. /Downloads/MLB.csv
    :returns: A list of strings
    """

    with open(location, 'r') as MLB:
        return [tuple(line.strip().split(',')) for line in MLB.readlines()]


def stats(infile, column):
    """
    Calculates an average from a list of values given a column

    :file: The file to preform the average operation on
    :column: The column to preform the operation on
    :returns: a list of strings
    """
    avg = 0
    columnIndex = (infile[0].index(column))
    infile.pop(0)

    for row in range(len(infile)):
        avg += int(infile[row][columnIndex])

    print("\n", "The at bat field average is:".rjust(33),
          round(avg / len(infile)))


def players(infile):
    """
    Prints some player info

    :infile: The file with the players and their at bat averages
    """

    for player in range(len(infile)):
        print('\n', infile[player][0].ljust(4), end="")
        print(infile[player][1].center(20), end="")
        for i in [2, 3]:
            print(infile[player][i].ljust(10), end="")


MLBlist = infile('MLB.csv')
players(MLBlist)
stats(MLBlist, 'AB')
