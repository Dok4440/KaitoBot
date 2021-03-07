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

    # hug command
    @commands.command()
    async def hug(self, ctx, user: discord.User, *, Notes=None):
         em = discord.Embed(title = f"୨୧・`🍰`・A hug for {user.name}! so cute! ー ✦", description=None,  color = 0xe4d3b3)

         hug_gifs = ["https://i.pinimg.com/originals/f2/80/5f/f2805f274471676c96aff2bc9fbedd70.gif", "https://i.imgur.com/mTAF7zA.gif", "https://media.tenor.com/images/b6d0903e0d54e05bb993f2eb78b39778/tenor.gif", "https://i.pinimg.com/originals/e2/c9/7a/e2c97a3b7a1ac0ec5bcecc0c18c61209.gif", "https://i.imgur.com/uXNQv1t.gif",  "https://i.pinimg.com/originals/9f/b8/ad/9fb8add5d9a2abe060cafcd211e1b8d5.gif"]

         em.set_image(url=random.choice(hug_gifs))
         em.set_footer(text = ("✦・(You guys are adorable...)"))

         await ctx.send(embed = em)


    # kiss command
    @commands.command()
    async def kiss(self, ctx, user: discord.User, *, Notes=None):
         em = discord.Embed(title = f"୨୧・`🍓`・A kiss for {user.name}! so cute! ー ✦", description=None,  color = 0xe4d3b3)

         kiss_gifs = ["https://i.pinimg.com/originals/e3/4e/31/e34e31123f8f35d5c771a2d6a70bef52.gif", "https://i.pinimg.com/originals/fe/6f/a7/fe6fa711ed29f18387c5da9800436062.gif", "https://i.pinimg.com/originals/44/74/7e/44747e448d7c150e95bbecb5c378bb35.gif", "https://i.imgur.com/WVSwvm6.gif", "https://i.imgur.com/OE7lSSY.gif"]

         em.set_image(url=random.choice(kiss_gifs))
         em.set_footer(text = ("✦・(I ship it...)"))

         await ctx.send(embed = em)


    # slap command
    @commands.command()
    async def slap(self, ctx, user: discord.User, *, Notes=None):
         em = discord.Embed(title = f"୨୧・`☕`・A slap for {user.name}! I hope they deserved it! ー ✦", description=None,  color = 0xe4d3b3)

         slap_gifs = ["https://i.pinimg.com/originals/fe/39/cf/fe39cfc3be04e3cbd7ffdcabb2e1837b.gif", "https://i.imgur.com/fm49srQ.gif", "https://i.kym-cdn.com/photos/images/newsfeed/000/940/326/086.gif", "https://i.imgur.com/yROjYng.gif", "https://reallifeanime.files.wordpress.com/2014/06/akari-slap.gif", "https://i.gifer.com/VF8X.gif", "https://hui3r.files.wordpress.com/2015/08/tumblr_mjpheaavj51s725bno1_500.gif"]

         em.set_image(url=random.choice(slap_gifs))
         em.set_footer(text = ("✦・(So violent...)"))

         await ctx.send(embed = em)


    # pat command
    @commands.command(aliases=['pet'])
    async def pat(self, ctx, user: discord.User, *, Notes=None):
         em = discord.Embed(title = f"୨୧・`🧇`・A pat for the cute {user.name}! Pat pat pat the {user.name}! ー ✦", description=None,  color = 0xe4d3b3)

         pat_gifs = ["https://i.pinimg.com/originals/ba/0a/18/ba0a18b4028f9c210f830f7a82a574cb.gif", "https://i.pinimg.com/originals/d7/c3/26/d7c326bd43776f1e0df6f63956230eb4.gif", "https://i.imgur.com/UWbKpx8.gif", "https://community.gamepress.gg/uploads/default/original/3X/6/6/664e58e013a8d2c3c3c8a4684aaeb192d1def025.gif", "https://i.imgur.com/LUypjw3.gif", "https://i.makeagif.com/media/6-04-2014/1m4gQJ.gif" ]

         em.set_image(url=random.choice(pat_gifs))
         em.set_footer(text = ("✦・(Now that's just adorable...)"))

         await ctx.send(embed = em)

# this is the end of the code, type all commands above this
def setup(client):
    client.add_cog(Fun(client))