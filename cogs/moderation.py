import discord
from discord.ext import commands
class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
      print ('Moderation module is ready.')

    # kick command
    @commands.command()
    @commands.has_permissions(kick_members=True) # check if the user has kick perms
    @commands.bot_has_permissions(kick_members=True) # check if the bot has kick perms
    async def kick(self, ctx, user: discord.Member, *, reason=None):
       await ctx.guild.kick(user, reason=reason)
       em = discord.Embed(title = f"> __**Kick !!**__", description = f"╭ ₊˚`🍓`ฅ︰**{user.name}** was kicked. ꒷꒦\n┊₊˚୨`☕`ɞ﹒**reason:** {reason}. ꒷꒦\n╰ฅ`🍰`๑︰**Moderator:** {ctx.author.display_name}. ꒷꒦",  color = 0xe4d3b3)
       await ctx.send(embed = em)
       await ctx.message.delete()
    # @kick.error()
    # async def kick(self, ctx, user: discord.Member, *, reason=None):
    #   await ctx.send("Insuff perms test")

    #ban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, id: int, *, reason=" - "):
        user = await self.client.fetch_user(id)
        actualReason = ctx.author.name + " | " + str(reason)
        await ctx.guild.ban(user, reason=actualReason)
        await ctx.send(f"> __**Ban !!**__\n╭ ₊˚`🍓`ฅ︰**{user.name}** was banned. ꒷꒦\n┊₊˚୨`☕`ɞ﹒**reason:** {reason}. ꒷꒦\n╰ฅ`🍰`๑︰**Moderator:** {ctx.author.display_name}. ꒷꒦")
        await ctx.message.delete()
        
    # unban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, id: int):
        user = await self.client.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f"> __**Unban !!**__\n╭ ₊˚`🍓`ฅ︰**{user.mention}** was unbanned. ꒷꒦\n┊₊˚୨`☕`ɞ﹒**user ID:** {user.ID} ꒷꒦\n╰ฅ`🍰`๑︰**Moderator:** {ctx.message.author.name}. ꒷꒦")
        await ctx.message.delete()


# this is the end of the code, type all mod commands above this
def setup(client):
    client.add_cog(Moderation(client))