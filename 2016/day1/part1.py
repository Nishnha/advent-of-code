# Nishnha, 3 December 2016

import os
from enum import Enum

class Bearing (Enum):
    north = 0
    west  = 1
    south = 2
    east  = 3

distanceMap = {
    Bearing.north : 0,
    Bearing.west  : 0,
    Bearing.south : 0,
    Bearing.east  : 0
} 

def main():
    with open("input.txt") as inputText:
        inputString = inputText.readline()[:-1]                                 # Skip the newline character at the end of input.txt
    parseInput(inputString)
    printDistance()

def parseInput (inputString):
    currentBearing = Bearing(0)
    inputArray = inputString.split(", ")
    for element in inputArray:
        direction = getDirection(element)
        distance = getDistance(element)
        currentBearing = updateDistance(currentBearing, direction, distance)

def getDirection (element):
    return element[0]                                                           # L or R
        
def getDistance (element):
    return element[1:]

def updateBearing (bearing, direction):
    if bearing is Bearing(0):
        if direction is "R":
            bearing = Bearing(3)
        if direction is "L":
            bearing = Bearing(1)

    elif bearing is Bearing(1):
        if direction is "R":
            bearing = Bearing(0)
        if direction is "L":
            bearing = Bearing(2)

    elif bearing is Bearing(2):
        if direction is "R":
            bearing = Bearing(1)
        if direction is "L":
            bearing = Bearing(3)

    elif bearing is Bearing(3):
        if direction is "R":
            bearing = Bearing(2)
        if direction is "L":
            bearing = Bearing(0)
 
    return bearing

def updateDistance (currentBearing, direction, distance):
    newBearing = updateBearing(currentBearing, direction)
    distanceMap[newBearing] = distanceMap[newBearing] + int(distance)
    return newBearing

def printDistance ():
    print("north:", distanceMap[Bearing(0)], " west:", distanceMap[Bearing(1)], " south:", distanceMap[Bearing(2)], " east:", distanceMap[Bearing(3)])
    
    vertical   = abs(distanceMap[Bearing(0)] - distanceMap[Bearing(2)])
    horizontal = abs(distanceMap[Bearing(1)]  - distanceMap[Bearing(3)])
    print("total displacement was: ", vertical + horizontal)

main()
