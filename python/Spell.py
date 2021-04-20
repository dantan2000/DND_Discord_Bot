import DiceRoll

class Spell:
    def __init__(self, s_name, s_desc, s_lvl, s_range = 0, numRolls = 0, numSides = 0, mod = 0):
        self.s_name = s_name
        self.s_desc = s_desc
        self.s_lvl = s_lvl
        self.s_range = s_range
        self.s_roll = DiceRoll(numRolls, numSides, mod)
    
    def roll():
        return self.s_roll.roll()

    def getInfo():
        ret = f"Spell -- {s_name}   Level: {s_lvl}    Range: {s_range}"
        ret += f"\n   Description: {s_desc}"
        if len(self.s_roll.roll()) > 0:
            ret += f"\n   Damage: {self.s_roll}"
        return ret

    