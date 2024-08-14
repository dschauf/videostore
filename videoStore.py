'''
Program: videoStore.py
Chapter 2 practice project #3 (page 63)
Author: Dennis Schauf
Date: 7/24/2024

Simple app that prompts the user for the number of video rentals in pricing categories. Calculates and displays the grand total. 
'''

# variables and constants 
NEW_VIDEOS = 3.0
OLD_VIDEOS = 2.0

# input phase
numNew = int(input("Please enter the number of NEW videos being rented: "))
numOld = int(input("Next, enter the number of OLD videos being rented: "))

# Processing phase 
grandTotal = (NEW_VIDEOS * numNew) + (OLD_VIDEOS * numOld)
grandTotal = round(grandTotal, 2)

# output phase 
print("The customer is renting: " + str(numNew) + " new video(s).")
print("The customer is also renting: " + str(numOld) + " new video(s).")
print("The total charge for the rentals is: $" + str(grandTotal))
input("\nPress ENTER to exit this program..")