# Solving day 1 of Advent of Code
# https://adventofcode.com/2022/day/1
# Part A / 2
# Dont have part A for first day (Deleted that code without realizing)


numbers = []
with open('input.txt', 'r') as file:
    f = file.readlines()
    number = 0
    for word in f:
        if (word == '\n'):
            numbers.append(number)
            number = 0
        else:
            number = number + int(word)


# find largest elment in array
def largest(arr):
    large = max(arr)
    arr.pop(arr.index(large))
    return large


topThree = 0

for i in range(0, 3):
    topThree = topThree + largest(numbers)

print(topThree)