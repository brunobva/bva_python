import subprocess
# Criado por Bruno Moraes
# Created -- OK -- 25/03/2021
# Tested -- OK -- -- 25/03/2021

def ping(host):
    command = ['ping', host]
    return subprocess.call(command)

with open('hosts_ping.txt') as f:
    for hosts in f:
        ip = hosts.strip('\n')
        response = ping(ip)
        result = ('%s,%s \n' % (ip, response))