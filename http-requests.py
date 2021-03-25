# https://youtu.be/c5FKPzUL70U

# import requests

# resposta = requests.get('https://api.github.com')

# #print(resposta.status_code)

# dados = resposta.text # para mostrar a saida em modo texto
# dados = resposta.json() # para mostrar a saída em modo json
# print(dados['current_user_url'])
### https://youtu.be/2Co4cjPMTnk
# import requests

# cabecalho = {'User-agent': 'Windows 12',
#               'Referer':'https://google.com'}

# r = ''
# try:
#     #r = requests.get('https://solyd.com.br')
#     r = requests.post('https://g1.globo.com.br', 
#                         headers=cabecalho)
#     print(r.status_code)
# except Exception as e:
#     print("Requisição falhou: ", e)

#### https://youtu.be/Qd8JT0bnJGs
import requests

url = "http://localhost:3001/users"

user_data = {
	"nome": "Bruno",
	"password": "Bruno@2021",
	"email": "bruno@email.com"
}

r = requests.post(url, json=user_data)

if r.status_code >= 200 r.status_code <=299;
	#Sucesso

else:
	#Erro

print(r)