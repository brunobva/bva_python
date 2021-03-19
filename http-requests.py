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

url = 'http://127.0.0.1:3001/users'

user_data = {
			"nome": "Vanessa Moraes",
			"password": "123321",
			"email": "Vanessa@email.com" 
}

r = requests.post(url, json=user_data)

if r.status_code >= 200 and r.status_code <= 299:
	print(f"Status Code {r.status_code}")
	print(f"Reason: {r.reason}")
	#$print(f"Texto: {r.text}")
	print(f"JSON: {r.json()}")
else:
	#Erros
	print(f"Status Code {r.status_code}")
	print(f"Reason: {r.reason}")
	#print(f"Texto: {r.text}")
	print(f"JSON: {r.json()}")

#### post: criando tokens 
url_token = 'http://127.0.0.1:3001/tokens'

data_token = {
			"password": "123321",
			"email": "bruno@email.com"
}
gtoken = requests.post(url_token, json=data_token)

if gtoken.status_code >= 200 and gtoken.status_code <= 299:
	print(f"Status Code {gtoken.status_code}")
	print(f"Reason: {gtoken.reason}")
	#$print(f"Texto: {gtoken.text}")
	
	token_data = gtoken.json()
	token = token_data['token']

	with open('token.txt', 'w') as file:
		file.write(token)
	print("Passo 1")
else:
	#Erros
	print(f"Status Code {gtoken.status_code}")
	print(f"Reason: {gtoken.reason}")
	#print(f"Texto: {gtoken.text}")
	print(f"JSON: {gtoken.json()}")
	print("Else: Passo 1")

## post -- Criando alunos

url_aluno = 'http://127.0.0.1:3001/alunos'

ntoken = 'Bearer '
with open('token.txt', 'r') as f:
	ntoken += f.read()

headers = {
	'Authorization': ntoken 
}

data_aluno = {
			"nome": "Marcilio",
			"sobrenome": "Jones",
			"email": "jones@email.com",
			"idade": "54",
			"peso": "89",
			"altura": "1.81"
			}
cr_aluno = requests.post(url_aluno, json=data_aluno, headers=headers)

if cr_aluno.status_code >= 200 and cr_aluno.status_code <= 299:
	print(f"Status Code {cr_aluno.status_code}")
	print(f"Reason: {cr_aluno.reason}")
	#print(f"Texto: {cr_aluno.text}")
	print(f"JSON: {cr_aluno.json()}")
	print("Passo 2")
else:
	#Erros
	print(f"Status Code {cr_aluno.status_code}")
	print(f"Reason: {cr_aluno.reason}")
	#print(f"Texto: {cr_aluno.text}")
	print(f"JSON: {cr_aluno.json()}")
	print("Else: Passo 2")
	
## get 
get_aluno = 'http://127.0.0.1:3001/alunos/2'
get_alunos = 'http://127.0.0.1:3001/alunos'

# ntoken = 'Bearer '
# with open('token.txt', 'r') as f:
# 	ntoken += f.read()

headers = {
# 	'Authorization': ntoken 
}

get_data_aluno = {
# 			"nome": "Abner",
# 			"sobrenome": "Garofo",
# 			"email": "garofo@email.com",
# 			"idade": "40",
# 			"peso": "110",
# 			"altura": "1.86"
 			}
aluno_get = requests.get(get_alunos, json=get_data_aluno )

if aluno_get.status_code >= 200 and aluno_get.status_code <= 299:
	print(f"Status Code {aluno_get.status_code}")
	print(f"Reason: {aluno_get.reason}")
	#print(f"Texto: {aluno_get.text}")
	#print(f"JSON: {aluno_get.json()}")
	
	r_data = aluno_get.json()
	#print(r_data)
	# print(r_data['nome'])
	# print(r_data['email'])
	for aluno in r_data:
		print(aluno)
	print("Passo 3")
else:
	#Erros
	print(f"Status Code {aluno_get.status_code}")
	print(f"Reason: {aluno_get.reason}")
	#print(f"Texto: {aluno_get.text}")
	#print(f"JSON: {aluno_get.json()}")
	for aluno in r_data:
		print(aluno['id'],aluno['nome'])
	print("Else: Passo 3")

### put - atualizar dados

put_aluno = 'http://127.0.0.1:3001/alunos/2'

ptoken = 'Bearer '
with open('token.txt', 'r') as a:
	ptoken += a.read()

headers = {
 	'Authorization': ptoken 
}

put_data_aluno = {
			"nome": "Jurema",
 			 "sobrenome": "Olive",
 			 "email": "jurema@email.com",
 			# "idade": "55",
 			# "peso": "110",
 			# "altura": "1.78"
 			}
