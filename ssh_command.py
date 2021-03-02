import paramiko, csv, os

hosts = ''
user = 'root'
passwd = ''


def ssh_connect(command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hosts, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    #ssh.close()
    result = stdout.readlines()
    return result

#cmd = ssh_connect("df -k |sed 's/ \+/,/g'")
cmd = ssh_connect("df -kT |awk '{print $1,$3,$4,$5,$6,$7}' |sed 's/ \+/,/g'")
saida = [i.strip("\n").split(",") for i in cmd[1:]]
saida = [i.strip("\r").split(",") for i in cmd[1:]]
#print(saida)

with open('bases_space_info_{}.csv'.format(hosts), 'w', newline="") as new_file:
    csv_writer = csv.writer(new_file, delimiter=',')
#    csv_writer = csv.writer(new_file)
    csv_writer.writerow(['Nome do NFS', 'Tamanho Total(KB)', 'Utilizado(KB)', 'Livre(KB)', '% Utilizado', 'Ponto de Montagem'])
    for line in saida:
        csv_writer.writerow(line)
