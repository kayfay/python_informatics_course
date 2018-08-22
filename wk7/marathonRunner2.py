#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:       marathonRunner2.py
# Programmer: Allen Tools
# Date:       2017-03-02
# Course ID:  LIS 4930 Python for Informatics
# Purpose:    A marathon runner in training leave her house at 5:42 am.
# She runs the first two miles at a slow pace (8:25 per mile), then runs
# seven miles at her training pace (7:15 per mile).  She finishes with two
# miles at her slow pace.  What time is it when she gets home for
# breakfast? 


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


start = Time(5, 42)
start = start.time_to_int()
print('start = ', start)

a = Time(0, 8, 25)
a = a.time_to_int()
a *= 2
print('a = ', a)

b = Time(0, 7, 15)
b = b.time_to_int()
b *= 7
print('b =', b)

c = Time(0, 8, 25)
c = c.time_to_int()
c *= 2
print('c =', c)

breakfastTime = int_to_time(start + a + b + c)

print("The runner get's home at", breakfastTime)
