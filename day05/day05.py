import re


def isUpdateValid (update, rules):
    # LEFT needs to be printed before RIGHT
    for leftNumIndex in range(len(update)):
        
        # only if there are rules for that num
        if update[leftNumIndex] in rules.keys():
            # Get rules for a num
            ruleList = rules[update[leftNumIndex]]
        
            # check if everything before it is valid
            for numToCheck in update[:leftNumIndex]:
                if numToCheck in ruleList:
                    return False

    return True



def swapWhenNotUpdateValid (update, rules):
    # LEFT needs to be printed before RIGHT
    for leftNumIndex in range(len(update)):
        
        # only if there are rules for that num
        if update[leftNumIndex] in rules.keys():
            # Get rules for a num
            ruleList = rules[update[leftNumIndex]]
        
            # check if everything before it is valid
            for rightNumIndex in range(len(update[:leftNumIndex])):
                if update[rightNumIndex] in ruleList:
                    # swap
                    update[leftNumIndex], update[rightNumIndex] = update[rightNumIndex], update[leftNumIndex]
                    return False

    return True

def SolveStar1():

    updates = []
    rules = dict()
    readingRules = True
    # Open the file in read mode
    with open('day05/input.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            if readingRules:
                if line == "\n":
                    readingRules = False
                else:
                    nums = [int(x) for x in line.split('|')]
                    if nums[0] not in rules.keys():
                        rules[nums[0]] = [nums[1]]
                    else:
                        rules[nums[0]].append(nums[1])
            else:
                updates.append([int(x) for x in line.split(',')])

    total = 0
    for update in updates:
        if isUpdateValid(update, rules):
            middleIndex = (len(update) - 1)//2
            total += update[middleIndex]

    return total


def SolveStar2():

    updates = []
    rules = dict()
    readingRules = True
    # Open the file in read mode
    with open('day05/input.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            if readingRules:
                if line == "\n":
                    readingRules = False
                else:
                    nums = [int(x) for x in line.split('|')]
                    if nums[0] not in rules.keys():
                        rules[nums[0]] = [nums[1]]
                    else:
                        rules[nums[0]].append(nums[1])
            else:
                updates.append([int(x) for x in line.split(',')])

    updatesToFix = []
    for update in updates:
        if not isUpdateValid(update, rules):
            updatesToFix.append(update)


    total = 0
    for update in updatesToFix:
        # Keep on swaping until it becomes valid ez pz
        while not swapWhenNotUpdateValid(update, rules):
            pass

        middleIndex = (len(update) - 1)//2
        total += update[middleIndex]

    return total