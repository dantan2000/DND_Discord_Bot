import random

class DiceRoll:
    def __init__(self, numRolls, numSides, mod):
        self.numRolls = numRolls
    
    def roll(self):
        rolled = []
        for x in range(self.numRolls):
            rolled.append(random.randint(1, self.numSides))
        rolled.append(self.mod)
        return rolled