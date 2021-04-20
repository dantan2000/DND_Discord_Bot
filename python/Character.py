import Inventory
import SpellSlots
import Types

def calculateMod(skillPoints):
    mod = (skillPoints - 10 + .5) // 2
    return int(mod)



class Alignment:
    def __init__(self, a_name, a_desc):
        self.a_name = a_name
        self.a_desc = a_desc

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
        AC = 10 + calculateMod(self.c_dex) + self.c_inv.calculateArmor()
        return AC

    # TODO: Prints the full character sheet
    def __str__(self):
        abilStr = ""
        for abil in self.c_abil:
            abilStr += f"   - {abil.a_name}\n"
        if len(abilStr) == 0:
            abilStr = "None"

        retStr = f"Name: {self.c_name}\nPlayer: {self.p_name}\nClass: {self.c_class}\n Level: {self.c_lvl}\n Race: {self.c_race}\nAlignment: {self.c_alignment}\n MaxHP: {self.c_maxHit} CurrHP: {self.c_currHit}\n STR: {self.c_str}\nDEX: {self.c_dex}\nCON: {self.c_con}\nINT: {self.c_int}\nWIS: {self.c_wis}\nCHA: {self.c_wis}\nAC: {self.getArmorClass()}\nInventory:\n{self.c_inv}\n\nFeatures & Traits:\n{abilStr}"
        # print(f"Character string: {retStr}")
        if not SpellSlots.emptySpellSlots(self.c_spellSlots):
            retStr += f"\nSpell Slots: {SpellSlots.dumpSpellSlots(self.c_spellSlots)}"
        return retStr

    def isComplete(self):
        return self.c_class is not None and self.c_lvl != 0 and self.c_race is not None and self.c_alignment is not None and self.c_str != 0 and self.c_dex != 0 and self.c_con != 0 and self.c_int != 0 and self.c_wis != 0 and self.c_cha != 0 and self.c_maxHit != 0 and len(self.c_abil) != 0 and len(self.c_prof != 0)


    def completeRequirements(self):
        listStr = "\n   -- "
        requirements = ""
        if self.c_class is None:
            requirements += listStr + "No Class"
        if self.c_lvl == 0:
            requirements += listStr + f"Cannot be level {self.c_lvl}"
        if self.c_race is None:
            requirements += listStr + "No Race"
        if self.c_alignment is None:
            requirements += listStr + "No Alignment"
        if self.c_str == 0:
            requirements += listStr + "No Strength Ability Score"
        if self.c_dex == 0:
            requirements += listStr + "No Dexterity Ability Score"
        if self.c_con == 0:
            requirements += listStr + "No Constitution Ability Score"
        if self.c_int == 0:
            requirements += listStr + "No Intelligence Ability Score"
        if self.c_wis == 0:
            requirements += listStr + "No Wisdom Ability Score"
        if self.c_cha == 0:
            requirements += listStr + "No Charisma Ability Score"
        if self.c_maxHit == 0:
            requirements += listStr + "No Maximum Hit Points"
        # TODO class proficiencies and race abilities enforcing
        if len(self.c_profs) == 0:
            requirements += listStr + "No Proficiencies"
        if len(self.c_abil) == 0:
            requirements += listStr + "No Abilities"
        return requirements


    def improveAbility(self):
        # TODO: Prompt and get which ability to improve with discord commands
        self.c_str += 1

    def selectSkills(self, skills):
        numSkills = skills[0]
        skillList = skills[1]
        # TODO: Prompt and get which skills to select

    def addAbility(self, abil):
        self.c_abil.append(abil)

    def isProficient(self, profName):
        for prof in self.c_profs:
            if prof.p_name.lower() == profName.lower():
                return True
        return False

    def getMod(self, abilityName):
        score = 10
        if abilityName == Types.STR:
            score = self.c_str
        if abilityName == Types.DEX:
            score = self.c_dex
        if abilityName == Types.CON:
            score = self.c_con
        if abilityName == Types.INT:
            score = self.c_int
        if abilityName == Types.WIS:
            score = self.c_wis
        if abilityName == Types.CHA:
            score = self.c_cha

        return calculateMod(score)

    def castSpell(self, spellLevel):
        try:
            spellLevel = int(spellLevel)
        except:
            raise ValueError("Spell level must be an Integer.")

        if spellLevel < 1 or spellLevel > 20:
            raise ValueError("Spell level must be between 1 and 20")
        if self.c_spellSlots[spellLevel] == 0:
            raise ValueError(f"Out of level {spellLevel} spells!")

        self.c_spellSlots[spellLevel] -= 1



    