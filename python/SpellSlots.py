import Types


def makeSpellSlots(cantrips = 0, lvl1 = 0, lvl2 = 0, lvl3 = 0, lvl4 = 0, lvl5 = 0, lvl6 = 0, lvl7 = 0, lvl8 = 0, lvl9 = 0):
    return [cantrips, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, lvl7, lvl8, lvl9]

def useSpell(spellSlots, lvl):
    if lvl < len(spellSlots) and spellSlots[lvl] > 0:
        spellSlots[lvl] -= 1
    else:
        raise Exception(f"No spell slots for level: {lvl}.")

def emptySpellSlots(spellSlots):
    for slot in spellSlots:
        if slot > 0:
            return False
    return True