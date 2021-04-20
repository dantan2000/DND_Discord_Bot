import config
import discord
import random
import sys
import Types
import Character
import DiceRoll
import Inventory
import Item
import LevelUp
import Race
import Skill
import Spell
import SpellSlots
import DB
from discord.ext import commands

SETSTR = "$setStr"
SETDEX = "$setDex"
SETCON = "$setCon"
SETINT = "$setInt"
SETWIS = "$setWis"
SETCHA = "$setCha"

player_character = {}
player_callback = {}

client = commands.Bot(command_prefix = "$")

def makeSetAbilityScoreMsg(cmd, abilityType):
    return f"Use command {cmd} [Score] to set the ability score for {abilityType}"

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def roll(ctx, *args):
    global player_character

    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        rollerName = openedCharacter.c_name
    except KeyError:
        rollerName = str(currPlayer).split('#')[0]

    try:
        # Assuming the format is in 1d20 + 2 format, combine string and remove spaces
        rollStr = ""
        for arg in args:
            rollStr += arg
        
        # Remove "+" modifier, if exists
        rollStr = rollStr.split("+")
        if len(rollStr) == 2:
            mod = [int(rollStr[1])]
        elif len(rollStr) == 1:
            mod = [0]
        else:
            raise ValueError("Invalid roll format. Expected \"+ INT\" modifier")

        # Seperate numRolls and numSides from "1d20"
        rollStr = rollStr[0].split("d")
        if len(rollStr) != 2:
            raise ValueError("Invalid roll format. Expected \"INTdINT\" syntax")
        numRolls = int(rollStr[0])
        numSides = int(rollStr[1])
        if numSides < 0:
            raise ValueError("Dice cannot have less than one side")
        roll = DiceRoll.DiceRoll(numRolls, numSides, mod)
        rolls = roll.roll()
        rollMsg = ""
        if len(rolls) > 1:
            sum = 0
            for r in rolls:
                sum += r
                rollMsg += f"{r} + "
            rollMsg = rollMsg[:len(rollMsg) - 2]
            rollMsg = f"{sum}\n    -- {rollMsg}"
        elif len(rolls) == 1:
            rollMsg = str(rolls[0])
        else:
            rollMsg = f"{sum}\n   -- Did not roll any dice."
        
        await ctx.send(f"{rollerName} rolled {roll.toString()}: {rollMsg}")
        return
    except:
        print("Error:", sys.exc_info()[0], " ", str(sys.exc_info()[0]))


    # Else, see if trying to roll for a skill check on an open character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
    except KeyError:
        await noOpenCharacter(ctx, "$roll", currPlayer)
        return

    try: 
        # Create skill name from arguments
        skill = ""
        for arg in args:
            skill += arg + " "
        # Trim trailing space
        if len(skill) > 0:
            skill = skill[:len(skill) - 1]
        
        skill = DB.getSkillCheck(skill)

        # Add ability mod and proficiency mod (if applicable)
        mods = []
        
        abilityMod = openedCharacter.getMod(skill.s_type)
        if abilityMod != 0:
            mods.append(abilityMod)

        
        if openedCharacter.isProficient(skill.s_name):
            mods.append(openedCharacter.c_profBonus)

        # Make and roll dice
        roll = DiceRoll.DiceRoll(1, 20, mods)

        rolls = roll.roll()

        # Make message for user
        rollMsg = ""
        if len(rolls) > 1:
            sum = 0
            for r in rolls:
                sum += r
                rollMsg += f"{r} + "
            rollMsg = rollMsg[:len(rollMsg) - 2]
            rollMsg = f"{sum}\n    -- {rollMsg}"
        elif len(rolls) == 1:
            rollMsg = str(rolls[0])
        else:
            rollMsg = f"{sum}\n   -- Did not roll any dice."
        

        await ctx.send(f"{rollerName} rolled for {skill.s_type}: {rollMsg}")
    except KeyError as e:
        await ctx.send(f"Error: {e}")
    except ValueError:
        await ctx.send(f"Usage: $roll [numRolls d numSides <+ mod> | savingThrowName | skillCheckName]")

