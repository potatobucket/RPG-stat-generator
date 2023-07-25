import os
import csv

prefixes = []
firstNames = []
lastNames = []
suffixes = []

main_path = os.path.dirname(__file__)
file_name = "C:/Users/potat/Desktop/Python Projects/RPG-stat-generator/Roleplaying Names List.csv"
file_path = os.path.join(main_path, file_name)
with open(file_path, "r") as whatevs:
    csv_reader = csv.DictReader(whatevs)
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

print(prefixes)
print(firstNames)
print(lastNames)
print(suffixes)
