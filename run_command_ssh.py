import paramiko

address = '45.77.18.220'
user = 'root'
passwd = 

def ssh_connect(command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=address, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    #ssh.close()
    result = stdout.readlines()
    return result

check_status = ssh_connect('systemctl status docker')
if check_status:
    for line in check_status:
        result = line.replace('\n','')
        if 'Active' in line and 'running' in line:
            print(f'Serviço do Docker ok')
        elif 'Active' in line and 'running' not in line:
            print(f'Serviço Docker está parado')
            print(f'iniciando o serviço')
            start = ssh_connect('systemctl restart docker && systemctl status docker')
            for line in start:
                if 'Active' in line and 'running' in line:
                    print(f'Serviço está ok!')
                elif 'Active' in line and 'running' not in line:
                    print(f'Serviço está parado')