# Invalid callback, used for multi step functions
async def unexpectedCallback(ctx, cmd, currPlayer):
    await ctx.send(f"Unexpected command: {cmd}\n\n  ++ {player_callback[currPlayer][1]}")

# Used when a player tries to modify a character without having one open
async def noOpenCharacter(ctx, cmd, currPlayer):
    await ctx.send(f"Error {cmd}: No character opened for {str(currPlayer).split('#')[0]}")

# Given a list of words, combine them into a single string with each word seperated by spaces with no trailing spaces.
def makeInputString(args):
    input = ""
    for arg in args:
        input += arg + " "
    if len(input) > 0:
        input = input [:len(input) - 1]
    return input


@client.command()
async def open(ctx, *args):
    global player_character
    currPlayer = ctx.author
    characterName = makeInputString(args)
    # Check if player already has a character open
    try:
        currCharacter = player_character[currPlayer]
        await ctx.send(f"Error: Could not open {characterName}; you already have {currCharacter.c_name} open! Please close this character before opening a new one.")
        return
    except:
        pass

    try:
        newCharacter = DB.openCharacter(characterName)
        player_character[currPlayer] = newCharacter
        await ctx.send(f"{currPlayer} is now playing as {newCharacter.c_name}!")
    except Exception as e:
        await ctx.send(f"Error: {e}")


@client.command()
async def close(ctx, *args):
    global player_character
    currPlayer = ctx.author
    save = makeInputString(args)
    # Check if player already has a character open
    try:
        currCharacter = player_character[currPlayer]
    except:
        await noOpenCharacter(ctx, "$close", currPlayer)
        return

    try: 
        # Save if the save flag was set to "true"
        saveMsg = ""
        if save.lower() == "true":
            DB.saveCharacter(currCharacter)
            saveMsg = "saved and "
        elif save.lower() == "false":
            pass
        else:
            raise ValueError("Usage -- $close <True | False>")
        # Delete player -> character pair
        del player_character[currPlayer]
        await ctx.send(f"{currCharacter.c_name} has been {saveMsg}closed.")
    except ValueError as e:
        await ctx.send(f"Error: {e}")
        

@client.command()
async def save(ctx):
    global player_character
    currPlayer = ctx.author
    save = makeInputString(args)
    # Check if player already has a character open
    try:
        currCharacter = player_character[currPlayer]
    except:
        await noOpenCharacter(ctx, "$save", currPlayer)
        return

    try:
        DB.saveCharacter(currCharacter)
        await ctx.send(f"{currCharacter.c_name} has been saved!")
    except ValueError as e:
        await ctx.send(f"Error: {e}")


@client.command()
async def deleteCharacter(ctx, *args):
    global player_character
    currPlayer = ctx.author
    characterName = makeInputString(args)

    try:
        deletedCharacter = DB.openCharacter(characterName)
        DB.deleteCharacter(deleteCharacter.c_name)
        await ctx.send(f"{deleteCharacter.c_name} has been deleted.")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@client.command()
async def getInfo(ctx, *args):
    name = makeInputString(args)
    await ctx.send(DB.getInfo(name))

@client.command()
async def createCharacter(ctx, *args):
    global player_character, player_callback
    currPlayer = ctx.author

    name = ""
    for arg in args:
        name += arg + " "
    if len(name) > 0:
        name = name[:len(name) - 1]
    else:
        await ctx.send("Error: Must give a character name")
        return

    #checks if player has character opened
    try:
        openedCharacter = player_character[currPlayer]
        await ctx.send(f"Cannot create character; you already have {openedCharacter.c_name} open!")
        return
    except KeyError:
        pass

    try:
        DB.openCharacter(name)
        await ctx.send(f"Cannot create character {name}. A character with that name already exists!")
        return
    except KeyError:
        player_character[currPlayer] = Character.Character(name, currPlayer)
        await ctx.send(f"Creating character {name}. Begin customizing!")

