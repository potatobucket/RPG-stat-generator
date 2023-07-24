races = ["dragonborn", "dwarf", "elf", "gnome", "half-elf", "halfling", "half-orc", "human", "kender", "tiefling"]
characterClasses = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]

if __name__ == "__main__":
    for race in races:
        for characterClass in characterClasses:
            print(f"{race.title()} the {characterClass.title()}")
