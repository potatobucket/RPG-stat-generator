import stat_generator as sg

sg.assign_stats()

print(f"Name: {sg.newGuy.firstName} {sg.newGuy.lastName}")
print(f"Race: {sg.newGuy.race.title()} | Class: {sg.newGuy.characterClass.title()}")
for stat in sg.newGuy.stats:
    print(f"    {stat}: {sg.newGuy.stats[stat]}")
