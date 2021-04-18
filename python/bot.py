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
async def roll(ctx, numRolls = "1", numSides = "20", mod = "0"):
    try:
        numRolls = int(numRolls)
        numSides = int(numSides)
        mod = int(mod)
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
            rollMsg += f" = {sum}"
        elif len(rolls) == 1:
            rollMsg = str(rolls[0])
        else:
            rollMsg = "Did not roll any dice."
        
        await ctx.send(f"{ctx.author} rolled {roll.toString()}: {rollMsg}")
    except:
        print("Unexpected error:", sys.exc_info()[0], " ", sys.exc_info()[0].__str__())
        await ctx.send(f"Usage: $roll [Num Rolls] [Num Sides] [Mod] -- got {numRolls} {numSides} {mod}")

# Invalid callback, used for multi step functions
async def unexpectedCallback(ctx, cmd, currPlayer):
    await ctx.send(f"Unexpected command: {cmd}\n\n  ++ {player_callback[currPlayer][1]}")

# Used when a player tries to modify a character without having one open
async def noOpenCharacter(ctx, cmd, currPlayer):
    await ctx.send(f"Error {cmd}: No character opened for {currPlayer.split('#')[0]}")

@client.command()
async def createCharacter(ctx, name):
    global player_character, player_callback
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        await ctx.send(f"Cannot create character; you already have {openedCharacter.c_name} open!")
    except KeyError:
        setStrMsg = makeSetAbilityScoreMsg(SETSTR, Types.STR)
        player_character[currPlayer] = Character.Character(name, currPlayer)
        player_callback[currPlayer] = ("", "")
        await ctx.send(f"Creating character {name}. Begin customizing!")

@client.command()
async def setStr(ctx, score):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        openedCharacter.c_str = score
        await ctx.send(f"Set {openedCharacter.c_name}'s Strength to {score}")
    except KeyError:
        noOpenCharacter(ctx, "$setStr", currPlayer)

@client.command()
async def setDex(ctx, score):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        openedCharacter.c_dex = score
        await ctx.send(f"Set {openedCharacter.c_name}'s Dexterity to {score}")
    except KeyError:
        noOpenCharacter(ctx, "$setDex", currPlayer)

@client.command()
async def setCon(ctx, score):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        openedCharacter.c_con = score
        await ctx.send(f"Set {openedCharacter.c_name}'s Constitution to {score}")
    except KeyError:
        noOpenCharacter(ctx, "$setCon", currPlayer)

@client.command()
async def setInt(ctx, score):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        openedCharacter.c_int = score
        await ctx.send(f"Set {openedCharacter.c_name}'s Intelligence to {score}")
    except KeyError:
        noOpenCharacter(ctx, "$setInt", currPlayer)

@client.command()
async def setWis(ctx, score):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        openedCharacter.c_wis = score
        await ctx.send(f"Set {openedCharacter.c_name}'s Wisdom to {score}")
    except KeyError:
        noOpenCharacter(ctx, "$setWis", currPlayer)

@client.command()
async def setCha(ctx, score):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        openedCharacter.c_cha = score
        await ctx.send(f"Set {openedCharacter.c_name}'s Charisma to {score}")
    except KeyError:
        noOpenCharacter(ctx, "$setCha", currPlayer)


@client.command()
async def setMaxHP(ctx, hp):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        openedCharacter.c_maxHit = hp
        await ctx.send(f"Set {openedCharacter.c_name}'s Maximum Hit Points to {hp}")
    except KeyError:
        noOpenCharacter(ctx, "$setMaxHP", currPlayer)

@client.command()
async def addMaxHP(ctx, hp):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        openedCharacter.c_maxHit += hp
        await ctx.send(f"Set {openedCharacter.c_name}'s Maximum Hit Points to {openedChacarter.c_maxHit}")
    except KeyError:
        noOpenCharacter(ctx, "$addMaxHP", currPlayer)

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
        if newAbil not in openedCharacter.c_feat:
            openedCharacter.c_feat.append(newAbil)
    except KeyError:
        await ctx.send(f"Cannot find feature: {feat}")

@client.command()
async def addProficiency(ctx, abil):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
    except KeyError:
        noOpenCharacter(ctx, "$addProficiency", currPlayer)
        return
    try:
        newProf = DB.getProficiency(prof)
        if newProf not in openedCharacter.c_feat:
            openedCharacter.c_feat.append(newProf)
    except KeyError:
        await ctx.send(f"Cannot find Proficiency: {prof}")


@client.command()
async def takeDmg(ctx, hp):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        openedCharacter.c_currHit -= hp
        await ctx.send(f"{openedCharacter.c_name} took {hp} damage!\n    Current HP: {openedCharacter.c_currHit}")
    except KeyError:
        noOpenCharacter(ctx, "$takeDmg", currPlayer)


@client.command()
async def heal(ctx, hp):
    global player_character
    currPlayer = ctx.author
    try:
        openedCharacter = player_character[currPlayer]
        openedCharacter.c_currHit += hp
        await ctx.send(f"{openedCharacter.c_name} healed for {hp} HP!\n    Current HP: {openedCharacter.c_currHit}")
    except KeyError:
        noOpenCharacter(ctx, "$heal", currPlayer)


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
    itemName = itemName[:len(itemName) - 1]

client.run(config.botToken)