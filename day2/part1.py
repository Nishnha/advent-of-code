#   1   2   3
#   4   5   6
#   7   8   9

import os

password = []

def main():
    defaultNum = 5
    code(getInput(defaultNum))
    print(password)

def code(num):
    password.append(num)

def getInput(num):
    inputArray = []
    with open("input.txt") as f:
        for line in f:
            for letter in line:
                inputArray.append(letter)
            inputArray.pop()                                                    # Remove the newline character at the end
            iterate(num, inputArray)
            inputArray = []

def iterate(num, array):
    for letter in array:
        num = findNext(num, letter)
    code(num)

def findNext(num, letter):
    L = {1:1, 2:1, 3:2, 4:4, 5:4, 6:5, 7:7, 8:7, 9:8}
    R = {1:2, 2:3, 3:3, 4:5, 5:6, 6:6, 7:8, 8:9, 9:9}
    U = {1:1, 2:2, 3:3, 4:1, 5:2, 6:3, 7:4, 8:5, 9:6}
    D = {1:4, 2:5, 3:6, 4:7, 5:8, 6:9, 7:7, 8:8, 9:9}
    
    if letter == "L":
        return L[num]
    if letter == "R":
        return R[num]
    if letter == "U":
        return U[num]
    if letter == "D":
        return D[num]

main()
