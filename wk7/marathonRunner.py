#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:       marathonrner.py
# Programmer: Allen Tools
# Date:       Feb 23 2017
# Course ID:  LIS 4930 Python for Informatics
# Purpose:    A marathon runner in training leaves her house at 5:42 am. She
# runs the first two miles at a slow pace (8:25 per mile), then runs seven
# miles at her training pace (7:15 per mile). She finishes with two miles
# at her slow pace. What time is it when she gets home for breakfest.


class Time:
    """
    Represents the time of day.

    attributes: hour, minute, second
    """


# Start time
sTime = Time()
sTime.minutes = 42
sTime.hours = 5

sH = sTime.hours
sM = sTime.minutes

# Run time
rTime = Time()
rTime.seconds = (2 * 25 + 7 * 15 + 2 * 25)
rTime.minutes = (2 * 8 + 7 * 7 + 2 * 8)

# Run time time blocks
rS = rTime.seconds % 60
rM = rTime.seconds // 60 + rTime.minutes % 60
rH = rTime.minutes // 60

# Breakfast time blocks
bH = sH + rH + (sM + rM) // 60
bM = (sM + rM) % 60

# following PEP8 guidelines is to delimit newlines by each comma and adhear to
# 79 character line length
print(
    "My wife leaves the house at ",
    sH,
    ":",
    sM,
    "AM ",
    "for her morning run. \nShe usually goes on a",
    rH,
    " hr ",
    rM,
    " mins ",
    rS,
    " secs",
    " long run.",
    "\nI know breakfast has to be ready at: ",
    bH,
    ":",
    format(bM, '02'),
    "AM\n",
    sep='',
    end='')
