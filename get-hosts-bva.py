import os, csv

class LerCsv:
    def __init__(self, ambiente='', hostname='', username='', password=''):

        self.ambiente = ambiente
        self.hostname = hostname
        self.username = hostname
        self.username = password

    
    #def file_hosts(self):
with open('hosts_lab.csv', 'r') as hosts:
    reader = csv.reader(hosts, delimiter=',')
    read = list(reader)
    output = ''
        
    for row in read:
        amb = row[0]
        host = row[1]
        usr = row[2]
        pwd = row[3]

    print(amb, host, usr, pwd)
    
