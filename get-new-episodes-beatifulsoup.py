#import what we need
# install these modules: beautifulsoup4 lxml html5lib requests
from bs4 import BeautifulSoup
import requests, re

#use session to get the page
r = requests.get('https://comandotorrent.net/the-good-doctor-4a-temporada-download-torrent-2020-dual-audio-legendado-web-dl-720p-1080p/')

site = BeautifulSoup(r.text, "html.parser")

#print(site.find('p').parent)
#print(site.find('a').get('href'))
#print(site.select("div", class_="entry-content cf"))
#print(site.find('div', class_="entry-content cf").find_all('p'))
#print(site.find_all('div', class_='entry-content cf')[0])
s = site.find('div', class_="entry-content cf").find_all('a')
for cont in s:
    if 'href' in cont.attrs:
        print(str(cont.attrs['href']))

# a = site.select("div", class_= "entry-content cf")
# try:
#     episode = a[0].get_text()
# #print(a)
# par = site.select('p')
# print(par)

#print(site)
# site = BeautifulSoup(r, 'lxml')
# eps = site.find_all("div", class_="entry-content cf")
# title = site.find_all("p", string=re.compile("Episódio 01"))
# links = site.select("p")
# actual = [link['href'] for link in links]
# a = site.find_parent("p")
# print(a)
# new = site.body.div.p
#print(actual)
#print(eps)
#print(title)
#print(links)
#print(new)

#eps = site.find_all('p')
# for new in eps:
#     #title = new.h2.a.text
#     sum = new.find('div', class_='entry-content cf')  
#     print(sum)   
#print(site.prettify())
# for article in site:
#     #ep = site.find(string=re.compile("LEGENDADO"))
#     ep = site.find_all(('p'))