import discord
from StuffsWeNeed import defaultstuff
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
      print ('Help module is ready.')

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
      # initial embed
      em = discord.Embed(title = defaultstuff.texts()["helpEmbed1Title"], description = defaultstuff.texts()["helpEmbed1Descr"], color = 0xe4d3b3)

      em.set_footer(text = "https://repl.it/@flo0003 ˚⊹", icon_url = "https://i.imgur.com/GgeUjQv.png")
      em.set_thumbnail(url = "https://media.discordapp.net/attachments/816336230081888269/817020579344416798/gf8HK6DDOea5rkAAAAASUVORK5CYII.png")

      await ctx.send(embed = em)

    # MODULES
    @help.command()
    async def admin(self, ctx):
      em = discord.Embed(title = defaultstuff.texts()["helpTitleAdminModule"], description = defaultstuff.texts()["helpTextAdminModule"], color = 0xe4d3b3)

      await ctx.send(embed = em)
    
    @help.command()
    async def mod(self, ctx):
      em = discord.Embed(title = defaultstuff.texts()["helpTitleModModule"], description = defaultstuff.texts()["helpTextModModule"], color = 0xe4d3b3)

      await ctx.send(embed = em)

    @help.command()
    async def fun(self, ctx):
      em = discord.Embed(title = defaultstuff.texts()["helpTitleFunModule"], description = defaultstuff.texts()["helpTextFunModule"], color = 0xe4d3b3)

      await ctx.send(embed = em)

    @help.command()
    async def eco(self, ctx):
      em = discord.Embed(title = defaultstuff.texts()["helpTitleEcoModule"], description = defaultstuff.texts()["helpTextEcoModule"], color = 0xe4d3b3)

      await ctx.send(embed = em)

    @help.command()
    async def misc(self, ctx):
      em = discord.Embed(title = defaultstuff.texts()["helpTitleMiscModule"], description = defaultstuff.texts()["helpTextMiscModule"], color = 0xe4d3b3)

      await ctx.send(embed = em)
    
# doki did smort thing ^ oooo very smort indeed

    # # help command KICK
    # @help.command(aliases = ['k'])
    # async def kick(self, ctx):
    #   em = discord.Embed(title = "`,kick` / `,k`", description = "Kicks a member of the server.", color = 0xe4d3b3)
    #   em.add_field(name = "Permissions", value = "KickMembers Permission")
    #   em.add_field(name = "Usage", value = ",kick <user> {reason}")

    #   await ctx.send(embed = em)

    #  @help.command()
    #  async def ping(self, ctx):
    #      em = discord.Embed(title = "``,ping`", description = "Displays Kaito's currect latency.", color = 0xe4d3b3)
    #      # no perms needed = no mention in the embed
    #      em.add_field(name = "Usage", value = ",ping")

    #      await ctx.send(embed = em)

    # @help.command(aliases=['av, pfp, profilepic'])
    # async def avatar(self, ctx):
    #     em = discord.Embed(title = "`,avatar` / `,av` / `,pfp` / `profilepic`", description = "Displays your avatar, provide a @Mention to get someone else's avatar.", color = 0xe4d3b3)
    #     # no perms needed = no mention in the embed
    #     em.add_field(name = "Usage", value = ",avatar or ,av @Someone")

    #     await ctx.send(embed = em)

    # @help.command()
    # async def invite(self, ctx):
    #     em =discord.Embed(title = "`,invite`", description = "Give Kaito's link to invite it to your server.", color = 0xe4d3b3)
    #     # no perms needed = no mention in de embed
    #     em.add_field(name ="Usage", value = ",invite")


# this is the end of the code, type all commands above this
def setup(client):
    client.add_cog(Help(client))