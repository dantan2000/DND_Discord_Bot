import Types.py

class Skill:
    def __init__(self, s_name, s_desc, s_type):
        self.s_name = s_name
        self.s_desc = s_desc
        self.s_type = s_type

    def isType(self, t):
        return t == self.s_type

    
class Ability:
    def __init__(self, a_name, a_desc):
        self.a_name = a_name
        self.a_desc = a_desc

    def applyAbility(self, character):
        if self.a_name.lower() == "Ability Score Improvement":
            character.improveAbility()
        else:
            character.addAbility(self)