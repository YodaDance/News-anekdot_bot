import discord
from discord.ext import commands
from script import anekdot_script
from discord.utils import get
import random
from config import settings


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = ('Внимание ', 'внимание '), intents = intents)


#bot events
@bot.event
async def on_ready(): #just give you a message that it works
    print('Таки я уже и заработал! Что клювом щёлкаешь?\nТаки моя работа и не бесплатная!\n')


@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server! Sending welcome message...\n')
    channel = get(member.guild.channels, name="основной")
    await channel.send(f'Таки и новый гость к нам пожаловал!\nШалом, {member.mention}! Таки ты готов к новой порции маленькой кошерной радости?\n')


@bot.event
async def on_member_remove(member):
    print(f'{member} has joined the server! Sending bye message...\n')
    channel = get(member.guild.channels, name="основной")
    await channel.send(f'{member.mention} таки и покинул нас. А где мои денюжки? Таки вы мне должны заплатить за выход, как в любом приличном заведении!\n')


#bot commands
anekdots = []
n_of_page = 1
@bot.command()
async def анекдот(ctx): #pops out a joke
    global anekdots
    global n_of_page


    anekdots, n_of_page = anekdot_script(anekdots, n_of_page)


    if anekdots:
        random.shuffle(anekdots)
        await ctx.send('Внимание, анекдот!\n')
        await ctx.send(anekdots[0].text)
        anekdots.pop(0)
    else:
        await ctx.send('Анекдоты кончились, дядя! Ну что ты так много и жадно их читаешь!\nА теперь и сам ищи себе эти анекдоты, родной!')

  
bot.run(settings['token'])
