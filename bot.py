import config
import discord
import random
from discord.ext import commands
import Types.py



client = commands.Bot(command_prefix = "$")

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def roll(ctx, numSides):
    try:
        numSides = int(numSides)
        if numSides < 0:
            raise ValueError("Dice cannot have less than one side")
        roll = random.randint(1, numSides)
        await ctx.send(f"Rolled a {roll}!")
    except:
        await ctx.send("Usage: $roll [Int]")

client.run(config.botToken)