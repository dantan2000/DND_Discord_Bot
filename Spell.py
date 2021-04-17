import DiceRoll

class Spell:
    def __init__(self, s_name, s_desc, s_lvl, numRolls = 0, numSides = 0, mod = 0):
        self.s_name = s_name
        self.s_desc = s_desc
        self.s_lvl = s_lvl
        self.s_roll = DiceRoll(numRolls, numSides, mod)
    
    def roll():
        return self.s_roll.roll()

    