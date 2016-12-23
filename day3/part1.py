import os

def main():
    totalPossible = isPossible(getInput())
    print(totalPossible)

def getInput():
    inputArray = []
    with open("input.txt") as f:
        for line in f:
            triple = [int(i) for i in line.split()]                             # Convert to a list of ints
            triple.sort()
            inputArray.append(triple)
    return inputArray

def isPossible(inputArray):
    possible = 0
    for triple in inputArray:
        if triple[0] + triple[1] > triple[2]:
            possible = possible + 1
    return possible

main()
