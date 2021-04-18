import Types

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

# Combined with Ability
# class Feature:
#     def __init__(self, f_name, f_desc):
#         self.f_name = f_name
#         self.f_desc = f_desc
    
#     def applyFeature(self, character):
#         if self.f_name.lower() == "Ability Score Improvement":
#             character.improveAbility()
#         else:
#             character.addAbility(self)

class Proficiency:
    def __init__(self, p_name, p_desc):
        self.p_name = p_name
        self.p_desc = p_desc
