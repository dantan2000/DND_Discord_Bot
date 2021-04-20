import SpellSlots
import copy

class LevelUpRow:

    def __init__(self, profBonus, features, spellSlots = SpellSlots.makeSpellSlots()):
        self.profBonus = profBonus
        self.spellSlots = spellSlots
        self.features = features

    # def levelUp(self, character):
    #     character.c_profBonus = self.profBonus
    #     character.c_spellSlots = copy.copy(self.spellSlots)
    #     for feat in features:
    #         applyFeature(character)

    def getSpellSlots(self):
        return copy.copy(self.spellSlots)
    
fighterLevelUpTable = {
    1: LevelUpRow(2, [])
}