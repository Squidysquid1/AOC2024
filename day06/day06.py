def outOfBounds(lines, y, x):
    if len(lines) == y or len(lines[y]) == x:
        return True

    if y == -1 or x == -1:
        return True

    return False

def isSolid(lines, y, x):
    if lines[y][x] == '#':
        return True
    return False

def markPath(lines, y, x, maxIter = 50000):
    found = False
    moves = 0
    direction = 0 # direction 0=N, 1=E, 2=S, 3=W
    iterations = 0
    while not found:
        if iterations > maxIter:
            return -1

        iterations +=1
        # North
        if direction == 0:
            if outOfBounds(lines, y-1, x):
                found = True
            elif isSolid(lines, y-1, x):
                direction = 1
            else:
                y -= 1
                if lines[y][x] == '.':
                    moves += 1
                    lines[y][x] = 'X'
                

        # East
        elif direction == 1:
            if outOfBounds(lines, y, x+1):
                found = True
            elif isSolid(lines, y, x+1):
                direction = 2
            else:
                x += 1
                if lines[y][x] == '.':
                    moves +=1
                    lines[y][x] = 'X'


        # South
        elif direction == 2:
            if outOfBounds(lines, y+1, x):
                found = True
            elif isSolid(lines, y+1, x):
                direction = 3
            else:
                y += 1
                if lines[y][x] == '.':
                    moves +=1
                    lines[y][x] = 'X'


        # West
        elif direction == 3:
            if outOfBounds(lines, y, x-1):
                found = True
            elif isSolid(lines, y, x-1):
                direction = 0
            else:
                x -= 1
                if lines[y][x] == '.':
                    moves +=1
                    lines[y][x] = 'X'

    return moves + 1

def SolveStar1():
    lines = []
    index = 0
    lineIndex = 0
    charIndex = 0
    # Open the file in read mode
    with open('day06/input.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            if '^' in line:
                lineIndex = index
                charIndex = line.find('^')
            lines.append(list(line))
            index += 1
    
    return markPath(lines, lineIndex, charIndex)
    

def SolveStar2():

    lines = []
    index = 0
    lineIndex = 0
    charIndex = 0
    
    # Open the file in read mode
    with open('day06/input.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            if '^' in line:
                lineIndex = index
                charIndex = line.find('^')
            lines.append(list(line))
            index += 1
    
    markPath(lines, lineIndex, charIndex)
    
    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            prev = lines[i][j]
            if prev == 'X':
                lines[i][j] = '#'
                if markPath(lines, lineIndex, charIndex) == -1:
                    count +=1
            lines[i][j] = prev
    

    return count
    