@client.command()
async def setLevel(ctx, level):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        if int(level) < 1 or int(level) > 20 :
            raise ValueError
        openedCharacter.c_lvl = int(level)
        await ctx.send(f"Set {openedCharacter.c_name}'s Level to {level}")
    except KeyError:
        noOpenCharacter(ctx, "$setLevel", currPlayer)
    except ValueError:
        await ctx.send(f"Error: Level Score must be an Integer between 1 and 20.")

@client.command()
async def setStr(ctx, score):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        if int(score) < 1 or int(score) > 20 :
            raise ValueError
        openedCharacter.c_str = int(score)
        await ctx.send(f"Set {openedCharacter.c_name}'s Strength to {score}")
    except KeyError:
        noOpenCharacter(ctx, "$setStr", currPlayer)
    except ValueError:
        await ctx.send(f"Error: Ability Score must be an Integer between 1 and 20.")

@client.command()
async def setDex(ctx, score):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        if int(score) < 1 or int(score) > 20 :
            raise ValueError
        openedCharacter.c_dex = int(score)
        await ctx.send(f"Set {openedCharacter.c_name}'s Dexterity to {score}")
    except KeyError:
        noOpenCharacter(ctx, "$setDex", currPlayer)
    except ValueError:
        await ctx.send(f"Error: Ability Score must be an Integer between 1 and 20.")

@client.command()
async def setCon(ctx, score):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        if int(score) < 1 or int(score) > 20 :
            raise ValueError
        openedCharacter.c_con = int(score)
        await ctx.send(f"Set {openedCharacter.c_name}'s Constitution to {score}")
    except KeyError:
        noOpenCharacter(ctx, "$setCon", currPlayer)
    except ValueError:
        await ctx.send(f"Error: Ability Score must be an Integer between 1 and 20.")

@client.command()
async def setInt(ctx, score):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        if int(score) < 1 or int(score) > 20 :
            raise ValueError
        openedCharacter.c_int = int(score)
        await ctx.send(f"Set {openedCharacter.c_name}'s Intelligence to {score}")
    except KeyError:
        noOpenCharacter(ctx, "$setInt", currPlayer)
    except ValueError:
        await ctx.send(f"Error: Ability Score must be an Integer between 1 and 20.")

@client.command()
async def setWis(ctx, score):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        if int(score) < 1 or int(score) > 20 :
            raise ValueError
        openedCharacter.c_wis = int(score)
        await ctx.send(f"Set {openedCharacter.c_name}'s Wisdom to {score}")
    except KeyError:
        noOpenCharacter(ctx, "$setWis", currPlayer)
    except ValueError:
        await ctx.send(f"Error: Ability Score must be an Integer between 1 and 20.")

@client.command()
async def setCha(ctx, score):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        if int(score) < 1 or int(score) > 20 :
            raise ValueError
        openedCharacter.c_cha = int(score)
        await ctx.send(f"Set {openedCharacter.c_name}'s Charisma to {score}")
    except KeyError:
        noOpenCharacter(ctx, "$setCha", currPlayer)
    except ValueError:
        await ctx.send(f"Error: Ability Score must be an Integer between 1 and 20.")


@client.command()
async def setMaxHP(ctx, hp):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        if int(hp) < 0 :
            raise ValueError
        openedCharacter.c_maxHit = int(hp)
        openedCharacter.c_currHit = openedCharacter.c_maxHit
        await ctx.send(f"Set {openedCharacter.c_name}'s Maximum Hit Points to {hp}")
    except KeyError:
        noOpenCharacter(ctx, "$setMaxHP", currPlayer)
    except ValueError:
        await ctx.send(f"Error: HP must be an Integer greater than 0.")


