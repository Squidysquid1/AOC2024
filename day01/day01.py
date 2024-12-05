import re
import math

def SolveStar1():

    leftNum = []
    rightNum = []
    # Open the file in read mode
    with open('day01/input.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            nums = line.split("   ")
            leftNum.append(int(nums[0]))
            rightNum.append(int(nums[1]))

    leftNum.sort()
    rightNum.sort()

    total = 0
    for i in range(0, len(leftNum)):
        total += abs(rightNum[i] - leftNum[i])

    return total


def SolveStar2():

    leftNum = []
    rightNum = []
    # Open the file in read mode
    with open('day01/input.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            nums = line.split("   ")
            leftNum.append(int(nums[0]))
            rightNum.append(int(nums[1]))

    leftNum.sort()
    rightNum.sort()

    numberCnt = dict()
    for i in range(len(rightNum)): 
        if rightNum[i] in numberCnt.keys():
            numberCnt[rightNum[i]] += 1
        else:
            numberCnt[rightNum[i]] = 1


    total = 0
    for i in range(len(leftNum)):
        if leftNum[i] in numberCnt.keys():
            total += leftNum[i] * numberCnt[leftNum[i]]

    return total


# Use heap
def SolveStar1Faster():
    pass