import re

def is_safe(nums):
    inc = nums[1] > nums[0]
    if inc:
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if not 1 <= diff <= 3:
                return False
        return True
    else:
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if not -3 <= diff <= -1:
                return False
        return True


def is_really_safe(nums):
    if is_safe(nums):
        return True
    for i in range(len(nums)):
        if is_safe(nums[:i] + nums[i+1:]):
            return True
    return False

def SolveStar1():
    # Open the file in read mode
    with open('day02/input.txt', 'r') as file:
        # Read each line in the file
        total = 0
        for line in file:
            level = [int(x.strip()) for x in line.split(" ")]
            total += is_safe(level)

        return total


def SolveStar2():
    # Open the file in read mode
    with open('day02/input.txt', 'r') as file:
        total = 0
        # Read each line in the file
        for line in file:
            level = [int(x.strip()) for x in line.split(" ")]
            total += is_really_safe(level)

    return total