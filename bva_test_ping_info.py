# import csv

# with open('hosts_lab.csv') as f:
#     read = csv.DictReader(f) #DictReader is used when the file has a header(title)

#     count = 0

#     for row in read:
#         print(row['Servidores']

#         if count > 5:
#             break
#         count += 1
############# 
# Exemplo 2
############# 
import csv
with open('hosts_lab.csv') as f:
    readCSV = csv.reader(f)
    server = []
    user = []
    passwd = []
    for row in readCSV:
    
        host = row[1]
        usr = row[2]
        pwd = row[3]
    
        server.append(host)
        user.append(usr)
        passwd.append(pwd)

    print('Servidor: ',server[2],'com o usuário: ',user[2],'está com a senha: ',passwd[2])
