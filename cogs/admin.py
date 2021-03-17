from discord.ext import commands
import pymongo
from pymongo import MongoClient
import os

dbclient = MongoClient(os.getenv('RANDOM_FUCKING_STRING_ISTFG_IDC'))
db = dbclient["KaitoBot"]

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
      print ('Admin module is ready.')

    # enable module
    @commands.command()
    @commands.is_owner()
    async def enableModule(self, ctx, extension):
      commands.load_extension(f'cogs.{extension}')
      await ctx.send('The module was enabled / reloaded.')

    # disable module
    @commands.command()
    @commands.is_owner()
    async def disableModule(self, ctx, extension):
      commands.unload_extension(f'cogs.{extension}')
      await ctx.send('The module was disabled.')

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def prefix(self, ctx, *, message):
      collection = db["Prefix"]

      post = {"server_id": ctx.message.guild.id, "prefix": message}

      collection.delete_many({"server_id": ctx.message.guild.id})
      collection.insert_one(post)

      await ctx.send("Prefix has been set.")

# this is the end of the code, type all mod commands above this
def setup(client):
    client.add_cog(Admin(client))

