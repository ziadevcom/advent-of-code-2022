# Solving day 2 of Advent of Code
# https://adventofcode.com/2022/day/2#part1
# Part A / 1

hands = {
    "A":{
        "name": "rock",
        "points": 1
    },
    "B": {
        "name": "paper",
        "points": 2
    },
    "C": {
        "name": "scissor",
        "points": 3
    },
    "X":{
        "name": "rock",
        "points": 1
    },
    "Y": {
        "name": "paper",
        "points": 2
    },
    "Z": {
        "name": "scissor",
        "points": 3
    },
}

wc = {
    "rock" : {
        "defeats": "scissor"
    },
    "paper" : {
        "defeats": "rock"
    },
    "scissor" : {
        "defeats": "paper"
    }
}

def main():
    points = 0
    with open('input.txt', 'r') as file:
        for word in file:
            result = rps(word[0], word[2])
            points += result
    print(points)

def rps(a, b):
    # result = { "status": "none", "points": 0}
    points = 0;
    move1 = hands[a]["name"]
    move2 = hands[b]["name"]

    if wc[move1]["defeats"] == move2:
        points = 0 + p2
    elif wc[move2]["defeats"] == move1:
        points = 6 + p2
    else:
        points = 3 + p2

    return points

main()