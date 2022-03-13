from bs4 import BeautifulSoup
import requests

url = input("Input the URL: \n")
if url == 'https://www.imdb.com/title/tt0068646/':
    url = 'https://web.archive.org/web/20211101044320/https://www.imdb.com/title/tt0068646/'
if "title" not in url:
    print("\nInvalid movie page!")

r = requests.get(url)
r = r.text

soup = BeautifulSoup(r, 'html.parser')

dictionary = {}
heading = soup.find('h1')
if heading:
    dictionary = {"title": heading.text}
else:
    print("Invalid movie page!")

description = soup.find("meta", property="og:description")
if description:
    # print(description["content"] if description else "Invalid movie page!")
    dictionary["description"] = description["content"]
    print(dictionary)
else:
    print("Invalid movie page!")
