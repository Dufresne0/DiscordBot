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
    channel = discord.utils.get(member.guild.text_channels, name="hosgeldiniz")
    await channel.send(f'{member.mention} lavuk slide cancelladı')
    print(f'{member.mention} lavuk slide cancelladı')


@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="hosgeldiniz")
    await channel.send(f'{member} aramızdan ayrıldı')
    print(f'{member} aramızdan ayrıldı')


@Bot.command()
async def Bot_komutlar(ctx, *args):
    await ctx.send("""
    Botu aktif etmek için : ?m komutunu kullanın
    
    Bir üyeyi banlamak için : ?m ban @member reason
    
    Bir üyenin banını açmak için : ?m unban member#1111
    
    Bir üyeyi atmak için : ?m kick @member
    
    Komutları tekrar görmek için herhangi bir kanala 'Bot_komutlar' yazın
    
    Bir kanalı çoğaltmak için çoğaltmak istediğniz kanala gidip : ?m copy deyin
    Zar atmak için ?m game roll deyin
    
    Yazdıklarınızı silmek için ?m clear deyin yazdığınız son mesajla birlikte yukarı doğru 5 mesaj siler 
    ne kadar silmesini istiyorsanız sayı verin
    
    >#This Bot belongs to Shultz<
                """)


@Bot.command(aliases=["game", "oyun"])
async def Shultz(ctx, *args):
    if "roll" in args:
        await ctx.send(game.roll_dice())
    else:
        await ctx.send('This Bot belongs to Shultz')


@Bot.command()
@commands.has_role("Bot-Komut")
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@Bot.command(aliases=["copy"])
async def clone_channel(ctx, amount=1):
    for i in range(amount):
        await ctx.channel.clone()


@Bot.command()
@commands.has_role("Bot-Komut")
async def kick(ctx, member: discord.Member, *args, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User has been kicked {member.mention}')


@Bot.command()
@commands.has_role("Bot-Komut")
async def ban(ctx, member: discord.Member, *args, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User has been banned {member.mention}')


@Bot.command()
@commands.has_role("Bot-Komut")
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for bans in banned_users:
        user = bans.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned user {user.mention}')
            return


Bot.run("--")
