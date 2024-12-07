# part of original star solution
def get_bit(number, index):
    mask = 1 << index
    return 1 if (number & mask) else 0

# original star 1 solution
def checkAllOperators(solution, nums):
    #1 mean *, 0 mean +
    #choose what combo of operator
    for binNum in range(2**(len(nums))):
        total = nums[0]
        for i in range(1, len(nums)):
            if get_bit(binNum, i) == 1:
                total *= nums[i]
            elif get_bit(binNum, i) == 0:
                total += nums[i]

        if total == solution:
            return True
            
    return False


def checkWithRecursion(solution, nums, total = 0):
    if solution == total:
        return True
    if len(nums) == 0:
        return False
    if total > solution:
        return False
    
    # + * ||
    return (checkWithRecursion(solution, nums[1:], total + nums[0]) 
            or checkWithRecursion(solution, nums[1:], total * nums[0]) )

def checkWithRecursionNewOperator(solution, nums, total = 0):
    if solution == total and len(nums) == 0:
        return True
    if total > solution:
        return False
    if len(nums) == 0:
        return False
  
    
    # + * ||
    return (checkWithRecursionNewOperator(solution, nums[1:], total + nums[0]) 
         or checkWithRecursionNewOperator(solution, nums[1:], total * nums[0]) 
         or checkWithRecursionNewOperator(solution, nums[1:], int(str(total) + str(nums[0]))) )




def SolveStar1():
    lines = []
    
    # Open the file in read mode
    with open('day07/input.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            convertedLine = line.split()
            convertedLine[0] = convertedLine[0][:-1]
            lines.append([int(x) for x in convertedLine])

    total = 0
    for line in lines:
        solution = line[0]
        if checkWithRecursion(solution, line[1:]):
            total += solution

    return total
    

def SolveStar2():
    lines = []
    
    # Open the file in read mode
    with open('day07/input.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            convertedLine = line.split()
            convertedLine[0] = convertedLine[0][:-1]
            lines.append([int(x) for x in convertedLine])

    total = 0
    for line in lines:
        solution = line[0]
        if checkWithRecursionNewOperator(solution, line[1:]):
            total += solution
    return total
    