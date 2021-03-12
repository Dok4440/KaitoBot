import discord
import os
import logging
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
logging.basicConfig(level=logging.INFO)


client = commands.Bot(command_prefix="b,", intents=intents)

client.remove_command("help")

# kanker yes kkr sletje kkr sletje yes :3 <3
# willem if ur reading this, they let me code in school omgogmmogmogmogmogmomgomogmogmog
# at it again, coding in skewl. ily btw
# abcdefghijklmnopqrstuvwxyz im so BORED WILLEM PLS


# event on_ready (bot runs)
@client.event
async def on_ready():
	print('Bot is online.')
	game = discord.Game(",help")
	await client.change_presence(status=discord.Status.online, activity=game)


# get all files from the "cogs" directory & load them in as commands
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('EPIK_BOT_TOKEN'))
# "if i delete this, the red line goes away" *deletes 2 lines of code* -dok
