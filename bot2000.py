import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='_', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def yardım_et (ctx):
    await ctx.send(f'Sana nasıl yardımcı olabilirim kralım ? ')

@bot.command()
async def oyun (ctx):
    secilen= random.choice(["CS2","MC","Döner efsanesi"])
    await ctx.send(f'işte oyun önerim: {secilen} ')

@bot.command()
async def ismin_neden_bot2000 (ctx):
    await ctx.send("Bimem, git enaryum'a sor")

@bot.command()
async def yazıcı3D (ctx):
    secilen= random.choice(["Bambu lab A1","bambu lab X1 carbon"])
    await ctx.send(f'işte 3D yazıcı önerim: {secilen} ')

@bot.command()
async def filement (ctx):
    secilen= random.choice(["Nane lab","Marka filement", "Solvix"])
    await ctx.send(f'işte flement önerim: {secilen} ')


bot.run("Token buraya")
