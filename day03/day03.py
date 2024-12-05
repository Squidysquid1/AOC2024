import re

def SolveStar1():
    pattern = re.compile("(?<=mul\\()\\d{1,3},\\d{1,3}(?=\\))")

    toMultiply = []
    # Open the file in read mode
    with open('day03/input.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            toMultiply += re.findall(pattern, line)

    total = 0
    for element in toMultiply:
        nums = element.split(',')
        num1 = int(nums[0])
        num2 = int(nums[1])
        total += num1 * num2

    return total


def SolveStar2():
    pattern = re.compile("((?<=mul\\()\\d{1,3},\\d{1,3}(?=\\)))|(don't\\(\\))|(do\\(\\))")

    toMultiply = []
    # Open the file in read mode
    with open('day03/input.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            toMultiply += re.findall(pattern, line)

    mulEnabled = True
    total = 0
    for instruction in toMultiply:
        # dont
        if instruction[1] != '':
            mulEnabled = False
        elif instruction[2] != '':
            mulEnabled = True
        elif instruction[0] != '' and mulEnabled:
            nums = instruction[0].split(',')
            num1 = int(nums[0])
            num2 = int(nums[1])
            total += num1 * num2
        
    return total