import config
import Inventory
import SpellSlots

def calculateMod(skillPoints):
    return (skillPoints - 10 + .5) // 2

class Character:

    def __init__(self, c_name, p_name, c_class = None, c_race = None, c_alignment = None, c_lvl = 0, c_str = 0, c_dex = 0, c_con = 0, c_int = 0, c_wis = 0, c_cha = 0, c_maxHit = 0, c_currHit = 0, c_inv = Inventory.Inventory(0, {}), c_spellSlots = SpellSlots.makeSpellSlots(), c_abil = [], c_profs = [], c_profBonus = 0):
        self.c_name = c_name
        self.p_name = p_name
        self.c_class = c_class
        self.c_lvl = c_lvl
        self.c_race = c_race
        self.c_alignment = c_alignment
        self.c_str = c_str
        self.c_dex = c_dex
        self.c_con = c_con
        self.c_int = c_int
        self.c_wis = c_wis
        self.c_cha = c_cha
        self.c_maxHit = c_maxHit
        self.c_currHit = c_currHit

        self.c_inv = c_inv

        self.c_spellSlots = c_spellSlots

        self.c_abil = c_abil
        self.c_profs = c_profs
        self.c_profBonus = c_profBonus


    def getArmorClass(self):
        AC = 10 + calculateMod(self.c_dex) + c_inv.calculateArmor()
        return AC

    # Prints the full character sheet
    def dump(self):
        return f"Name: {self.c_name}\nPlayer:{self.p_name}\nClass:  ** TODO **\nRace:{self.c_race}\nAlignment:{self.c_alignment}\nSTR: {self.c_str}\nDEX: {self.c_dex}\nCON: {self.c_con}\nINT: {self.c_int}\nWIS: {self.c_wis}\nCHA: {self.c_wis}\nAC: {self.getArmorClass}\nInventory: ** TODO **\nFeatures & Traits: ** TODO **"

    def isComplete(self):
        return self.c_class is not None and self.c_lvl != 0 and self.c_race is not None and self.c_alignment is not None and self.c_str != 0 and self.c_dex != 0 and self.c_con != 0 and self.c_int != 0 and self.c_wis != 0 and self.c_cha != 0 and self.c_maxHit != 0 and len(self.c_abil) != 0 and len(self.c_prof != 0)

    def improveAbility(self):
        # TODO: Prompt and get which ability to improve with discord commands
        self.c_str += 1

    def selectSkills(self, skills):
        numSkills = skills[0]
        skillList = skills[1]
        # TODO: Prompt and get which skills to select

    def addAbility(self, abil):
        self.c_abil.append(abil)
