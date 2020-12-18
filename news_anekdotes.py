import discord
from discord.ext import commands
from script import anekdot_script
import random
from config import settings


bot = commands.Bot(command_prefix = ('Внимание ', 'внимание '))


@bot.command()
async def привет(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello, {author.mention}! Are you ready for a piece of jewish fun?')


anekdots = []
n_of_page = 1
@bot.command()
async def анекдот(ctx):
    global anekdots
    global n_of_page


    anekdots, n_of_page = anekdot_script(anekdots, n_of_page)


    if anekdots:
        random.shuffle(anekdots)
        await ctx.send('Внимание, анекдот!\n')
        await ctx.send(anekdots[0].text)
        anekdots.pop(0)
    else:
        await ctx.send('Nothing left! Find new web-site for fun!')

    
bot.run(settings['token'])
