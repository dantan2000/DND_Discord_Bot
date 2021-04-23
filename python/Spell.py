import DiceRoll

class Spell:
    def __init__(self, s_name, s_desc, s_lvl, s_castTime, s_range = 0, numRolls = 0, numSides = 0, mod = [0]):
        self.s_name = s_name
        self.s_desc = s_desc
        self.s_lvl = s_lvl
        self.s_castTime = s_castTime
        self.s_range = s_range
        self.s_roll = DiceRoll.DiceRoll(numRolls, numSides, mod)
    
    def roll(self):
        return self.s_roll.roll()

    def getInfo(self):
        ret = f"Spell -- {self.s_name}     Level: {self.s_lvl}    Casting Time: {self.s_castTime}    Range: {self.s_range}"
        ret += f"\n   Description: {self.s_desc}"
        if len(self.s_roll.roll()) > 0:
            ret += f"\n   Damage: {self.s_roll}"
        return ret

    