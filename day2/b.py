# Solving day 2 of Advent of Code
# https://adventofcode.com/2022/day/2#part2
# Part B / 2

hands = {
    "A": {
        "name" : "rock",
        "defeats" : "scissor",
        "loses" : "paper"
    },
    "B": {
        "name" : "paper",
        "defeats" : "rock",
        "loses" : "scissor"
    },
    "C": {
        "name" : "scissor",
        "defeats" : "paper",
        "loses" : "rock"
    }
}

Points = {
    "rock"    : 1,
    "paper"   : 2,
    "scissor" : 3
}

def main():
    points = 0
    with open('input.txt', 'r') as file:
        for word in file:
            points += makeMove(word[0], word[2])
    print(points)



def makeMove(elf, human):
    points = 0
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win    
    if human == 'X':
        points = 0 + Points[hands[elf]["defeats"]]
    elif human == 'Y':
        points = 3 + Points[hands[elf]["name"]]
    elif human == 'Z':
        points = 6 + Points[hands[elf]["loses"]]
    
    return points


main()