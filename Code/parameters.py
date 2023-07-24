import csv

races = ["dragonborn", "dwarf", "elf", "gnome", "half-elf", "halfling", "half-orc", "human", "kender", "tiefling"]
characterClasses = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]
prefixes = []
firstNames = []
lastNames = []
suffixes = []

with open("Roleplaying Names List.csv", "r") as names:
    csv_reader = csv.reader(names)
    next(csv_reader)
    for line in csv_reader:
        if line[0] != "":
            prefixes.append(line[0])
        if line[1] != "":
            firstNames.append(line[1])
        if line[2] != "":
            lastNames.append(line[2])
        if line[3] != "":
            suffixes.append(line[3])
