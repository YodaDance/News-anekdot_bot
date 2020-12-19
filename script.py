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

