#scrap the saved page and save it in .csv file

from bs4 import BeautifulSoup
import csv

with open('webscrap/sel.html') as html_file :

    soup = BeautifulSoup( html_file , 'lxml')


csv_file = open('webscrap/news.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title','summary','img_src'])


div = soup.find('div', id = 'latest-container')
for article in div.find_all('article') :
   
    image_src = article.find('div', class_= 'thumb').img['src']
    image_url = 'https://www.iottechnews.com' + image_src

    csv_writer.writerow([article.a.text,article.p.text,image_url])



csv_file.close()