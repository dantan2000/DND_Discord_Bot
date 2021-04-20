import Types
import Skill
import Character
import SpellSlots
import LevelUp

class Class:

    def __init__(self, className, hitDie, proficiencies, numSkills, skills, levelUpTable):
        self.className = className
        self.hitDie = hitDie
        self.proficiencies = proficiencies
        self.numSkills = numSkills
        self.skills = skills
        self.levelUpTable = levelUpTable

    def levelUp(self, character):
        if character.c_lvl == 0:
            character.selectSkills(self.skills)
        levelUpRow = self.levelUpTable[character.c_lvl]
        levelUpRow.levelUp(character)
        character.c_lvl += 1

    def getSpellSlots(self, level):
        if level < 1 or level > 21:
            return SpellSlots.makeSpellSlots()
        return self.levelUpTable[level - 1].spellSlots

    # TODO: find a good way to make class descriptions
    def __str__(self):
        return self.className

 
        

# class Fighter(Class):
#     hitDie = 10
#     Proficiencies = [Types.ARMOR, Types.SHIELD, Types.SIMPLE_WEAPON, Types.MARTIAL_WEAPON, Types.STR, Types.CON]
#     Skills = (2, [Skill.s_acrobatics, Skill.s_animalHandling, Skill.s_athletics, Skill.s_history, Skill.s_insight, Skill.s_intimidation, Skill.s_perception, Skill.s_survival])

#     def levelUp(self, character):
#         levelUpStats = getLevelUpStats(TYPES.FIGHTER, character.c_lvl + 1)