class Character:
    def __init__(self, name = "Jimothy", race = "Human", characterClass = "Fighter"):
        self.name = name
        self.race = race
        self.characterClass = characterClass
        self.stats = {
            "Strength" : 0,
            "Dexterity" : 0,
            "Constitution" : 0,
            "Intelligence" : 0,
            "Wisdom" : 0,
            "Charisma" : 0
        }
