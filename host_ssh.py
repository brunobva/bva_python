# Ler lista de hosts de um arquivo;
import paramiko
fi = open(r'basis_hosts.txt')
ln = fi.readlines()

for line in ln:
    if line.strip() != '':
        print(line)


# h = [ln.rstrip('\n').rsplit(',') for ln in fi]
# print(h)
fi.close()
# linedict = dict([(no, line) for no, line in enumerate(fi.readlines())])
# print(linedict, end='')
    # if ln.startswith("PRD"):
    #     srv = (ln[0:])
    #     print(srv, end='')

    # host = read
    # print(host)
    
    # usr = 'vagrant'
    # passw = 'vagrant'
    # command: "df -kT |awk '{print $1,$3,$4,$5,$6,$7}' |sed 's/ \+/,/g'"

    #for h in read:
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname=host[1], username=usr, password=usr)
# stdin, stdout, stderr = ssh.exec_command(command)
# stdin.close()
# #ssh.close()
# result = stdout.readlines()
    
# rodar comandos até finalizar lista;
#cmd = ssh_connect("df -kT |awk '{print $1,$3,$4,$5,$6,$7}' |sed 's/ \+/,/g'")