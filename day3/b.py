# Solving day 3 of Advent of Code
# https://adventofcode.com/2022/day/3#part2
# Part B / 2

elfGroups = [] # 2 Dimensional array, each child array is 3 rucksacks per elf group
Points = []

def main():

    # Opening the text file and loading it in a array (groups)
    with open('input.txt', 'r') as file:
        puzzleInput = file.readlines()
        # Grouping 3 runsacks as one and adding to runskacks array
        for i in range(0, len(puzzleInput), 3):
            rucksackGroup = []
            for j in range(i, i+3):
                # Add groups of 3 ruckstacks to temp array
                rucksackString = puzzleInput[j].rstrip()
                rucksackGroup.append(rucksackString)
            
            elfGroups.append(rucksackGroup)


    # 1. Looping through all rucksack groups
    # 2. Finding mutual value each group of 3 ruckstacks
    # 3. Calculating point for that value aka badge
    # 4. Adding calculated point in Points array
    for group in elfGroups:
        findBadge(group)
        points = calculatePoints(findBadge(group))
        Points.append(points)

    # Printing Sum of all Points after all the calculations
    print(sum(Points))

def findBadge(group):
    group_1 = group[0]
    group_2 = group[1]
    group_3 = group[2]
    for letter in group_1:
        if letter in group_2 and letter in group_3:
            return letter
    

def calculatePoints(letter):
    # Convert the input letter to ascii and return the points mapped by upper case or lowercase letters
    # Uppercase alphabets points = 27-52
    # Lowercase alphabets points = 1 - 26
    ascii_letter = ord(letter)
    if letter.islower():
        return ascii_letter - 96
    else:
        return ascii_letter - 38


main()