import config.py

def calculateMod(skillPoints):
    return (skillPoints - 10 + .5) // 2

class Character:

    def __init__(self, c_name, c_class, p_name, c_race, c_alignment, c_str, c_dex, c_con, c_int, c_wis, c_cha):
        self.c_name = c_name
        self.c_class = c_class
        self.c_lvl = 0
        self.p_name = p_name
        self.c_race = c_race
        self.c_alignment = c_alignment
        self.c_str = c_str
        self.c_dex = c_dex
        self.c_con = c_con
        self.c_int = c_int
        self.c_wis = c_wis
        self.c_cha = c_cha

        self.c_inv = Inventory(0, {})

        self.c_spellSlots = makeSpellSlots()

        self.c_abil = []
        self.c_profs = []
        self.c_profBonus = 0

        self.c_expectedCallback = None

    def getArmorClass(self):
        AC = 10 + calculateMod(self.c_dex)
        for a in self.c_armor:
            AC += a.getArmorClass()
        return AC


    def setStr(self, newStr):
        self.c_str = newStr
    
    def setDex(self, newDex):
        self.c_dex = newDex

    def setCon(self, newCon):
        self.c_con = newCon

    def setInt(self, newInt):
        self.c_int = newInt

    def setWis(self, newWis):
        self.c_wis = newWis
    
    def setCha(self, newCha):
        self.Cha = newCha

    def improveAbility(self):
        # TODO: Prompt and get which ability to improve with discord commands
        self.c_str += 1

    def selectSkills(self, skills)
        numSkills = skills[0]
        skillList = skills[1]
        # TODO: Prompt and get which skills to select

    def addAbility(self, abil):
        self.c_abil.append(abil)
