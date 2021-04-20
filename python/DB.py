import Skill
import Class
import LevelUp
import Types
import Item
import Character

skills = [
    Skill.Skill(Types.STR, "Proficiency for Strength Saving Throws.", Types.STR),
    Skill.Skill(Types.DEX, "Proficiency for Dexterity Saving Throws.", Types.DEX),
    Skill.Skill(Types.CON, "Proficiency for Constitution Saving Throws.", Types.CON),
    Skill.Skill(Types.INT, "Proficiency for Intelligence Saving Throws.", Types.INT),
    Skill.Skill(Types.WIS, "Proficiency for Wisdom Saving Throws.", Types.WIS),
    Skill.Skill(Types.CHA, "Proficiency for Charisma Saving Throws.", Types.CHA),
    Skill.Skill(Types.ACROBATICS, "Acrobatics checks.", Types.DEX),
    Skill.Skill(Types.ANIMAL_HANDLING, "Animal handling checks.", Types.WIS),
    Skill.Skill(Types.ARCANA, "Arcana checks.", Types.INT),
    Skill.Skill(Types.ATHLETICS, "Athletics checks.", Types.STR),
    Skill.Skill(Types.DECEPTION, "Deception checks.", Types.CHA),
    Skill.Skill(Types.HISTORY, "History checks.", Types.INT),
    Skill.Skill(Types.INSIGHT, "Insight checks.", Types.WIS),
    Skill.Skill(Types.INTIMIDATION, "Intimidation checks.", Types.CHA),
    Skill.Skill(Types.INVESTIGATION, "Investigation checks.", Types.INT),
    Skill.Skill(Types.MEDICINE, "Medicine checks.", Types.WIS),
    Skill.Skill(Types.NATURE, "Nature checks.", Types.INT),
    Skill.Skill(Types.PERCEPTION, "Perception checks.", Types.WIS),
    Skill.Skill(Types.PERFORMANCE, "Performance checks.", Types.CHA),
    Skill.Skill(Types.PERSUASION, "Persuasion checks.", Types.CHA),
    Skill.Skill(Types.RELIGION, "Religion checks.", Types.INT),
    Skill.Skill(Types.SLIGHT_OF_HAND, "Slight of Hand checks.", Types.DEX),
    Skill.Skill(Types.STEALTH, "Stealth checks.", Types.DEX),
    Skill.Skill(Types.SURVIVAL, "Survival checks.", Types.WIS)
]

# TODO: Get Skill Checks from Database
def getSkillCheck(skillName):
    for s in skills:
        # print(f"  --- comparing {skillName.lower()} to {s.s_name.lower()} ---\n       ++ {skillName.lower() == s.s_name.lower()}")
        if s.s_name.lower() == skillName.lower():
            return s
    raise KeyError(f"Could not find skill {skillName}")


abilities = [
    Skill.Ability("Fighting Style", "You adopt a particular style of fighting as your specialty. Choose one of the following options. You can’t take a Fighting Style option more than once, even if you later get to choose again."),
    Skill.Ability("Action Surge", "Starting at 2nd level, you can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action on top of your regular action and a possible bonus action. Once you use this feature, you must finish a short or long rest before you can use it again. Starting at 17th level, you can use it twice before a rest, but only once on the same turn."),
    Skill.Ability("Improved Critical", "Beginning when you choose this archetype at 3rd level, your weapon attacks score a critical hit on a roll of 19 or 20."),
    Skill.Ability("Remarkable Athlete", "Starting at 7th level, you can add half your proficiency bonus (round up) to any Strength, Dexterity, or Constitution check you make that doesn’t already use your proficiency bonus. In addition, when you make a running long jump, the distance you can cover increases by a number of feet equal to your Strength modifier."),
    Skill.Ability("Survivor", "At 18th level, you attain the pinnacle of resilience in battle. At the start of each of your turns, you regain hit points equal to 5 + your Constitution modifier if you have no more than half of your hit points left. You don’t gain this benefit if you have 0 hit points."),
    Skill.Ability("Ability Score Improvement", "When you reach 4th level, and again at 6th, 8th, 12th, 14th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."),
    Skill.Ability("Extra Attack", "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn. The number of attacks increases to three when you reach 11th level in this class and to four when you reach 20th level in this class"),
    Skill.Ability("Indomitable", "Beginning at 9th level, you can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can’t use this feature again until you finish a long rest. You can use this feature twice between long rests starting at 13th level and three times between long rests starting at 17th level."),
    Skill.Ability("Archery", "You gain a +2 bonus to attack rolls you make with ranged weapons"),
    Skill.Ability("Defense", "While you are wearing armor, you gain a +1 bonus to AC"),
    Skill.Ability("Dueling", "When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon."),
    Skill.Ability("Great Weapon Fighting", "When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit."),
    Skill.Ability("Protection", "When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield."),
    Skill.Ability("Two-Weapon Fighting", "When you engage in two-weapon fighting, you can add your ability modifier.")
]

# TODO: get Abilities from DB
def getAbility(abilityName):
    for a in abilities:
        if a.a_name.lower() == abilityName.lower():
            return a
    raise KeyError(f"Cannot find ability with name {abilityName}")


