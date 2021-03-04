#Desafio 114
# Crie um codigo em Python que teste se o site Pudim está acessivel pelo computador utilizado.
import requests

#try:
resp = requests.get(url='http://pudim.com.br')
print(resp)
#except:
    