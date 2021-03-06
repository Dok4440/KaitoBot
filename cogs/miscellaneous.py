import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import os

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

dbclient = MongoClient(os.getenv('RANDOM_FUCKING_STRING_ISTFG_IDC'))
db = dbclient["KaitoBot"]

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
      em = discord.Embed(description = "₊˚✦`☕`⊹﹕[invite me to your server](https://tinyurl.com/kaitobot) <a:KB_bunWhack:816632384342196254>", color = 0xe4d3b3)

      await ctx.send(embed = em)

    @commands.command(aliases=['docs'])
    async def readme(self, ctx):
        em = discord.Embed(title = "Documentation", description = "GitHub Repository: https://github.com/Dok4440/KaitoBot\nCommands list: https://github.com/Dok4440/KaitoBot/wiki/Command-List", color = 0xe4d3b3)

        await ctx.send(embed = em)

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
        await ctx.message.delete()
		
    # server count command
    @commands.command()
    async def stats(self, ctx):
        em = discord.Embed(color = 0xe4d3b3)
        em.set_author(name="﹕☕・SheepieBot v1.00.0・✦", icon_url = "https://cdn.discordapp.com/avatars/817075893099823166/622e3a17df78f6faa775d460359cb3e1.webp?size=1024")
        em.add_field(name="୨୧・authors", value="✦ー`Dok4440`\n✦ー`Flo0003`")
        # em.add_field(name="Uptime", value=f"{self.client.uptime}", inline=False)
        em.add_field(name="୨୧・server count", value = f"✦ー`{str(len(self.client.guilds))}`")

        await ctx.send(embed = em)


    @commands.Cog.listener()
    async def on_member_join(self, member):
      collection = db["Greetings"]
      results = collection.find({"server_id": member.guild.id})

      for result in results:
        msg = result["message"]
        guild = result["server_id"]
        ch = result["channel_id"]

      guild = self.client.get_guild(guild)
      channel = guild.get_channel(ch)
      await channel.send(msg)
        
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def greetmsg(self, ctx, *, message):
      collection = db["Greetings"]

      post = {"server_id": ctx.message.guild.id, "message": message, "channel_id": ctx.message.channel.id}

      collection.delete_many({"server_id": ctx.message.guild.id})
      collection.insert_one(post) #magic 

      await ctx.send("Welcome message has been set.")

    

# this is the end of the code, type all mod commands above this
def setup(client):
    client.add_cog(Miscellaneous(client))