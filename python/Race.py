import Types

class Race:
    
    def __init__(self, r_name, r_desc, r_size, r_speed, r_abilityMods, r_profs, r_languages, r_traits):
        self.r_name = r_name
        self.r_desc = r_desc
        self.r_size = r_size
        self.r_speed = r_speed
        self.r_abilityMods = r_abilityMods
        self.r_profs = r_profs
        self.r_languages = r_languages
        self.r_traits = r_traits

    def getInfo(self):
        ret = f"Race -- {self.r_name}"
        ret += f"Description: {self.r_desc}"
        ret += f"\nSize - {self.r_size}"
        ret += f"\nSpeed - {self.r_speed}"
        ret += f"\nAbility Modifiers: {self.r_abilityMods}"
        ret += f"\nProficiencies: {self.r_profs}"
        ret += f"\nLanguages: {self.r_languages}"
        ret += f"\nTraits: {self.r_traits}"
        return ret

    def __str__(self):
        return self.r_name