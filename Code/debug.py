import stat_generator as sg

statArray = []
testArray = [10, 10, 10, 10, 10, 10]

def assign_stats():
    arrayIndex = 0
    if testArray == []:
        for stat in sg.newGuy.stats:
            sg.newGuy.stats[stat] = sg.generate_stat()
            testArray.append(sg.newGuy.stats[stat])
    else:
        for value in range(len(testArray)):
            testArray[value] = sg.generate_stat()
        for key in sg.newGuy.stats.keys():
            sg.newGuy.stats[key] = testArray[arrayIndex]
            arrayIndex += 1

print(sg.newGuy.stats)
assign_stats()
print(testArray)
print(sg.newGuy.stats)

# for value in range(len(testArray)):
#     print(testArray[value])
