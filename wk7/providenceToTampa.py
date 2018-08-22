#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:       providenceToTampa.py
# Programmer: Allen Tools
# Date:       2017-02-24 07:42
# Course ID:  LIS 4930 Python for Informatics
# Purpose:    A flight leaves Tampa International Airport (TIA) at 2:34 pm
# heading for Providence, Rhode Island (PVD). The plane arrives at 6:14 pm.
# What is the total duration of the flight?


class Time:
    """
    A time keeping class

    Attributes: hour, minutes, seconds
    """


# Arival and departure
aTime = Time()
aTime.hour = 6
aTime.minutes = 14

aH = aTime.hour
aM = aTime.minutes

dTime = Time()
dTime.hour = 2
dTime.minutes = 34

dH = dTime.hour
dM = dTime.minutes

# Sum up the durations
durTotal = ((aH - dH) * 60) + (aM - dM)

print("The flight from Tampa Int. Airport to Providence, RH has a",
      durTotal // 60, "hours and", durTotal % 60, "minute travel time.")
