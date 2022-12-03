# Solving day 3 of Advent of Code
# https://adventofcode.com/2022/day/3#part1
# Part A / 1

rucksacks = [] # Array of dictionaries, each dictionary is an ruck sack with two compartments
Points = []

def main():

    # Opening the text file and loading it in a dictionary (rucksacks)
    with open('input.txt', 'r') as file:
        puzzleInput = file.readlines()
        for rucksack in puzzleInput:
            str = rucksack.rstrip() # String the new line indetifier from string (\n)
            mid = round((len(str) / 2)) # End of the first compartment string & start of second
            rucksacks.append({"compartment1" : str[0: mid], "compartment2" : str[mid:] }) # Dividing the string into two parts before appending

    # 1. Looping through all rucksacks
    # 2. Finding mutual value in both compartment
    # 3. Calculating point for that value
    # 4. Appending calculated point in Points array
    for rucksack in rucksacks:
        points = calculatePoints(fineMutualItem(rucksack))
        Points.append(points)

    # Printing Sum of all Points after all the calculations
    print(sum(Points))

def fineMutualItem(rucksack):
    compartment_1 = rucksack["compartment1"]
    compartment_2 = rucksack["compartment2"]

    for letter in compartment_1:
            if letter in compartment_2:
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