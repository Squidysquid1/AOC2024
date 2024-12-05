import re

def xmasW(lines, lineIndex, charIndex):
    if charIndex < 3:
        return False

    xmas = "XMAS"
    #check for horizontal
    for char in xmas:
        if lines[lineIndex][charIndex] != char:
            return False

        charIndex -= 1
        
    return True


def xmasE(lines, lineIndex, charIndex):

    # check if out of bounds
    if len(lines[lineIndex]) - charIndex < 4:
        return False
    
    xmas = "XMAS"
    #check for horizontal
    for char in xmas:
        if lines[lineIndex][charIndex] != char:
            return False

        charIndex += 1
        
    return True


def xmasS(lines, lineIndex, charIndex):

    # check if out of bounds
    if len(lines) - lineIndex < 4:
        return False

    xmas = "XMAS"
    #check for horizontal
    for char in xmas:
        if lines[lineIndex][charIndex] != char:
            return False

        lineIndex += 1
        
    return True


def xmasN(lines, lineIndex, charIndex):

    # check if out of bounds
    if lineIndex < 3:
        return False

    xmas = "XMAS"
    #check for horizontal
    for char in xmas:
        if lines[lineIndex][charIndex] != char:
            return False

        lineIndex -= 1
        
    return True


def xmasNE(lines, lineIndex, charIndex, word = "XMAS"):
    # check if out of bounds
    if lineIndex < len(word) - 1:
        return False

    if len(lines[lineIndex]) - charIndex < len(word):
        return False

    #check for horizontal
    for char in word:
        if lines[lineIndex][charIndex] != char:
            return False

        lineIndex -= 1
        charIndex += 1
        
    return True


def xmasNW(lines, lineIndex, charIndex, word = "XMAS"):
    if lineIndex < len(word) - 1:
        return False

    if charIndex < len(word) -1:
        return False

    #check for horizontal
    for char in word:
        if lines[lineIndex][charIndex] != char:
            return False

        lineIndex -= 1
        charIndex -= 1
        

    return True


def xmasSE(lines, lineIndex, charIndex, word = "XMAS"):
    # check if out of bounds
    if len(lines) - lineIndex < len(word):
        return False
    
    if len(lines[lineIndex]) - charIndex < len(word):
        return False

    #check for horizontal
    for char in word:
        if lines[lineIndex][charIndex] != char:
            return False

        lineIndex += 1
        charIndex += 1
        

    return True


def xmasSW(lines, lineIndex, charIndex, word = "XMAS"):
    # check if out of bounds
    if len(lines) - lineIndex < len(word):
        return False

    if charIndex < len(word)-1:
        return False

    #check for horizontal
    for char in word:
        if lines[lineIndex][charIndex] != char:
            return False

        lineIndex += 1
        charIndex -= 1
        

    return True


def checkForXmas(lines, lineIndex, charIndex):
    xmasTimes = 0
    if xmasN(lines, lineIndex, charIndex):
        xmasTimes += 1

    if xmasS(lines, lineIndex, charIndex):
        xmasTimes += 1

    if xmasE(lines, lineIndex, charIndex):
        xmasTimes += 1

    if xmasW(lines, lineIndex, charIndex):
        xmasTimes += 1

    if xmasNE(lines, lineIndex, charIndex):
        xmasTimes += 1

    if xmasNW(lines, lineIndex, charIndex):
        xmasTimes += 1

    if xmasSE(lines, lineIndex, charIndex):
        xmasTimes += 1

    if xmasSW(lines, lineIndex, charIndex):
        xmasTimes += 1

    return xmasTimes


def checkForX_Mas(lines, lineIndex, charIndex):
    masTimes = 0

    # NE SE
    if xmasNE(lines, lineIndex, charIndex, "MAS") and xmasSE(lines, lineIndex-2, charIndex, "MAS"):
        masTimes += 1

    # NE NW
    if xmasNE(lines, lineIndex, charIndex, "MAS") and xmasNW(lines, lineIndex, charIndex+2, "MAS"):
        masTimes += 1

    # SW NW
    if xmasSW(lines, lineIndex, charIndex, "MAS") and xmasNW(lines, lineIndex+2, charIndex, "MAS"):
        masTimes += 1

    # SW SE
    if xmasSW(lines, lineIndex, charIndex, "MAS") and xmasSE(lines, lineIndex, charIndex-2, "MAS"):
        masTimes += 1

    return masTimes


def SolveStar1():
    # Open the file in read mode
    lines = []

    with open('day04/input.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            lines.append(line)

    total = 0
    for lineIndex in range(len(lines)):
        for charIndex in range(len(lines[lineIndex])):
            if lines[lineIndex][charIndex] == 'X':
                total += checkForXmas(lines, lineIndex, charIndex)


    return total


def SolveStar2():
    # Open the file in read mode
    lines = []

    with open('day04/input.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            lines.append(line)

    total = 0
    for lineIndex in range(len(lines)):
        for charIndex in range(len(lines[lineIndex])):
            if lines[lineIndex][charIndex] == 'M':
                total += checkForX_Mas(lines, lineIndex, charIndex)

    return total