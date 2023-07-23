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
