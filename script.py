#Парсит веб-страницу и ретернит анекдоты о евреях, текст из сервиса балабоба
from bs4 import BeautifulSoup
import requests
import urllib.request
from fake_useragent import UserAgent 
import json 


def anekdot_script(anekdots, n_of_page): #ретернит лист анекдотов с конкретной страницы
    url = 'https://humornet.ru/anekdot/evrei/page/{}/'


    if not anekdots: #если лист пустой
        response = requests.get(url.format(n_of_page)) #собирает информацию со страницы, начиная с 1ой страницы
        response.encoding = 'utf-8'


        soup = BeautifulSoup(response.text, 'lxml') #парсит страницу в html формат
        anekdots = soup.select('.text') #анекдот имеют класс "text"

        n_of_page += 1 #переход на след. страницу
        
    
    return anekdots, n_of_page


def balaboba_script(text): #ретернит строку, полученную в результате ввода вашего текста в сервис балабобу
    url = "https://zeapi.yandex.net/lab/api/yalm/text3"
    ua = UserAgent().ff
    headers = {
    'Content-Type': 'application/json',
    'User-Agent': ua,
    'Origin': 'https://yandex.ru',
    'Referer': 'https://yandex.ru/',
    }
    payload = {"query": text,"intro": 0,"filter": 1}
    params =  json.dumps(payload).encode('utf-8')

    req = urllib.request.Request(url, data=params, headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))

    
    return json_data['text']

