import requests
from bs4 import BeautifulSoup

url = input("Digite uma URL de um produto do site: ")
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

product = soup.find_all('h1')[0].get_text()
desc = soup.select("div.text-more-info")[0].get_text()
price = soup.select("span.price-txt")[0].get_text()
points = (float(price[2:]) * 1.50 + float(price[2:]))
pts = points * 0.2
print("Produto: ", product, 'com', '{:.0f}'.format(pts),"pt(s) de qualificação")
print("Descrição: ", desc)
print("Valor Real: ", price)
print("Valor em Ponto(s): ", '{:.0f}'.format(points))
print('{:.0f}'.format(pts), "ponto(s) de Cashback")