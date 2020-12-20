#Parses the webpage and then gives anekdotes/news
from bs4 import BeautifulSoup
import requests


def anekdot_script(anekdots, n_of_page): #возвращает list анекдотов со страницы n_of_page + 1, если list пуст, и номер страницы
    url = 'https://humornet.ru/anekdot/evrei/page/{}/'


    if not anekdots: #если лист пустой
        response = requests.get(url.format(n_of_page)) #переходим на конкретную страницу с номером n_of_page
        response.encoding = 'utf-8'


        soup = BeautifulSoup(response.text, 'lxml') #парсим страницу
        anekdots = [anekdot.text.replace('-', '\n-') for anekdot in soup.select('.text')] # анекдоты имееют class = 'text', собираем анекдоты в список

        n_of_page += 1 #анекдоты собраны на этой страницу, переходим на следюущую
        
    
    return anekdots, n_of_page



def news_script(): #возвращает два словаря (главная и другие новости), ключ - сама новость, значение - ссылка на новость. Сайт - VTimes, экономика и финансы
                   #вы вполне можете сменить тематику, просто изменив URL VTimes, парсинг будет работать и с ними.
    response = requests.get('https://www.vtimes.io/economy') 
    soup = BeautifulSoup(response.text, 'lxml')


    #работает только на тематических разделах, на главном разделе такого класса нет, а вот класс дефолтных новостей есть,так что если настроите на главную страницу - вырезайте/комменьте эту часть кода
    soup_news_headline = soup.select('.article-excerpt-lead__link') #главная новость раздела
    news_headline = dict()
    news_headline[soup_news_headline[0]['title']] = soup_news_headline[0]['href']


    soup_news_default = soup.select(".article-excerpt-default__link") # остальные новости
    news_default = dict()
    for new in soup_news_default:
        news_default[new['title']] = new['href']


    return news_headline, news_default