import csv
import requests
from bs4 import BeautifulSoup
mainContent = requests.get("https://cryptonewsandprices.me/")
# print(mainContent.text)

soup = BeautifulSoup(mainContent.text, 'html.parser')
title = soup.find('h5', class_='card-title').get_text()
print(title)

published = soup.find('small', class_='text-info').get_text().strip()
print(published)


titleall = soup.find_all('h5', class_='card-title')
# print(titleall)

title_list = []
for item in titleall:
    individualtitle = item.get_text()
    title_list.append(individualtitle)
print(title_list)

with open('pythonscraper.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for item in title_list:
        writer.writerow([item])
