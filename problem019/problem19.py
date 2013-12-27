#!/usr/bin/env python2


SUNDAY = 0
DAYS = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
        'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
DaysOfTheMonths = {
        'sep': 30,
        'apr': 30,
        'jun': 30,
        'nov': 30,
        'jan': 31,
        'mar': 31,
        'may': 31,
        'jul': 31,
        'aug': 31,
        'oct': 31,
        'dec': 31}


def isleap(year):
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0


def total_days(year):
    if isleap(year):
        return 366
    else:
        return 365


def days_of_the_month(month, year):
    def feb_days(year):
        if isleap(year):
            return 29
        else:
            return 28
    
    if month == 'feb':
        return feb_days(year)
    else:
        return DaysOfTheMonths[month]


first_day = DAYS.index('mon') #Back in 1900
first_day = (first_day + total_days(1900)) % 7
total_sundays = 0


for y in xrange(1901, 2001):
    for m in MONTHS:
        if first_day == SUNDAY:
            total_sundays += 1
        first_day = (first_day + days_of_the_month(m, y)) % 7


print total_sundays


