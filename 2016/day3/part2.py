import os

def main():
    totalPossible = isPossible(sortTriples(getInput()))
    print(totalPossible)

def getInput():
    inputArray = []
    with open("input.txt") as f:
        for line in f:
            triple = [int(i) for i in line.split()]                             # Convert to a list of ints
            inputArray.append(triple)
    return inputArray

def sortTriples(inputArray):
    output = []
    row = []
    for i in range(0,3):
        for triple in inputArray:
            row.append(triple[i])
    for i in range(0, int(len(row)/3)):
        triple = []
        triple.append(row.pop(0))
        triple.append(row.pop(0))
        triple.append(row.pop(0))
        output.append(triple)
    return output

def isPossible(array):
    possible = 0
    for triple in array:
        triple.sort()
        if triple[0] + triple[1] > triple[2]:
            possible = possible + 1
    return possible

main()
