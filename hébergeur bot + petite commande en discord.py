import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')

@bot.command()
async def hi(ctx):
await ctx.send(f"Bonjour à toi !)


bot.run('Token Bot') # Remplacez *Token Bot* par le bon token de votre application discord. 
