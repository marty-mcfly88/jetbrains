import string
import requests
from bs4 import BeautifulSoup

URL = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
content = requests.get(URL)
soup = BeautifulSoup(content.text, 'html.parser')

news_article_links = soup.find_all('span', {'class': 'c-meta__type'}, text='News') # replace <article_type>
for news_article in news_article_links:
    # Anchor
    anchor = news_article.find_parent('article').find('a', {'data-track-action': 'view article'})
    anchor_link = anchor['href']
    # Article name
    article_name: str = news_article.find_parent('article').find('a').contents[0]
    translation_table = article_name.maketrans(" ", "_", string.punctuation)
    article_name = article_name.translate(translation_table).rstrip() + ".txt"
    # Article body
    article_url = "https://www.nature.com" + anchor_link
    article_response = requests.get(article_url)
    article_soup = BeautifulSoup(article_response.content, 'html.parser')
    text = article_soup.find('div', {'class': 'c-article-body'}).text.strip()

    # Create file with the correct name and write to it
    # file = open(name, 'wb')
    # file.write(text.strip())
    # print('file written')
    # file.close()

    with open(article_name, "wb") as article_txt:
        text_bytes = text.encode('UTF-8')
        article_txt.write(text_bytes)

    #     for p in tags_p:
    #         body_string = p.string
    #         print(str(body_string).strip())
    #         body_string = str(body_string).strip()
