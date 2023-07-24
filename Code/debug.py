import random as rnd
import character

jimothy = character.Character()

statArray = []
statSpread = []

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

def assign_stats():
    for stat in jimothy.stats:
        jimothy.stats[stat] = generate_stat()
        statSpread.append(jimothy.stats[stat])

def check_stat_total(spread = statSpread):
    newStatTotal = 0
    for check in spread:
        newStatTotal += check
    return newStatTotal

def check_number_bigness(array = statSpread):
    bigNumbers = 0
    for number in array:
        if number >= 15:
            bigNumbers += 1
    return bigNumbers

def pass_or_fail(statTotal, bigNumbers):
    if statTotal >= 75 and bigNumbers >= 2:
        return True
    else:
        return False
    
assign_stats()
check_stat_total()

print(statSpread, check_stat_total(), check_number_bigness())
print(pass_or_fail(check_stat_total(), check_number_bigness()))
