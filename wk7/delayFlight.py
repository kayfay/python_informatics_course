#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:       delayFlight.py
# Programmer: Allen Tools
# Date:       2017-02-24 13:24
# Course ID:  LIS 4930 Python for Informatics
# Purpose:    The return flight from Providence leaves at 6:50 am and, due
# to a mechanical issue, is forced to land at Reagan International Airport in
# Washington DC at 7:35 am.  The crew work on the plane until 1:35 pm before
# passengers can re-board the flight and continue on to Tampa.  The flight
# finally arrives in Tampa at 4:05 pm.  What is the total time the plane was in
# the air?  How long was the delay?  What was the total time it took for
# passengers to get from Providence to Tampa?


class Time():
    """
    A time class object

    Attributes: hour, minutes, seconds
    """


def timeExtractor(time):
    """
    A function to take an input time
    (ex. 24:00) as a string returns
    a list [h, m] (ex. [24, 00])
    """
    return [int(time.split(':')[0]), int(time.split(':')[1])]


Providence = timeExtractor('6:50')
ReaganArival = timeExtractor('7:45')
ReaganDeparture = timeExtractor('12:00') + timeExtractor('1:35')
ReaganDeparture[0] += ReaganDeparture.pop(2)
ReaganDeparture[1] += ReaganDeparture.pop(2)
Tampa = timeExtractor('4:05')

# Inflight in minutes
fDuration = (ReaganArival[0] - Providence[0] + Tampa[0] - 1) * 60 + (
    ReaganArival[1] - Providence[1] + Tampa[1] - ReaganDeparture[1])

print("The passengers were in flight for", fDuration // 60, "hrs and",
      fDuration % 60, "mins.")

# Flight delay in minutes
fDelay = (ReaganDeparture[0] - ReaganArival[0]) * 60 + (ReaganDeparture[1] -
                                                        ReaganArival[1])

print("The passengers were delayed by", fDelay // 60, "hrs and", fDelay % 60,
      "mins")

# Total travel time
tTime = (fDelay + fDuration)

print("The total time it took to get to their destination was", tTime // 60,
      "hrs and", tTime % 60, "mins.")