aluno_put = requests.put(put_aluno, json=put_data_aluno, headers=headers)

if aluno_put.status_code >= 200 and aluno_put.status_code <= 299:
	print(f"Status Code {aluno_put.status_code}")
	print(f"Reason: {aluno_put.reason}")
	#print(f"Texto: {aluno_put.text}")
	#print(f"JSON: {aluno_put.json()}")
	
	r_data = aluno_put.json()
	print(r_data)
	# print(r_data['nome'])
	# print(r_data['email'])
	#for aluno in r_data:
	#	print(aluno['id'],aluno['nome'],aluno['sobrenome'])
	print("Passo 4")
else:
	#Erros
	print(f"Status Code - Else: {aluno_put.status_code}")
	print(f"Reason - Else: {aluno_put.reason}")
	#print(f"Texto: {aluno_put.text}")
	#print(f"JSON: {aluno_put.json()}")
	print("Else: Passo 4")

### delete - Deletar dados

del_aluno = 'http://127.0.0.1:3001/alunos/2'

ptoken = 'Bearer '
with open('token.txt', 'r') as a:
	ptoken += a.read()

headers = {
 	'Authorization': ptoken 
}

del_data_aluno = {
			# "nome": "Jurema",
 			#  "sobrenome": "Olive",
 			#  "email": "jurema@email.com",
 			# "idade": "55",
 			# "peso": "110",
 			# "altura": "1.78"
 			}
aluno_del = requests.delete(del_aluno, json=del_data_aluno, headers=headers)

if aluno_del.status_code >= 200 and aluno_del.status_code <= 299:
	print(f"Status Code {aluno_del.status_code}")
	print(f"Reason: {aluno_del.reason}")
	#print(f"Texto: {aluno_del.text}")
	print(f"JSON: {aluno_del.json()}")
	
	r_data = aluno_del.json()
	print(r_data)
	# print(r_data['nome'])
	# print(r_data['email'])
	# for aluno in r_data:
	# 	print(aluno['id'],aluno['nome'],aluno['sobrenome'])
	print("Passo 5")
else:
	#Erros
	print(f"Status Code - Else: {aluno_get.status_code}")
	print(f"Reason - Else: {aluno_get.reason}")
	#print(f"Texto: {aluno_del.text}")
	#print(f"JSON: {aluno_del.json()}")
	print("Else: Passo 5")

### Passo 6: Upload Foto
## post
from requests_toolbelt import MultipartEncoder
from mimetypes import MimeTypes

mimetypes = MimeTypes()

arquivo_f = 'Logo - BVA - Original.png'
mimetype_f = mimetypes.guess_type(arquivo_f)[0]
# print(mimetype_f)

multipart = MultipartEncoder(fields={
	'aluno_id': '5',
	'foto': (arquivo_f, open(arquivo_f, 'rb'), mimetype_f)
})

url_foto = 'http://127.0.0.1:3001/fotos'

ntoken = 'Bearer '
with open('token.txt', 'r') as f:
	ntoken += f.read()

headers = {
 	'Authorization': ntoken,
	'Content-Type': multipart.content_type

}

nfoto = requests.post(url_foto, headers=headers, data=multipart)

if nfoto.status_code >= 200 and nfoto.status_code <= 299:
	print(f"Status Code {nfoto.status_code}")
	print(f"Reason: {nfoto.reason}")
	#print(f"Texto: {nfoto.text}")
	print(f"JSON: {nfoto.json()}")
	print("Passo 6")
else:
	#Erros
	print(f"Status Code {nfoto.status_code}")
	print(f"Reason: {nfoto.reason}")
	#print(f"Texto: {nfoto.text}")
	print(f"JSON: {nfoto.json()}")
	print("Else: Passo 6")

#### Passo 7: Download
download_url = 'http://localhost:3001/images/1616115087397_16360.png'

download = download_url.split('/')[-1]

down = requests.get(download_url)

if down.status_code >= 200 and down.status_code <= 299:
	print(f"Status Code {down.status_code}")
	print(f"Reason: {down.reason}")
	#print(f"Texto: {nfoto.text}")
	#print(f"JSON: {down.json()}")

	with open(download, 'wb') as pic:
		pic.write(down.content)

	print("Passo 7")
else:
	#Erros
	print(f"Status Code {down.status_code}")
	print(f"Reason: {down.reason}")
	#print(f"Texto: {down.text}")
	#print(f"JSON: {down.json()}")
	print("Else: Passo 7")