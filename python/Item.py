import DiceRoll

class Item:
    
    def __init__(self, i_name, i_desc, i_value, i_types):
        self.i_name = i_name
        self.i_desc = i_desc
        self.i_value = i_value
        self.i_types = i_types

    def getName(self):
        return self.i_name

    def getDesc(self):
        return self.i_desc

    def getValue(self):
        return self.i_value

    def isType(self, t):
        for i_type in i_types:
            if t == i_type:
                return True
        return False

class Weapon(Item):

    def __init__(self, i_name, i_desc, i_value, i_types, numRolls, numSides, hitMod, dmgMod):
        super().__init__(i_name, i_desc, i_value, i_types)
        self.hitRoll = DiceRoll(1, 20, hitMod)
        self.dmgRoll = DiceRoll(1, numSides, dmgMod)

    def rollHit(self):
        return self.hitRoll.roll()
    
    def rollDmg(self):
        return self.dmgRoll.roll()

class Armor(Item):
    def __init__(self, i_name, i_desc, i_value, i_types, armorClass):
        super().__init__(i_name, i_desc, i_value, i_types)
        self.armorClass = armorClass

    def getArmorClass(self):
        return self.armorClass

items = []

def getItem(itemName):
    for i in items:
        if i_name.lower() == itemName.lower():
            return i
    raise KeyError(f"No item of name {itemName}")