#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:       dictionaries.py
# Programmer: Allen Tools
# Date:       2017-03-09
# Course ID:  LIS 4930 Python for Informatics
# Purpose:    Write a program that uses a dictionary to create a histogram.
# Count the occurances of each letter in the phrase. "Do you think Donald Trump
# wants to be President, or is he just having fun?"

text = "Do you think Donald Trump Wants to be President"
text += ", or is he just having fun?"


def histogram(string):
    frequency = dict()
    for letter in string.lower():
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1

    for i in frequency:
        col = "*" * frequency[i]
        row = i, frequency[i]
        print(str(row).ljust(10), col)


histogram(text)
