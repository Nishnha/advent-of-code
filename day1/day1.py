# Nishnhs, 3 December 2016

# Parse the list for L and R
# Normal direction is north, for a R direction becomes west, 
# from west, another R turns direction south
# Add up numbers in each direction
# Subtract north from south
# Subtract west from east
# take absolute value of both, total is the distance from starting point

import os
from enum import Enum

class Bering (Enum):
    north = 0
    west  = 1
    south = 2
    east  = 3

distanceMap = {
        Bering(0) : 0, # north
        Bering(1) : 0, # west
        Bering(2) : 0, # south
        Bering(3) : 0  # east
        } 

def main():
    with open("input.txt") as inputText:
        inputString = inputText.readline()[:-1]
    parseInput(inputString)
    printDistance()

def parseInput (inputString):
    currentBering = Bering(0)
    inputArray = inputString.split(",")
    for element in inputArray:
        direction = getDirection(element)
        distance = getDistance(element)
        currentBering = updateDistance(currentBering, direction, distance)

def getDirection (element):
    return element[-2]
        
def getDistance (element):
    return element[-1]

def updateBering (bering, direction):
    if bering is Bering(0):
        if direction is "R":
            bering = Bering(3)
        if direction is "L":
            bering = Bering(1)
    elif bering is Bering(1):
        if direction is "R":
            bering = Bering(0)
        if direction is "L":
            bering = Bering(2)
    elif bering is Bering(2):
        if direction is "R":
            bering = Bering(1)
        if direction is "L":
            bering = Bering(3)
    elif bering is Bering(3):
        if direction is "R":
            bering = Bering(2)
        if direction is "L":
            bering = Bering(0)
    else:
        print("fuck")
    return bering

def updateDistance (currentBering, direction, distance):
    newBering = updateBering(currentBering, direction)
    distanceMap[newBering] = distanceMap[newBering] + int(distance)
    return newBering

def printDistance ():
    print("north", distanceMap[Bering(0)], " west", distanceMap[Bering(1)], " south", distanceMap[Bering(2)], " east", distanceMap[Bering(3)])
    vertical   = abs(distanceMap[Bering(0)] - distanceMap[Bering(2)])
    horizontal = abs(distanceMap[Bering(1)]  - distanceMap[Bering(3)])
    print("total distance moved was ", vertical + horizontal)

main()
