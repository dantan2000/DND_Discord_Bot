import Skill.py

skills = [
    Skill(Types.ACROBATICS, "Acrobatics checks.", Types.DEX),
    Skill(Types.ANIMAL_HANDLING, "Animal handling checks.", Types.WIS),
    Skill(Types.ARCANA, "Arcana checks.", Types.INT),
    Skill(Types.ATHLETICS, "Athletics checks." Types.STR),
    Skill(Types.DECEPTION, "Deception checks.", Types.CHA),
    Skill(Types.HISTORY, "History checks.", Types.INT),
    Skill(Types.INSIGHT, "Insight checks.", Types.WIS),
    Skill(Types.INTIMIDATION, "Intimidation checks.", Types.CHA),
    Skill(Types.INVESTIGATION, "Investigation checks.", Types.INT),
    Skill(Types.MEDICINE, "Medicine checks.", Types.WIS),
    Skill(Types.Nature, "Nature checks.", Types.INT),
    Skill(Types.PERCEPTION, "Perception checks.", Types.WIS),
    Skill(Types.PERFORMANCE, "Performance checks.", Types.CHA),
    Skill(Types.PERSUASION, "Persuasion checks.", Types.CHA),
    Skill(Types.RELIGION, "Religion checks.", Types.INT),
    Skill(Types.SLIGHT_OF_HAND, "Slight of Hand checks.", Types.DEX),
    Skill(Types.STEALTH, "Stealth checks.", Types.DEX),
    Skill(Types.SURVIVAL, "Survival checks.", Types.WIS)
]

# TODO: Get Skill Checks from Database
def getSkillCheck(skillName):
    for s in skills:
        if s.s_name.lower == skillName.lower():
            return s
    raise KeyError(f"Could not find skill {skill}")


abilities = [
    Ability("Fighting Style", "You adopt a particular style of fighting as your specialty. Choose one of the following options. You can’t take a Fighting Style option more than once, even if you later get to choose again."),
    Ability("Action Surge", "Starting at 2nd level, you can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action on top of your regular action and a possible bonus action. Once you use this feature, you must finish a short or long rest before you can use it again. Starting at 17th level, you can use it twice before a rest, but only once on the same turn."),
    Ability("Improved Critical", "Beginning when you choose this archetype at 3rd level, your weapon attacks score a critical hit on a roll of 19 or 20."),
    Ability("Remarkable Athlete", "Starting at 7th level, you can add half your proficiency bonus (round up) to any Strength, Dexterity, or Constitution check you make that doesn’t already use your proficiency bonus. In addition, when you make a running long jump, the distance you can cover increases by a number of feet equal to your Strength modifier."),
    Ability("Survivor", "At 18th level, you attain the pinnacle of resilience in battle. At the start of each of your turns, you regain hit points equal to 5 + your Constitution modifier if you have no more than half of your hit points left. You don’t gain this benefit if you have 0 hit points."),
    Ability("Ability Score Improvement", "When you reach 4th level, and again at 6th, 8th, 12th, 14th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.")
    Ability("Extra Attack", "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn. The number of attacks increases to three when you reach 11th level in this class and to four when you reach 20th level in this class"),
    Ability("Indomitable", "Beginning at 9th level, you can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can’t use this feature again until you finish a long rest. You can use this feature twice between long rests starting at 13th level and three times between long rests starting at 17th level."),
    Ability("Archery", "You gain a +2 bonus to attack rolls you make with ranged weapons"),
    Ability("Defense", "While you are wearing armor, you gain a +1 bonus to AC"),
    Ability("Dueling", "When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon."),
    Ability("Great Weapon Fighting", "When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit."),
    Ability("Protection", "When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield."),
    Ability("Two-Weapon Fighting"), "When you engage in two-weapon fighting, you can add your ability modifier.")
]

# TODO: get Abilities from DB
def getAbility(abilityName):
    for a in abilities:
        if a.a_name.lower() == abilityName.lower():
            return a
    raise KeyError(f"Cannot find ability with name {abilityName}")