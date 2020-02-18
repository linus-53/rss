import requests
from bs4 import BeautifulSoup
import csv



url = "https://rss.nytimes.com/services/xml/rss/nyt/US.xml"
resp = requests.get(url)

soup = BeautifulSoup(resp.content, features="xml")

items = soup.findAll('item')

news_items = []

for item in items:
    news_item = {}
    news_item['title'] = item.title.text
    news_item['description'] = item.description.text
    news_item['link'] = item.link.text
    news_items.append(news_item)

with open('news.csv', 'w') as fobj:
    csvwriter = csv.writer(fobj, delimiter=',')
    for row in test:
        csvwriter.writerow(test)
