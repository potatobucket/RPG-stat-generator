import random as rnd
import character
import parameters as prm

#-- generates a new character with a random name (including honorofics and titles, though they can be ignored if desired), race and class
newGuy = character.Character(rnd.choice(prm.prefixes), rnd.choice(prm.firstNames), rnd.choice(prm.lastNames), rnd.choice(prm.suffixes), rnd.choice(prm.races), rnd.choice(prm.characterClasses))

#-- used for handling stats as they're being generated
#-- statArray is the pool for dice rolls for each stat
#-- statSpread is the end result for all six stats in the order they were rolled
statArray = []
statSpread = []

#-- generates a stat using the rule "roll 4d6, drop the lowest value"
def generate_stat():
    statArray = []
    statTotal = 0
    for die in range(4):
        stat = rnd.randrange(1, 7)
        statArray.append(stat)
    statArray.sort()
    statArray.pop(0)
    for roll in statArray:
        statTotal += roll
    return statTotal

#-- generates a value for strength, dexterity, constitution, intelligence, wisdom and charisma stats
def assign_stats():
    for stat in newGuy.stats:
        newGuy.stats[stat] = generate_stat()
        statSpread.append(newGuy.stats[stat])

#-- returns the total value of all of the character's stats added together
def check_stat_total(spread = statSpread):
    newStatTotal = 0
    for check in spread:
        newStatTotal += check
    return newStatTotal

#-- returns the total number of stats whose total is greater than the given threshold
def check_number_bigness(array = statSpread):
    bigNumbers = 0
    for number in array:
        if number >= 15:
            bigNumbers += 1
    return bigNumbers

#-- checks if the stats satisfy the arbitrary restrictions of having a total of
#-- more than 75 and at least two values of 15 or more
def pass_or_fail(statTotal, bigNumbers):
    if statTotal >= 75 and bigNumbers >= 2:
        return True
    else:
        return False

def display_character():
    print(f"Name: {newGuy.firstName} {newGuy.lastName}")
    print(f"Race: {newGuy.race.title()} | Class: {newGuy.characterClass.title()}")
    for stat in newGuy.stats:
        print(f"    {stat}: {newGuy.stats[stat]}")


if __name__ == "__main__":
    assign_stats()
    display_character()
