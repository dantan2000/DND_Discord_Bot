import random

class DiceRoll:
    def __init__(self, numRolls, numSides, mods):
        self.numRolls = numRolls
        self.numSides = numSides
        self.mods = mods
    
    def roll(self):
        rolled = []
        for x in range(self.numRolls):
            rolled.append(random.randint(1, self.numSides))
        for mod in self.mods:
            if mod != 0:
                rolled.append(mod)
        return rolled
    
    def toString(self):
        modString = ""
        for mod in self.mods:
            if mod != 0:
                modString += f" + {mod}"
        return f"{self.numRolls}d{self.numSides}{modString}"