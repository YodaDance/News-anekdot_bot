# Parses the webpage and then gives anekdotes/news
from bs4 import BeautifulSoup
import requests


def anekdot_script(anekdots, n_of_page):
    # возвращает list анекдотов со страницы n_of_page + 1, если list пуст
    # и n_of_page
    url = 'https://humornet.ru/anekdot/evrei/page/{}/'
    if not anekdots:  # если лист пустой
        # переходим на конкретную страницу с номером n_of_page
        response = requests.get(url.format(n_of_page))
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')  # парсим страницу
        anekdots = [anekdot.text.replace('-', '\n-') for anekdot
                    in soup.select('.text')]
        # анекдоты собраны на этой странице, переходим на следюущую
        n_of_page += 1
    return anekdots, n_of_page


def news_script():
    # возвращает два словаря (главная и другие новости)
    # ключ - сама новость, значение - ссылка на новость.
    response = requests.get('https://www.vtimes.io/economy')
    soup = BeautifulSoup(response.text, 'lxml')
    # работает только на тематических разделах, на главном разделе - нет
    # класс дефолтных новостей есть, так что если хотите на главной -
    # вырезайте/комменьте эту часть кода
    # главная новость раздела
    soup_news_headline = soup.select('.article-excerpt-lead__link')
    news_headline = dict()
    # главная новость
    news_headline_key = soup_news_headline[0]['title']
    # заводим в словарь со ссылкой
    news_headline[news_headline_key] = soup_news_headline[0]['href']
    # остальные новости, аналогично главной
    soup_news_default = soup.select(".article-excerpt-default__link")
    news_default = dict()
    for new in soup_news_default:
        news_default[new['title']] = new['href']
    return news_headline, news_default