@client.command()
async def setProfBonus(ctx, bonus):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        openedCharacter.c_profBonus = int(bonus)
        await ctx.send(f"Set {openedCharacter.c_name}'s Proficiency Bonus to {bonus}")
    except KeyError:
        noOpenCharacter(ctx, "$setProfBonus", currPlayer)
    except ValueError:
        await ctx.send(f"Error: Proficiency Bonus must be an Integer.")

@client.command()
async def setAlignment(ctx, align):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
    except KeyError:
        await noOpenCharacter(ctx, "$setAlignment", currPlayer)
        return
    try:
        align = DB.getAlignment(align)
        if openedCharacter.c_alignment is None:
            openedCharacter.c_alignment = align.a_name
            await ctx.send(f"{openedCharacter.c_name} has Alignment {align.a_name}")
        else:
            await ctx.send(f"{openedCharacter.c_name} alrady has Alignment {openedChacarter.c_alignment}")
    except KeyError:
        await ctx.send(f"Cannot find Alignment: {align}")

        
@client.command()
async def setRace(ctx, race):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
    except KeyError:
        await noOpenCharacter(ctx, "$setRace", currPlayer)
        return
    try:
        race = DB.getRace(race)
        if openedCharacter.c_race is None:
            openedCharacter.c_race = race.r_name
            await ctx.send(f"{openedCharacter.c_name} is a {race.r_name}")
        else:
            await ctx.send(f"{openedCharacter.c_name} is already a {openedChacarter.c_race}")
    except KeyError:
        await ctx.send(f"Cannot find Race: {race}")

        
@client.command()
async def setClass(ctx, className):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
    except KeyError:
        await noOpenCharacter(ctx, "$setClass", currPlayer)
        return
    try:
        newClass = DB.getClass(className)
        if openedCharacter.c_class is None:
            openedCharacter.c_class = newClass.className
            await ctx.send(f"{openedCharacter.c_name} is a {newClass.className}")
        else:
            await ctx.send(f"{openedCharacter.c_name} is already a {openedChacarter.c_class}")
    except KeyError:
        await ctx.send(f"Cannot find Class: {className}")


@client.command()
async def addMaxHP(ctx, hp):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        openedCharacter.c_maxHit += int(hp)
        openedCharacter.c_currHit = openedCharacter.c_maxHit
        await ctx.send(f"Set {openedCharacter.c_name}'s Maximum Hit Points to {openedChacarter.c_maxHit}")
    except KeyError:
        noOpenCharacter(ctx, "$addMaxHP", currPlayer)
    except ValueError:
        await ctx.send(f"Error: HP must be an Integer.")

@client.command(aliases = ('addAbility', 'addFeature'))
async def addAbilityFeature(ctx, abil):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
    except KeyError:
        noOpenCharacter(ctx, "$addAbility, $addFeature", currPlayer)
        return
    try:
        newAbil = DB.getAbility(abil)
        if newAbil not in openedCharacter.c_abil:
            openedCharacter.c_abil.append(newAbil)
    except KeyError:
        await ctx.send(f"Cannot find Feature/Ability: {feat}")

@client.command()
async def addProficiency(ctx, prof):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
    except KeyError:
        noOpenCharacter(ctx, "$addProficiency", currPlayer)
        return
    try:
        newProf = DB.getProficiency(prof)
        if newProf not in openedCharacter.c_profs:
            openedCharacter.c_profs.append(newProf)
            await ctx.send(f"{openedCharacter.c_name} is now proficient in {newProf.p_name}!")
        else:
            await ctx.send(f"{openedCharacter.c_name} is already proficient in {newProf.p_name}")
    except KeyError:
        await ctx.send(f"Cannot find Proficiency: {prof}")


