import Item.py

class Inventory:
    def __init__(self, gold, items):
        self.gold = gold
        self.items = items
        self.donnedArmor = []

    def donArmor(self, armorName):
        for i in self.items:
            if i.i_name.lower() == armorName.lower() and (i.isType(Types.ARMOR) or i.isType(Types.SHIELD)):
                if len(self.donnedArmor) == 1:
                    if not self.donnedArmor[0].isType(i.i_type):
                        self.donnedArmor.append(i)
                        return True
                    elif len(self.donnedArmor == 0):
                        self.donnedArmor.append(i)
                        return True
        return False

    def doffArmor(self, armorName):
        for a in self.donnedArmor:
            if a.i_name.lower() == armornName.lower():
                self.donnedArmor.remove(a)
                return

    def calculateArmor(self):
        AC = 0
        for a in self.donnedArmor:
            AC += a.getArmorClass()
        return AC

    def addItem(self, itemName, qty):
        item = Item.getItem(itemName)
        try:
            self.items[item.i_name] = (item, self.items[item.i_name][1] + qty)
        except KeyError:
            self.items[item.i_name] = (item, qty)
    
    def removeItem(self, itemName, qty)
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
            
