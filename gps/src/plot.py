#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv
from pylab import *


def read_csv_file(filename):
    """
    Returns a list file containing strings of colulmns from a csv

    args: csv file
    returns: list of strings
    """
    data = []
    with open(filename) as infile:
        csvfile = csv.reader(infile)
        for row in csvfile:
            data.append(row)
    return data


def list_gps_commands(data):
    """
    Takes a list of strings and checks for a value then generates a dictionary
    of GPS commands and their frequency

    args: list data with GPS commands at index 0
    returns: dictionary {GPS Command : occurances}
    """
    gps_cmds = dict()
    for row in data:
        try:
            gps_cmds[row[0]] += 1
        except KeyError:
            gps_cmds[row[0]] = 1
    return gps_cmds


#==== Main Program ====#
filename1 = '../data/GPS-2008-06-04-09-03-45.csv'
filename2 = '../data/GPS-2008-05-30-09-00-50.csv'

filecontents = read_csv_file(filename)

print("The number of records in the file is ", len(filecontents))

gps_commands = list_gps_commands(filecontents)

x_data = []
x_labels = []

for command in gps_commands:
    x_data.append(gps_commands[command])
    x_labels.append(command)

bars = arange(len(x_data))
bar(bars, x_data, align='center')
xticks(bars, x_labels, rotation=-10)
ylabel("Number of Unique Commands")
title('Unique GPS Commands Found in File')

figure()  # from pylab

# y = [1, 2, -1, 1]
# x = [10, 11, 12, 13]
#
# plot(x, y, 'o')
# title('Simple Plots')

# i = arange(6)

# plot(i, sin(i), 'k+', i, cos(i), 'm:')
# title("plot(i, sin(i), 'k+', i, cos(i), 'm:')")

# plot(i, sin(i), lw=4)
# plot(i, cos(i), lw=2)

show()
