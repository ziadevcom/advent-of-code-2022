# Solving day 4 of Advent of Code
# https://adventofcode.com/2022/day/4#part1
# Part B / 2

# Find the number of pairs in which ranges overlap
# i.e - In 2-8,3-7 overlaps all of the sections 3 through 7.

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


# return whether current pair has a range which fully contains the other one
def comparePair(pair):
    elf_1 = pair["elf_1"]
    elf_2 = pair["elf_2"]
    if inRange(elf_1, elf_2):
        return True
    return False


# Check if range 1 exits in range 2
# Conditional checks if the end of the range 2 is lower than range 1 start or start of the range 2 is higher than the end of the range 1, if that condition is true, it means the range is not overlapping
def inRange(range1, range2):
    if range2[1] < range1[0] or range2[0] > range1[1]:
        return False
    else:
        return True

main()