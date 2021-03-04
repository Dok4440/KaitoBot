from discord.ext import commands

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


# this is the end of the code, type all mod commands above this
def setup(client):
    client.add_cog(Admin(client))

