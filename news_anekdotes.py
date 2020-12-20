import discord
from discord.ext import commands
from script import anekdot_script, news_script
from discord.utils import get
import random
from config import settings


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = ('Внимание ', 'внимание '), intents = intents)


#bot events - при определенных событиях бот будет реагировать и выполнять действия
@bot.event
async def on_ready(): #в консоли выдает сообщение, что работает
    print('Таки я уже и заработал! Что клювом щёлкаешь?\nТаки моя работа и не бесплатная!\n')


@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server! Sending welcome message...\n')
    channel = get(member.guild.channels, name="основной") #вставьте название вашего канала
    await channel.send(f'\nТаки и новый гость к нам пожаловал!\nШалом, {member.mention}! Таки ты готов к новой порции маленькой кошерной радости?')
    #ваше любое сообщение по желанию


@bot.event
async def on_member_remove(member): #пользователь уходит с канала или его выгнали
    print(f'{member} has left the server! Sending bye message...\n')
    channel = get(member.guild.channels, name="основной") #вставьте название вашего канала для вывода сообщения
    await channel.send(f'\n{member.mention} таки и покинул нас. А где мои денюжки? Таки вы мне должны заплатить за выход, как в любом приличном заведении!')
    #ваше любое сообщение по желанию


#bot commands - команды в чате
anekdots = []
n_of_page = 1
@bot.command()
async def анекдот(ctx): #будет выводить анекдот, пока они не кончатся
    global anekdots
    global n_of_page


    anekdots, n_of_page = anekdot_script(anekdots, n_of_page)


    if anekdots:
        random.shuffle(anekdots) #перемешивает список анекдотов, чтобы не выдавал их в одном и том же порядке
        await ctx.send('Внимание, анекдот!\n')
        await ctx.send(anekdots[0].text)
        anekdots.pop(0) #удаляем анекдот из пулла
    else:
        await ctx.send('Анекдоты кончились, дядя! Ну что ты так много и жадно их читаешь!\nА теперь и сам ищи себе эти анекдоты, родной!')
        #анекдоты могут и кончится :)


@bot.command()
async def новости(ctx): #напишет в чат основную новость и 5 других, отображаемые на сайте VTimes
                        # вы можете сделать больше,чем 5. Новостей около 18 в пулле будет(главная + 17 обычных)
    news_headline, news_default = news_script() #создаем главную и другие новости в виде словарей
    news_headline_key = list(news_headline.keys())[0] #сама главная новость, заодно ключ для ссылки
    news_headline_href = '<{}>'.format(news_headline[news_headline_key]) #чтобы embed не выскакивал при выскакивании ссылок
    

    news_headline_output = f'***Внимание, новости!\n\n\nГлавная новость:***\n{"**" + news_headline_key + "**"}.\nСсылка к прочтению:\n{news_headline_href}\n\n\n'


    default_news_output = '***Перейдем к другим новостям:***\n'
    for i in range(5): #аналогично как и с главной новостью, только теперь в цикле
        news_default_key = list(news_default.keys())[i]
        news_default_href = '<{}>'.format(news_default[news_default_key])
        default_news_output += f'{i+1}) {"**" + news_default_key + "**" }.\nСсылка к прочтению:\n{news_default_href}\n\n'

    
    final_news = news_headline_output + default_news_output #сводим главную и другие новости в 1 сообщение
    await ctx.send(final_news) #отправляем сообщение

bot.run(settings['token']) #у меня создан отдельный файл с конфигом, сюда в ы можете просто вставить свой токен
