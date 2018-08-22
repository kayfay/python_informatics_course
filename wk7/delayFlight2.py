#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:       providenceToTampa2.py
# Programmer: Allen Tools
# Date:       2017-03-02
# Course ID:  LIS 4930 Python for Informatics
# Purpose:    The return flight from Providence leaves at 6:50 am and, due
# to a mechanical issue, is forced to land at Reagan International Airport in
# Washington DC at 7:35 am.  The crew work on the plane until 1:35 pm before
# passengers can re-board the flight and continue on to Tampa.  The flight
# finally arrives in Tampa at 4:05 pm.  What is the total time the plane was in
# the air?  How long was the delay?  What was the total time it took for
# passengers to get from Providence to Tampa?


class Time:
    """
    Represents the time of day.

    attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        """
       Intializes a time object.

       hour: as an int where is 0 to 9
       minute: as an int where is 0 to 9
       second: as an int or float where is 0 to 9 or 0.0 to 9.9
       """
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """
       Returns a string representation of the time. like time 00:00:00
       """
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def print_time(self):
        """
       Prints a string representation of time.
       """
        print(str(self))

    def time_to_int(self):
        """
        Computes the number of seconds since midnight.
        """
        minutes = self.hour * 60 + self.minute  # ex hr=1,min=2,sec=3
        seconds = minutes * 60 + self.second  # min*60 + 3
        return seconds

    def is_after(self, other):
        """
        Returns true if t1 is after t2; false otherwise.
        """
        return self.time_to_int() > other.time_to_int()

    def __add__(self, other):
        """
        Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):  # isinstance is a checker
            # other is something like 00:00:00
            # and time is the time class
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """
        Adds two Time objects or a Time object and a number.
        """
        return self.__add__(other)

    def add_time(self, other):
        """
        Adds two time objects.
        """
        assert self.is_valid() and other.is_valid()
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        """
        Returns a new Time that is the sum of this time and seconds.
        """
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_valid(self):
        """
        Checks whether a Time object satisifies the invariants.
        """
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True


def int_to_time(seconds):
    """
    Makes a new Time object

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time


start = Time(6, 50)

stop = Time(7, 35)

resume = Time(1, 35)

land = Time(4, 5)

print("The total time the plane was in the air:")
# take the morning take off time and subtract it from the morning mechanical
# failure time 7:35 - 6:50
morningDurationSeconds = (stop.time_to_int() - start.time_to_int())
# since they were all calculated by converting them into a bunch of seconds
# in example 6:50 * 120 seconds = 3720 seconds
# I used the int_to_time function to change the duration
# into an hours, minutes, seconds format
morningDurationHMS = int_to_time(morningDurationSeconds)

# take the afternoon take off time, after fixing the mecanial problem
# and subtract it from the time when the plan landed in tampa
afternoonDurationSeconds = (land.time_to_int() - resume.time_to_int())
afternoonDurationHMS = int_to_time(afternoonDurationSeconds)

print(morningDurationHMS + afternoonDurationHMS, "in Hours, Minutes, Seconds")

print("The delay duration:")
"""those poor passengers had to wait in the bar drinking mohitos"""
delay = (stop.time_to_int() - resume.time_to_int())
print(int_to_time(delay))

print("The total time:")
print(start + land)
