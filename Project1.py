# File: Project1.py
# Student: Ruijia Huang
# UT EID: rh38477
# Course Name: CS303E
# 
# Date Created: 10/7/2021
# Date Last Modified: 10/8/2021
# Description of Program: Takes an input that represents a month in 2022(1-12)
# and then prints out a calendar for that month with a centered header, 7 columns
# for the days of the week, and empty lines as padding.

#Returning the name of the month
def monthName(month):
    if (month == 1):
        return "January 2022"
    elif (month == 2):
        return "February 2022"
    elif (month == 3):
        return "March 2022"
    elif (month == 4):
        return "April 2022"
    elif (month == 5):
        return "May 2022"
    elif (month == 6):
        return "June 2022"
    elif (month == 7):
        return "July 2022"
    elif (month == 8):
        return "August 2022"
    elif (month == 9):
        return "September 2022"
    elif (month == 10):
        return "October 2022"
    elif (month == 11):
        return "November 2022"
    elif (month == 12):
        return "December 2022"

#Returning the first day of the month given(0-6)
def firstDayOfMonth(month):
    if(month == 1):
        return 6
    elif(month == 2):
        return 2
    elif(month == 3):
        return 2
    elif (month == 4):
        return 5
    elif (month == 5):
        return 0
    elif (month == 6):
        return 3
    elif (month == 7):
        return 5
    elif (month == 8):
        return 1
    elif (month == 9):
        return 4
    elif (month == 10):
        return 6
    elif (month == 11):
        return 2
    elif (month == 12):
        return 4

#Returning how many days there are in the given month
def daysInMonth(month):
    if(month == 1):
        return 31
    elif(month == 2):
        return 28
    elif(month == 3):
        return 31
    elif (month == 4):
        return 30
    elif (month == 5):
        return 31
    elif (month == 6):
        return 30
    elif (month == 7):
        return 31
    elif (month == 8):
        return 31
    elif (month == 9):
        return 30
    elif (month == 10):
        return 31
    elif (month == 11):
        return 30
    elif (month == 12):
        return 31

#Taking month input
month = int(input("Enter the number of a month [1..12]: "))

#Checking whether the input is valid
while(month > 12 or month < 1):
    print("Month must be between 1 and 12. Try again!")
    month = int(input("Enter the number of a month [1..12]: "))


#Printing the calendar header
print("")
print(monthName(month).center(21))
print(" Su Mo Tu We Th Fr Sa")

#Printing the first line(empty space)
for counter in range(firstDayOfMonth(month)):
    print("   ", end="")

#Printing days
day = 1
startDay = firstDayOfMonth(month)

for day in range(1, daysInMonth(month)+1):
    if(startDay < 6):
        print(format(day, '3'), end="")
        day +=1
        startDay += 1
    elif(startDay == 6 and day != daysInMonth(month)):
        print(format(day, '3'), end="")
        print()
        day += 1
        startDay = 0
    elif(day == daysInMonth(month)):
        print(format(day, '3'))
        break

print()


