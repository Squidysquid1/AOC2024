
#315 - 306
def SolveStar1():
    lines = []
    # Open the file in read mode
    with open('day08/simpleinput.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            lines.append(line)


    cords = dict()
    for lineIndex in range(len(lines)):
        line = lines[lineIndex]
        for charIndex in range(len(line)): 
            char = line[charIndex]

            if (char != '.') and (char != '\n') and (char != '#'):
                cord = (charIndex, lineIndex)
                if char in cords.keys():
                    cords[char].append(cord)
                else:
                    cords[char] = [cord]

    uniqueAntinode = {}

    for antennas in cords.values():
        print(antennas)
        for j in range(len(antennas)-1):  
            coordToCompare = antennas[j]
            for i in range(j+1, len(antennas)):
                curCoord = antennas[i]
                charIndexDiff = curCoord[0] - coordToCompare[0]
                lineIndexDiff = curCoord[1] - coordToCompare[1]

                uniqueAntinode[(curCoord[0] + charIndexDiff, curCoord[1] + lineIndexDiff)] = 0
                uniqueAntinode[(coordToCompare[0] - charIndexDiff, coordToCompare[1] - lineIndexDiff)] = 0

    total = 0     
    for key in uniqueAntinode.keys():
        if key[1] >= 0 and key[1] < len(lines):
            if key[0] >= 0 and key[0] < len(lines[0]):
                total+=1

    
    print(uniqueAntinode)
    return total
    

def SolveStar2():
    # Open the file in read mode
    with open('day08/input.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            pass

    return -1