proficiencies = [
    Skill.Proficiency(Types.STR, "Proficiency for Strength Saving Throws."),
    Skill.Proficiency(Types.DEX, "Proficiency for Dexterity Saving Throws."),
    Skill.Proficiency(Types.CON, "Proficiency for Constitution Saving Throws."),
    Skill.Proficiency(Types.INT, "Proficiency for Intelligence Saving Throws."),
    Skill.Proficiency(Types.WIS, "Proficiency for Wisdom Saving Throws."),
    Skill.Proficiency(Types.CHA, "Proficiency for Charisma Saving Throws."),
    Skill.Proficiency(Types.ACROBATICS, "Proficiency for Acrobatics Skill Checks."),
    Skill.Proficiency(Types.ANIMAL_HANDLING, "Proficiency for Animal Handling Skill Checks."),
    Skill.Proficiency(Types.ARCANA, "Proficiency for Arcana Skill Checks."),
    Skill.Proficiency(Types.ATHLETICS, "Proficiency for Athletics Skill Checks."),
    Skill.Proficiency(Types.DECEPTION, "Proficiency for Deception Skill Checks."),
    Skill.Proficiency(Types.HISTORY, "Proficiency for History Skill Checks."),
    Skill.Proficiency(Types.INSIGHT, "Proficiency for Insight Skill Checks."),
    Skill.Proficiency(Types.INTIMIDATION, "Proficiency for Intimidation Skill Checks."),
    Skill.Proficiency(Types.INVESTIGATION, "Proficiency for Investigation Skill Checks."),
    Skill.Proficiency(Types.MEDICINE, "Proficiency for Medicine Skill Checks."),
    Skill.Proficiency(Types.NATURE, "Proficiency for Nature Skill Checks."),
    Skill.Proficiency(Types.PERCEPTION, "Proficiency for Perception Skill Checks."),
    Skill.Proficiency(Types.PERFORMANCE, "Proficiency for Performance Skill Checks."),
    Skill.Proficiency(Types.PERSUASION, "Proficiency for Persuasion Skill Checks."),
    Skill.Proficiency(Types.RELIGION, "Proficiency for Religion Skill Checks."),
    Skill.Proficiency(Types.SLIGHT_OF_HAND, "Proficiency for Slight of Hand Skill Checks."),
    Skill.Proficiency(Types.STEALTH, "Proficiency for Stealth Skill Checks."),
    Skill.Proficiency(Types.SURVIVAL, "Proficiency for Survival Skill Checks.")
]


# TODO: get Proficiencies from DB
def getProficiency(proficiency):
    for prof in proficiencies:
        if prof.p_name.lower() == proficiency.lower():
            return prof
    raise KeyError(f"Cannot find proficiency with name {proficiency}")

items = [
    Item.Weapon("Longsword", "Proficiency with a longsword allows you to add your proficiency bonus to the attack roll for any attack you make with it.", 15, [Types.MARTIAL_WEAPON, Types.MELEE_WEAPON], 1, 8),
    Item.Weapon("Longbow", "Proficiency with a longbow allows you to add your proficiency bonus to the attack roll for any attack you make with it.", 50, [Types.MARTIAL_WEAPON, Types.RANGED_WEAPON], 1, 8),
    Item.Armor("Leather Armor", "The Breastplate and shoulder protectors of this armor are made of leather that has been stiffened by being boiled in oil. The rest of the armor is made of softer and more flexible materials.", 10, [Types.ARMOR], 1),
    Item.Armor("Leather Armor", "Plate consists of shaped, interlocking metal plates to cover the entire body. A suit of plate includes gauntlets, heavy leather boots, a visored helmet, and thick layers of padding underneath the armor. Buckles and straps distribute the weight over the body.", 1500, [Types.ARMOR], 8),
    Item.Armor("Shield", "A shield is made from wood or metal and is carried in one hand. Wielding a shield increases your Armor Class by 2. You can benefit from only one shield at a time.", 10, [Types.SHIELD], 2)
]

# TODO: Get items from DB
def getItem(itemName):
    for i in items:
        if i.i_name.lower() == itemName.lower():
            return i
    raise KeyError(f"No item of name {itemName}")

fighterProf = [Types.ARMOR, Types.SHIELD, Types.SIMPLE_WEAPON, Types.MARTIAL_WEAPON, Types.STR, Types.CON]
fighterSkill = [Types.ACROBATICS, Types.ANIMAL_HANDLING, Types.ATHLETICS, Types.HISTORY, Types.INSIGHT, Types.INTIMIDATION, Types.PERCEPTION, Types.SURVIVAL]
fighterLevelUp = []

classes = [
    Class.Class("Fighter", 10, fighterProf, 2, fighterSkill, fighterLevelUp)
]

# TODO: Get classes from DB
def getClass(className):
    raise KeyError(f"No Class of name {className}")


# TODO: Get races from DB
def getRace(raceName):
    raise KeyError(f"No Race of name {raceName}")


alignments = [
    Character.Alignment("Lawful Good", "No Description."),
    Character.Alignment("Neutral Good", "No Description."),
    Character.Alignment("Chaotic Good", "No Description."),
    Character.Alignment("Lawful Neutral", "No Description."),
    Character.Alignment("True Neutral", "No Description."),
    Character.Alignment("Chaotic Neutral", "No Description."),
    Character.Alignment("Lawful Evil", "No Description."),
    Character.Alignment("Neutral Evil", "No Description."),
    Character.Alignment("Chaotic Evil", "No Description.")
]


# TODO: Get alignments from DB
def getAlignment(alignmentName):
    for a in alignments:
        if alignmentName.lower() == a.a_name.lower():
            return a
    raise KeyError(f"No Alignment of name {alignmentName}")