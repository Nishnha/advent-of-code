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

#           1
#       2   3   4
#   5   6   7   8   9
#       A   B   C
#           D

def findNext(char, letter):
    L = {1:1, 2:2, 3:2, 4:3, 5:5, 6:5, 7:6, 8:7, 9:8, 'A':'A', 'B':'A', 'C':'B', 'D':'D'}
    R = {1:1, 2:3, 3:4, 4:4, 5:6, 6:7, 7:8, 8:9, 9:9, 'A':'B', 'B':'C', 'C':'C', 'D':'D'}
    U = {1:1, 2:2, 3:1, 4:4, 5:5, 6:2, 7:3, 8:4, 9:9, 'A':6, 'B':7, 'C':8, 'D':'B'}
    D = {1:3, 2:6, 3:7, 4:8, 5:5, 6:'A', 7:'B', 8:'C', 9:9, 'A':'A', 'B':'D', 'C':'C', 'D':'D'}

    if letter == "L":
        return L[char]
    if letter == "R":
        return R[char]
    if letter == "U":
        return U[char]
    if letter == "D":
        return D[char]

main()
