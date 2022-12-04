# Solving day 4 of Advent of Code
# https://adventofcode.com/2022/day/4#part1
# Part A / 1

# Find the number of pairs in which one range fully contains the other one

assignmentPairs = []

def main():
    count = 0
    # loading file into memory
    with open('input.txt', 'r') as file:
        text = file.readlines()
        for line in text:
            # formatting and type casting the input
            arr = line.rstrip().split(',')
            pair_1 = arr[0].split('-')
            pair_2 = arr[1].split('-')
            assignmentPairs.append({    
                "elf_1" : [int(pair_1[0]), int(pair_1[1])],
                "elf_2" : [int(pair_2[0]), int(pair_2[1])]
            })
    
    for pair in assignmentPairs:
        if comparePair(pair) == True:
            count += 1

    print(count)

def comparePair(pair):
    # return whether current pair has a range which fully contains the other one
    elf_1 = pair["elf_1"]
    elf_2 = pair["elf_2"]
    res1 = inRange(elf_1, elf_2)
    res2 = inRange(elf_2, elf_1)
    if res1 or res2:
        return True
    return False

def inRange(range1, range2):
    # check if range 1 exits in range 2
    if range1[0] <= range2[0] and range1[1] >= range2[1]:
        return True
    else:
        return False

main()