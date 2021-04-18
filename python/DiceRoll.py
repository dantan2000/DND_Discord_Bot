import random

class DiceRoll:
    def __init__(self, numRolls, numSides, mod):
        self.numRolls = numRolls
        self.numSides = numSides
        self.mod = mod
    
    def roll(self):
        rolled = []
        for x in range(self.numRolls):
            rolled.append(random.randint(1, self.numSides))
        if self.mod != 0:
            rolled.append(self.mod)
        return rolled
    
    def toString(self):
        modString = f" + {self.mod}" if self.mod != 0 else ""
        return f"{self.numRolls}d{self.numSides}{modString}"