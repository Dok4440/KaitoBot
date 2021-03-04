import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

class Miscellaneous(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
      print ('Miscellaneous module is ready.')

    # ping
    @commands.command()
    async def ping(self, ctx):
      await ctx.send(f"pong~! <a:bun:816363543174840320>・`{round(self.client.latency * 1000)}ms`")

    # invite
    @commands.command(aliases=['inv'])
    async def invite(self, ctx):
      await ctx.send("₊˚✦`☕`⊹﹕invite me to your server with this link: https://tinyurl.com/invitekaitobot !<a:KB_bunWhack:816632384342196254>")

     # open source
    @commands.command(aliases=['code', 'source'])
    async def opensource(self, ctx):
      await ctx.send("₊˚✦`☕`⊹﹕access my open-source code on Flo's repl.it profile!: https://repl.it/@flo0003")
    
    # avatar
    @commands.command(aliases=['av', 'pfp', 'profilepic', 'profilepicture'])
    @commands.guild_only() # only able to do this command in a server (not in DM)
    async def avatar(self, ctx, *, user: discord.Member = None):
        user = user or ctx.author
        # size = size or 1024 # gotta figure this out later
        size = 1024
        await ctx.send(f"₊˚✦`☕`⊹﹕{user.name}'s avatar・꒷꒦\n{user.avatar_url_as(size=size)}")
		
    # say
    @commands.command(aliases=['repeat', 'speak'])
    async def say(self, ctx, *, msg="₊˚✦`☕`⊹﹕please provide text for me to say!・꒷꒦"):
        await ctx.send(msg)
        await ctx.delete(ctx.message)
		
    #welcome msg
    @commands.Cog.listener()
    async def on_member_join(self, member):
      guild = self.client.get_guild(816336230081888266)
      channel = guild.get_channel(816336230081888269)
      await channel.send(f'test')

# this is the end of the code, type all mod commands above this
def setup(client):
    client.add_cog(Miscellaneous(client))