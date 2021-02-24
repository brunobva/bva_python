import paramiko

address = '45.77.18.220'
username = 'root'
passwd = '}1qA7Kt.!Sf},eNh'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=address, username=username, password=passwd)
stdin, stdout, stderr = ssh.exec_command('ifconfig')
stdin.close()
interface = []
for line in stdout.readlines():
    result = line.replace('\n', '')
    if 'mtu' in line:
        interface_name = result.split(':')[0]
        interface.append(interface_name)
ssh.close()
print(interface)