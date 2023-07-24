class Character:
    def __init__(self, prefix = "Mister", firstName = "Jimothy", lastName = "Bimothy", suffix = ", Esq.", race = "Human", characterClass = "Fighter"):
        self.prefix = prefix
        self.firstName = firstName
        self.lastName = lastName
        self.race = race
        self.suffix = suffix
        self.characterClass = characterClass
        self.stats = {
            "Strength" : 0,
            "Dexterity" : 0,
            "Constitution" : 0,
            "Intelligence" : 0,
            "Wisdom" : 0,
            "Charisma" : 0
        }
