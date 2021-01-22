import discord
from discord.ext import commands
from functions import *

intens = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix='?m ', intens=intens)
game = Game()


@Bot.event
async def on_ready():
    print("I'm ready!!")


@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="hoşgeldiniz")
    await channel.send(f"{member.mention} lavuk slide cancelladı.")
    print(f"{member} lavuk slide cancelladı.")


@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="gidenler")
    await channel.send(f"{member.mention} Aramızdan ayrıldı sg")
    print(f"{member} Aramızdan ayrıldı sg")


@Bot.command(aliases=["game", "oyun"])
async def Shultz(ctx, *args):
    if "roll" in args:
        await ctx.send(game.roll_dice())
    else:
        await ctx.send('Buğra Aydın Götünü Siktim Gözün Aydın')


Bot.run('ODAwNjQ1MDM2NjA5NzY1Mzc2.YAVIyw.jCHbSnZX8xyMikR1ROjLRqNP4Ws')
