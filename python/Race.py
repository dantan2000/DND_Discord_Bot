import Types

class Race:
    
    # @abstractmethod
    def getName():
        pass

    # @abstractmethod
    def getSize():
        pass

    # @abstractmethod
    def getSpeed():
        pass

    # @abstractmethod
    def getAbilityScoreMods():
        pass

    # @abstractmethod
    def getProficiencies():
        pass

    # @abstractmethod
    def getLanguages():
        pass

    # @abstractmethod
    def getTraits():
        pass


class Human(Race):

    def getName():
        return Types.HUMAN

    def getSize():
        return Types.MED

    def getSpeed():
        return 30

    def getAbilityScoreMods():
        mods = {
            Types.STR: 1,
            Types.DEX: 1,
            Types.CON: 1,
            Types.INT: 1,
            Types.WIS: 1,
            Types.CHA: 1
        }
        return mods

    def getProficiencies():
        return []

    def getLanguages():
        return [Types.CMN]

    def getTraits():
        return []