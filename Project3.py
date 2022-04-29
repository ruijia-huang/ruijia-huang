# File: Project3.py
# Student: Ruijia Huang
# UT EID: rh38477
# Course Name: CS303E
# 
# Date Created: 11/29/2021
# Date Last Modified: 11/30/2021
# Description of Program: The program takes information from populationdata.csv and uses it to complete commands
# from the user in a system that can be used to request information about the populations of Texas counties
# as well as state wide. The commands that can be used are help, quit, counties, census, estimate, and growth.
# If a command is not recognized, the system tells the user that it isn't valid and to try again. The program
# keeps asking for commands until the user decides to quit.
# The program also has a function that reads the populationdata csv file and creates a dictionary
# of all Texas counties and their respective census and estimate statistics. It returns that dictionary and a list of
# county names.

import os.path

def readFile():
    fileName = 'populationdata.csv'

    infile = open(fileName, 'r')
    dict = {}
    censusTotal = 0
    estimateTotal = 0
    names = []

    for line in infile:
        if(line[0] == '#'):
            continue
        else:
            lst = line.split(",")
            if len(lst) == 4:
                county = (lst[0] + ' ' + lst[1]).lower()
                census2010 = int(lst[2])
                estimate2020 = int(lst[3])
            else:
                county = lst[0].lower()
                census2010 = int(lst[1])
                estimate2020 = int(lst[2])

            dict[county] = (census2010, estimate2020)
            censusTotal += census2010
            estimateTotal += estimate2020
            names.append(county)

        dict['texas'] = (censusTotal, estimateTotal)

    return dict, names
    

def main():
    if(os.path.isfile('populationdata.csv')):
        dict, names = readFile()

        print("Welcome to the Texas Population Dashboard.")
        print("This provides census data from the 2010 census and")
        print("estimated population data in Texas as of 1/1/2020.")
        print("Creating dictionary from file: populationdata.csv")
        print()
        print("Enter any of the following commands:")
        print("\033[1mHelp -\033[0m list available commands;")
        print("\033[1mQuit -\033[0m exit this dashboard;")
        print("\033[1mCounties -\033[0m list all Texas counties;")
        print("\033[1mCensus <countyName>/Texas -\033[0m population in 2010 census by specified county or statewide;")
        print("\033[1mEstimated <countyName>/Texas -\033[0m estimated population in 2020 by specified county or statewide.")
        print("\033[1mGrowth <countyName>/Texas -\033[0m percent change from 2010 to 2020, by county or statewide.")

        #how to get the county name from the command? how does the parsing for the two word counties work
        while(True):
            print()
            command = input("\033[1mPlease enter a command: \033[0m")
            command = command.lower()

            commWords = command.split()
            comm = commWords[0].strip()
            args = commWords[1:]
            name = " ".join(args).strip()

            if(commWords[0] == 'help'):
                print("\033[1mHelp -\033[0m list available commands;")
                print("\033[1mQuit -\033[0m exit this dashboard;")
                print("\033[1mCounties -\033[0m list all Texas counties;")
                print("\033[1mCensus <countyName>/Texas -\033[0m population in 2010 census by specified county or statewide;")
                print("\033[1mEstimated <countyName>/Texas -\033[0m estimated population in 2020 by specified county or statewide.")
                print("\033[1mGrowth <countyName>/Texas -\033[0m percent change from 2010 to 2020, by county or statewide.")
            elif(commWords[0] == 'counties'):
                counter = 0
                for i in range(len(names)):
                    print(names[i].title(), ", ", sep="", end="")
                    counter += 1
                    if counter == 10:
                        print()
                        counter = 0
                print()
            elif(commWords[0] == 'census'):
                if name == 'texas':
                    census, estimate = dict['texas']
                    print("Texas total population in the 2010 Census:", census)
                elif name in dict:
                    census, estimate = dict[name]
                    print(name.title(), "county had", census, "citizens in the 2010 Census.")
                else:
                    print("County", name.title(), "not recgonized.")
            elif(commWords[0] == 'estimated'):
                if name == 'texas':
                    census, estimate = dict['texas']
                    print("Texas estimated population (January, 2020):", estimate)
                elif name in dict:
                    census, estimate = dict[name]
                    print(name.title(), "county had estimated population (January, 2020):", estimate)
                else:
                    print("County", name.title(), "not recgonized.")
            elif(commWords[0] == 'growth'):
                if name == 'texas':
                    census, estimate = dict['texas']
                    growth = (estimate - census) / census
                    print("Texas had percent population change (2010 to 2020):", format(growth, '.2%'))
                elif name in dict:
                    # also shouldnt texas already be in the dictionary
                    census, estimate = dict[name]
                    growth = (estimate - census) / census
                    print(name.title(), "had percent population change (2010 to 2020):", format(growth, '.2%'))
                else:
                    print("County", name.title(), "not recgonized.")
            elif(commWords[0] == 'quit'):
                print("Thank you for using the Texas Population Database Dashboard. Goodbye!")
                break
            else:
                print("Command is not recognized. Try again!")
    else:
        print("File does not exist.")

main()