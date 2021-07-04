import discord
from discord.ext import commands
<<<<<<< Updated upstream:news_anekdotes.py
from script import anekdot_script, news_script
=======
from script import anekdot_script, balaboba_script
>>>>>>> Stashed changes:main.py
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
        await ctx.send(anekdots[0])  # случайный анекдот
        anekdots.pop(0)  # удаляем анекдот из пулла
    else:
<<<<<<< Updated upstream:news_anekdotes.py
        await ctx.send('Анекдоты кончились, дядя! \
                        Что ты так много и жадно их читаешь!\n\
                        А теперь и сам ищи себе эти анекдоты, родной!')
        # анекдоты могут и кончится :)


@bot.command()
async def новости(ctx):  # напишет в чат новости, отображаемые на сайте VTimes
    news_headline, news_default = news_script()
    # сама главная новость, заодно ключ для ссылки
    news_headline_key = list(news_headline.keys())[0]
    # чтобы embed не выскакивал при выскакивании ссылок
    news_headline_href = '<{}>'.format(news_headline[news_headline_key])
    news_headline_output = f'***Внимание, новости!\n\n\nГлавная новость:***\n\
                            {"**" + news_headline_key + "**"}.\nСсылка \
                            к прочтению:\n{news_headline_href}\n\n\n'
    default_news_output = '***Перейдем к другим новостям:***\n'
    # аналогично главной новости, только теперь в цикле
    for i in range(5):  # можете изменить количество вывода
        news_default_key = list(news_default.keys())[i]
        news_default_href = '<{}>'.format(news_default[news_default_key])
        default_news_output += f'{i+1}) {"**" + news_default_key + "**" }.\n\
                                Ссылка к прочтению:\n{news_default_href}\n\n'
    # сводим новости в 1 сообщение
    final_news_output = news_headline_output + default_news_output
    await ctx.send(final_news_output)  # отправляем сообщение
bot.run(settings['token'])  # вы можете вставить свой токен
=======
        await ctx.send('Анекдоты кончились, дядя! Ну что ты так много и жадно их читаешь!\nА теперь и сам ищи себе эти анекдоты, родной!')
        #анекдоты могут и кончится :)


@bot.command()
async def балабоба(ctx, *arg):
    # реализация в комментах позволяет вам сначала вызвать команду, а потом добавить в нее текст для вызова скрипта балабобы
    # await ctx.send('Таки и поведай мне, что ты хочешь написать!')
    

    # def check(msg):
    #     return msg.author == ctx.author and msg.channel == ctx.channel 


    # try:
    #     msg = await bot.wait_for('message', check = check, timeout = 30) #30 сек на ввод текста
    # except asyncio.TimeoutError:
    #     await ctx.send('Таки клювом в нашей семье не щелкают и отвечают быстро!')
    
    # await ctx.send(balaboba_script(msg.content))
    text = " ".join(arg)
    try:
        await ctx.send(f"**{text}** {balaboba_script(text)}")
    except:
        await ctx.send('Алю! За такие слова и на базаре нос отрывают! Ошибка!')
    
  
bot.run(settings['token']) #у меня создан отдельный файл с конфигом, сюда вы можете просто вставить свой токен
>>>>>>> Stashed changes:main.py