@client.command()
async def takeDmg(ctx, hp):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        openedCharacter.c_currHit -= int(hp)
        await ctx.send(f"{openedCharacter.c_name} took {hp} damage!\n    Current HP: {openedCharacter.c_currHit}")
    except KeyError:
        noOpenCharacter(ctx, "$takeDmg", currPlayer)
    except ValueError:
        await ctx.send(f"Error: HP must be an Integer.")


@client.command()
async def heal(ctx, hp):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        openedCharacter.c_currHit += int(hp)
        await ctx.send(f"{openedCharacter.c_name} healed for {hp} HP!\n    Current HP: {openedCharacter.c_currHit}")
    except KeyError:
        noOpenCharacter(ctx, "$heal", currPlayer)
    except ValueError:
        await ctx.send(f"Error: HP must be an Integer.")


@client.command()
async def addItem(ctx, *args):
    currPlayer = ctx.author
    # Check if the player has a character opened
    try:
        openedCharacter = player_character[currPlayer]
        # Check if there are arguments
        if len(args) == 0:
            await ctx.send("Usage: $addItem <itemName> [qty = 1]")
            return
    except KeyError:
        noOpenCharacter(ctx, "$addItem", currPlayer)

    # Check if the last argument is a quantity (int)
    try:
        qty = int(args[len(args) - 1])
        args = args[:len(args) - 1]
    except ValueError:
        qty = 1

    # Make item name string
    itemName = ""
    for word in args:
        itemName += word + " "
    # Trim trailing space
    if len(itemName) > 0:
        itemName = itemName[:len(itemName) - 1]

    try:
        item = DB.getItem(itemName)
        openedCharacter.c_inv.addItem(item, qty)
        await ctx.send(f"{openedCharacter.c_name} received a {item.i_name}!")
    except KeyError:
        await ctx.send(f"Error: cannot find item: \"{itemName}\"")
    
@client.command()
async def removeItem(ctx, *args):
    currPlayer = ctx.author
    # Check if the player has a character opened
    try:
        openedCharacter = player_character[currPlayer]
        # Check if there are arguments
        if len(args) == 0:
            await ctx.send("Usage: $addItem <itemName> [qty = 1]")
            return
    except KeyError:
        noOpenCharacter(ctx, "$addItem", currPlayer)

    # Check if the last argument is a quantity (int)
    try:
        qty = int(args[len(args) - 1])
        args = args[:len(args) - 1]
    except ValueError:
        qty = 1

    # Make item name string
    itemName = ""
    for word in args:
        itemName += word + " "
    # Trim trailing space
    if len(itemName) > 0:
        itemName = itemName[:len(itemName) - 1]

    try:
        openedCharacter.c_inv.removeItem(itemName, qty)
    except (KeyError, ValueError) as e:
        await ctx.send(f"Error: {e}")


@client.command()
async def addGold(ctx, qty):
    currPlayer = ctx.author
    # Check if the player has a character opened
    try:
        openedCharacter = player_character[currPlayer]
    except KeyError:
        noOpenCharacter(ctx, "$addGold", currPlayer)
    
    try:
        qty = int(qty)
    except ValueError:
        await ctx.send(f"Error: Quantity must be an Integer.")
        return

    try:
        openedCharacter.c_inv.addGold(qty)
        await ctx.send(f"{openedCharacter.c_name} got {qty} gold!\n  - New balance: {openedCharacter.c_inv.gold} gp")
    except TypeError:
        await ctx.send("Usage: $addGold <qty>")
    except ValueError as e:
        await ctx.send(f"Error: {e}")
    
    
@client.command()
async def removeGold(ctx, qty):
    currPlayer = ctx.author
    # Check if the player has a character opened
    try:
        openedCharacter = player_character[currPlayer]
    except KeyError:
        noOpenCharacter(ctx, "$removeGold", currPlayer)
    
    try:
        qty = int(qty)
    except ValueError:
        await ctx.send(f"Error: Quantity must be an Integer.")

    try:
        openedCharacter.c_inv.removeGold(qty)
        await ctx.send(f"{openedCharacter.c_name} removed {qty} gold.\n  - New balance: {openedCharacter.c_inv.gold} gp")
    except TypeError:
        await ctx.send("Usage: $removeGold <qty>")
    except ValueError as e:
        await ctx.send(f"Error: {e}")


