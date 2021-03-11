# https://youtu.be/a6fIbtFB46g

#1) install - pip install request-html


import csv
from requests_html import HTML, HTMLSession
# # From file .html
# with open('simple.html') as html_file:
#     source = html_file.read()
#     html = HTML(html=source)

# in order to save the result into a csv
csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Video'])

session = HTMLSession()
r = session.get('https://coreyms.com')

articles = r.html.find('article')

#articles = html.find('div.article')
# for article in articles:
#     # headline = article.find('h2', first=True).text
#     # headline = article.find('p', first=True).text

# print(headline)
# print(summary)

# article = html.find('div.article')
for article in articles:
    headline = article.find('.entry-title-link', first=True).text
    print(headline)
    summary = article.find('.entry-content p', first=True).text
    print(summary)
try:
    vid_src = article.find('iframe', first=True)
    vid_id = vid_src.split('/')[4]
    vid_id = vid_srv.split('?')[0]
    yt_link = f'https://youtube.com/watch?v={vid_id}'
except Exception as e:
    yt_link = None

print(yt_link)
print()

csv_writer.writerow([headline, summary, yt_link])


csv_file.close()
# print(article.text)

# vid_src = article.find('iframe', first=True)
# print(vid_srv.html)
# print(vid_srv.attrs) # Get an Dict with all atribute as dictionary
# print(vid_srv.attrs['src']) # To get just the src attribute
# vid_id = vid_src.split('/')[4]
# vid_id = vid_srv.split('?')[0] # get just the video ID
# print(vid_id)
# yt_link = f'https://youtube.com/watch?v={vid_id}'
# print(yt_link)