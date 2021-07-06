import discord
from discord.ext import commands
from script import anekdot_script, balaboba_script
from discord.utils import get
import random
from config import settings


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=('Внимание ', 'внимание '), intents=intents)


# bot events - при определенных событиях бот будет реагировать и действовать
@bot.event
async def on_ready():  # в консоли выдает сообщение, что работает
    print('Что клювом щёлкаешь?\nТаки моя работа и не бесплатная!\n')


@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server! Sending welcome message...\n')
    channel = get(member.guild.channels, name="основной")  # name = ваш канал
    await channel.send(f'\nТаки и новый гость к нам пожаловал!\n \
                        Шалом, {member.mention}! Таки ты готов к новой порции \
                        маленькой кошерной радости?')
    # ваше любое сообщение по желанию


@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server! Sending bye message...\n')
    channel = get(member.guild.channels, name="основной")
    await channel.send(f'\n{member.mention} таки и покинул нас. \
                        А где мои денюжки? Таки вы мне должны заплатить \
                        за выход, как в любом приличном заведении!')
    # ваше любое сообщение по желанию


# bot commands - команды в чате
anekdots = []
n_of_page = 1


@bot.command()
async def анекдот(ctx):  # будет выводить анекдот, пока они не кончатся
    global anekdots
    global n_of_page

    anekdots, n_of_page = anekdot_script(anekdots, n_of_page)

    if anekdots:
        random.shuffle(anekdots)  # перемешивает список анекдотов
        await ctx.send('Внимание, анекдот!\n')
        await ctx.send(content=anekdots[0])  # tts = True случайный анекдот
        anekdots.pop(0)  # удаляем анекдот из пулла
    else:
        await ctx.send('Анекдоты кончились, дядя! \
            Ну что ты так много и жадно их читаешь!\
                \nА теперь и сам ищи себе эти анекдоты, родной!')
        # анекдоты могут и кончится :)


@bot.command()
async def балабоба(ctx, *arg):
    # реализация в комментах позволяет вам сначала вызвать команду,
    # а потом добавить в нее текст для вызова скрипта балабобы
    # await ctx.send('Таки и поведай мне, что ты хочешь написать!')
    # def check(msg):
    #     return msg.author == ctx.author and msg.channel == ctx.channel
    # try:
    #     msg = await bot.wait_for('message', check = check, timeout = 30)
    # #30 сек на ввод текста
    # except asyncio.TimeoutError:
    #     await ctx.send('Таки клювом в нашей семье не щелкают и отвечают быстро!')
    # await ctx.send(balaboba_script(msg.content))
    text = " ".join(arg)
    try:
        await ctx.send(f"**{text}** {balaboba_script(text)}")
    except KeyError:
        await ctx.send('Алю! За такие слова и на базаре нос отрывают! Ошибка!')
bot.run(settings['token'])   # ваш токен вместо settings['token']
