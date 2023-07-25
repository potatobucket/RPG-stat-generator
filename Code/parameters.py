import csv

races = ["dragonborn", "dwarf", "elf", "gnome", "half-elf", "halfling", "half-orc", "human", "kender", "tiefling"]
characterClasses = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]
prefixes = []
firstNames = []
lastNames = []
suffixes = []

with open("Roleplaying Names List.csv", "r") as names:
    csv_reader = csv.DictReader(names)
    # next(csv_reader)
    for line in csv_reader:
        if line["Prefix"] != "":
            prefixes.append(line["Prefix"])
        if line["First Name"] != "":
            firstNames.append(line["First Name"])
        if line["Last Name"] != "":
            lastNames.append(line["Last Name"])
        if line["Suffix"] != "":
            suffixes.append(line["Suffix"])
