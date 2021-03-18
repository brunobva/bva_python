#import what we need
from requests_html import HTMLSession
session = HTMLSession()

#use session to get the page
#r = session.get('https://comandotorrent.net/the-good-doctor-4a-temporada-download-torrent-2020-dual-audio-legendado-web-dl-720p-1080p/')
r = session.get('https://www.baixafilmetorrent.net/the-good-doctor-o-bom-doutor-4a-temporada-completa-torrent-dublada-e-legendada/')
#render the html, sleep=1 to give it a second to finish before moving on. scrolldown= how many times to page down on the browser, to get more results. 5 was a good number here
r.html.render()

#find all the articles by using inspect element and create blank list
articles = r.html.find('conteudo.clearfix')

for article in articles:
    # episode = article.find('strong', first=True).text
    # print(episode)
    link = article.find('td-ep-qua', first=True).text
    print(link)
#print(articles)