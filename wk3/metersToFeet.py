 #These lines are Python3 comments
 #File: metersToFeet.py 
 #Programmer: Allen Tools
 #Date: 01/26/2017
 #Course ID: LIS 4930 Python for Informatics
 #Purpose: A script that converts meters to feet

def converter( convrsnFctr = 3.2808 ):
    """
    Simple program to convert two numbers by a conversion factor

    Default is meters to feet
    """
    measurementIn = input( "Type the amount of the"
                          " first type and press enter: " )

    measurementOut =  float(measurementIn) * convrsnFctr 

    print( "The converted measurement is:", round( measurementOut , 2 ) )

converter()
