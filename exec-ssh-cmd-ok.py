import paramiko, csv

command = 'uptime ; uname -a'

with open ('devops_hosts.csv', 'r') as d:
    read = csv.reader(d)
    hosts = list(read)

    for h in hosts:
        server = []
        user = []
        passwd = []
    for host in hosts:
            server = host[1]
            user = host[2]
            passwd = host[3]
    
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=server, username=user, password=passwd)
            stdin, stdout, stderr = ssh.exec_command(command)
            stdin.close()
            #ssh.close()
            result = stdout.readlines()
            print(f"The server {server} runned the command {result} as properly.")