@client.command()
async def don(ctx, *args):
    currPlayer = ctx.author
    # Check if the player has a character opened
    try:
        openedCharacter = player_character[currPlayer]
        # Check if there are arguments
        if len(args) == 0:
            await ctx.send("Usage: $donArmor <armorName>")
            return
    except KeyError:
        noOpenCharacter(ctx, "$donArmor", currPlayer)

    # Make armor name string
    armorName = ""
    for word in args:
        armorName += word + " "
    # Trim trailing space
    if len(armorName) > 0:
        armorName = armorName[:len(armorName) - 1]

    try:
        openedCharacter.c_inv.donArmor(armorName)
    except ValueError as e:
        await ctx.send(f"Error: {e}")


@client.command()
async def doff(ctx, *args):
    currPlayer = ctx.author
    # Check if the player has a character opened
    try:
        openedCharacter = player_character[currPlayer]
        # Check if there are arguments
        if len(args) == 0:
            await ctx.send("Usage: $donArmor <armorName>")
            return
    except KeyError:
        noOpenCharacter(ctx, "$donArmor", currPlayer)

    # Make armor name string
    armorName = ""
    for word in args:
        armorName += word + " "
    # Trim trailing space
    if len(armorName) > 0:
        armorName = armorName[:len(armorName) - 1]

    try:
        openedCharacter.c_inv.doffArmor(armorName)
    except ValueError as e:
        await ctx.send(f"Error: {e}")

@client.command()
async def isComplete(ctx):
    currPlayer = ctx.author
    # Check if the player has a character opened
    try:
        openedCharacter = player_character[currPlayer]
        if openedCharacter.isComplete():
            await ctx.send(f"{openedCharacter.c_name} is complete!")
        else:
            await ctx.send(f"{openedCharacter.c_name} is not complete. Current Issues: {openedCharacter.completeRequirements()}")
    except KeyError:
        noOpenCharacter(ctx, "$isComplete", currPlayer)

@client.command()
async def dumpCharacter(ctx):
    currPlayer = ctx.author
    # Check if the player has a character opened
    try:
        openedCharacter = player_character[currPlayer]
        await ctx.send(f"Character sheet: \n{openedCharacter}")
    except KeyError:
        noOpenCharacter(ctx, "$dumpCharacter", currPlayer)


@client.command()
async def castSpell(ctx, spellLevel):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        openedCharacter.castSpell(spellLevel)
        await ctx.send(f"{openedCharacter.c_name} cast a level {spellLevel} spell!\n    Remaining level {spellLevel} slots: {openedCharacter.c_spellSlots[int(spellLevel)]}")
    except KeyError:
        await noOpenCharacter(ctx, "$castSpell", currPlayer)
    except ValueError as e:
        await ctx.send(f"Error: {e}")


@client.command()
async def longRest(ctx):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        openedCharacter.c_currHit = openedCharacter.c_maxHit
        openedCharacter.spellSlots = openedCharacter.c_class.getSpellSlots(openedCharacter.c_lvl)
        await ctx.send(f"{openedChacarter.c_name} took a long rest. Healed to full and restored any spell slots!")
    except KeyError:
        await noOpenCharacter(ctx, "$longRest", currPlayer)
    except ValueError as e:
        await ctx.send(f"Error: {e}")


@client.command()
async def shortRest(ctx):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        await ctx.send(f"{openedChacarter.c_name} took a short rest. You may spend available hit die to heal for Hit Die + CON modifier")
    except KeyError:
        await noOpenCharacter(ctx, "$shortRest", currPlayer)
    except ValueError as e:
        await ctx.send(f"Error: {e}")

client.run(config.botToken)