import string
import requests
from bs4 import BeautifulSoup
import os


def get_clean_title(title):
    title = title.replace(" ", "_")
    for i in list(string.punctuation):
        title = title.replace(i, "_")
    return title


def article(url,URL_BASE,user_article):
    r = requests.get(url)
    if r.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        saved_articles = []
        articles = soup.find_all('article')
        for article in articles:
            article_type = article.find('span', 'c-meta__type').text.strip()
            if article_type == user_article:
                sublink = article.find('a').get('href')
                full_link = URL_BASE + sublink
                req = requests.get(full_link)
                soup = BeautifulSoup(req.text, 'html.parser')
                page_body = soup.find('div', {'class': 'c-article-body'}).text.strip()
                # page_body = soup.find('body').text.encode()
                h1 = soup.find('div', 'c-article-header__restrict').find('h1').text.strip()
                file_name = get_clean_title(h1) + '.txt'
                with open(file_name, 'wb') as file:
                    page_body = page_body.encode('UTF-8')
                    file.write(page_body)
                saved_articles.append(file_name)


n = int(input())
user_article = input()

URL = 'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page='
URL_BASE = 'https://www.nature.com'
first_address = os.getcwd()
for i in range(1,   n+1):
    folder_name = f'Page_{i}'
    os.chdir(first_address)
    print(os.getcwd())
    os.mkdir(folder_name)
    os.chdir(folder_name)
    article(URL+str(i), URL_BASE, user_article)
