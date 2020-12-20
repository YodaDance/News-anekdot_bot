#Parses the webpage and then gives anekdotes about jewish
from bs4 import BeautifulSoup
import requests


def anekdot_script(anekdots, n_of_page): #return list of anekdots of a specific page
    url = 'https://humornet.ru/anekdot/evrei/page/{}/'


    if not anekdots: #if the list is empty
        response = requests.get(url.format(n_of_page)) #getting page info, starts with the first page
        response.encoding = 'utf-8'


        soup = BeautifulSoup(response.text, 'lxml') #parses the page to html format
        anekdots = soup.select('.text') #anekdots have class 'text' on this page

        n_of_page += 1 #turning on the next page
        
    
    return anekdots, n_of_page



def news_script(): #возвращает два словаря (главная и другие новости), ключ - сама новость, значение - ссылка на новость. Сайтй - VTimes, экономика и финансы
                   #вы вполне можете сменить тематику, просто изменив URL VTimes, парсинг будет работать и с ними.
    response = requests.get('https://www.vtimes.io/economy') 
    soup = BeautifulSoup(response.text, 'lxml')

    #работает только на тематических разделах, на главном разделе такого класса нет, а вот класс дефолтных новостей есть,так что если настроите на главную страницу - вырезайте/комменьте эту часть кода
    soup_news_headline = soup.select('.article-excerpt-lead__link')
    news_headline = dict()
    news_headline[soup_news_headline[0]['title']] = soup_news_headline[0]['href']


    soup_news_default = soup.select(".article-excerpt-default__link")
    news_default = dict()
    for new in soup_news_default:
        news_default[new['title']] = new['href']


    return news_headline, news_default