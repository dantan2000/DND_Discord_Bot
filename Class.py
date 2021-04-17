import Types.py
import Skill.py
import Character.py
import LevelUp.py

class Class:

    def __init__(hitDie, proficiencies, skills, levelUpTable):
        self.hitDie = hitDie
        self.proficiencies = proficiencies
        self.skills = skills
        self.levelUpTable = levelUpTable

    def levelUp(self, character):
        if character.c_lvl == 0:
            character.selectSkills(self.skills)
        levelUpRow = self.levelUpTable[character.c_lvl]
        levelUpRow.levelUp(character)

        
        

class Fighter(Class):
    hitDie = 10
    Proficiencies = [Types.ARMOR, Types.SHIELD, Types.SIMPLE_WEAPON, Types.MARTIAL_WEAPON, Types.STR, Types.CON]
    Skills = (2, [Skill.s_acrobatics, Skill.s_animalHandling, Skill.s_athletics, Skill.s_history, Skill.s_insight, Skill.s_intimidation, Skill.s_perception, Skill.s_survival])

    def levelUp(self, character):
        levelUpStats = getLevelUpStats(TYPES.FIGHTER, character.c_lvl + 1)