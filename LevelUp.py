import Character.py
class LevelUpRow:

    def __init__(self, profBonus, features, spellSlots = makeSpellSlots())
        self.profBonus = profBonus
        self.spellSlots = spellSlots
        self.features = features

    def levelUp(self, character):
        character.c_profBonus = self.profBonus
        character.c_spellSlots = self.spellSlots
        for feat in features:
            applyFeature(character)
    
fighterLevelUpTable = {
    1: LevelUpRow(2, [])
}