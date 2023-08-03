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
#-- also handles rerolling in case the total and no. >= 15 thresholds are not met
def assign_stats():
    arrayIndex = 0
    if statSpread == []:
        for stat in newGuy.stats:
            newGuy.stats[stat] = generate_stat()
            statSpread.append(newGuy.stats[stat])
    else:
        for value in range(len(statSpread)):
            statSpread[value] = generate_stat()
        for key in newGuy.stats.keys():
            newGuy.stats[key] = statSpread[arrayIndex]
            arrayIndex += 1

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
    guyID = f"""
    Optional prefix: {newGuy.prefix}
    Name: {newGuy.firstName} {newGuy.lastName}
    Optional suffix: {newGuy.suffix}
    Race: {newGuy.race.title()} | Class: {newGuy.characterClass.title()}\n"""
    for stat in newGuy.stats:
        guyID += f"\t{stat}: {newGuy.stats[stat]}\n"
    return guyID


if __name__ == "__main__":
    #-- initializes the first set of stats for your new character and checks the
    #-- arbitrary limits set on me by Rosetta Code
    assign_stats()
    check_stat_total()
    check_number_bigness()

    #-- if the first set of stats didn't satisfy then this loop will reroll
    #-- until it does (and took me too long to figure out)
    while pass_or_fail(check_stat_total(), check_number_bigness()) == False:
        assign_stats()
        check_stat_total()
        check_number_bigness()

    print(display_character())
