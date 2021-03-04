import discord
import random
from StuffsWeNeed import defaultstuff
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
      print ('Fun module is ready.')

    #hug
    @commands.command()
    async def hug(ctx, user: discord.User, *, Notes):
      hug_gifs = ['https://media1.tenor.com/images/626cb1e13142bce7f228ab8e30e2519c/tenor.gif?itemid=16896135', 'https://media1.tenor.com/images/6dd6ce8f5d0360dbc1653818109d5e4b/tenor.gif?itemid=12873207']
      em = discord.Embed(title = defaultstuff.texts()["hugEmbedTitle"], description=None)
      em.set_image(url=random.choice(hug_gifs))

      await ctx.send(embed=em)

# this is the end of the code, type all commands above this
def setup(client):
    client.add_cog(Fun(client))