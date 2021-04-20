import Item

class Inventory:
    def __init__(self, gold, items):
        self.gold = gold
        self.items = items
        self.donnedArmor = []

    def donArmor(self, armorName):
        for i in self.items:
            if i.i_name.lower() == armorName.lower():
                if (i.isType(Types.ARMOR) or i.isType(Types.SHIELD)):
                    if len(self.donnedArmor) == 1:
                        if not self.donnedArmor[0].isType(i.i_type):
                            self.donnedArmor.append(i)
                        else:
                            raise ValueError(f"Cannot don a {i.i_type}. Already have one equipped!")
                    elif len(self.donnedArmor == 0):
                        self.donnedArmor.append(i)
                else:
                    raise ValueError(f"You try to don a {armorName}. Everyone around you looks at you strange because its not a piece of armor.")
        return False

    def doffArmor(self, armorName):
        for a in self.donnedArmor:
            if a.i_name.lower() == armornName.lower():
                self.donnedArmor.remove(a)
                return
        raise ValueError(f"Could not doff - don't have a {armorName} equipped")

    def calculateArmor(self):
        AC = 0
        for a in self.donnedArmor:
            AC += a.getArmorClass()
        return AC

    def addItem(self, item, qty):
        try:
            self.items[item.i_name] = (item, self.items[item.i_name][1] + qty)
        except KeyError:
            self.items[item.i_name] = (item, qty)
    
    def removeItem(self, itemName, qty):
        for iName in self.items:
            item_qty = self.items[iName]
            if item_qty[0].i_name.lower() == itemName.lower():
                if item_qty[1] - qty > 0:
                    item_qty[1] -= qty
                elif item_qty[1] - qty == 0:
                    self.items.pop(iName)
                    return
                else:
                    raise ValueError(f"Cannot remove {qty} {item_qty[0].i_name}(s). Only have {item_qty[1]}")
        raise KeyError(f"Item {itemName} not owned.")
            
    def addGold(self, qty):
        newBal = self.gold + qty
        if newBal < 0:
            raise ValueError(f"Cannot add {qty} gold; only have {self.gold} gold.")
        else:
            self.gold = newBal

    def removeGold(self, qty):
        newBal = self.gold - qty
        if newBal < 0:
            raise ValueError(f"Cannot remove {qty} gold; only have {self.gold} gold.")
        else:
            self.gold = newBal
            
    def __str__(self):
        returnStr = ""
        returnStr += f"{self.gold} gp\n"
        for item_qty in self.items:
            item = item_qty[0]
            qty = item_qty[1]
            returnStr += f"{item.i_name}  -- qty: {qty}\n"
        returnStr += "Equipped Armor: "
        armorStr = ""
        for armor in self.donnedArmor:
            armorStr += armor.i_name + ", "
        if len(armorStr) > 0:
            armorStr = armorStr[:len(armorStr) - 2]
        else:
            armorStr = "None"
        return returnStr