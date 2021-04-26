import sqlite3
import subprocess

# conn = sqlite3.connect('dev.db')
# cursor = conn.cursor()
# sql = '''CREATE TABLE disk_info (
#     HOSTNAME char(20) NOT NULL,
#     NFS CHAR(100),
#     "TAMANHO TOTAL(KB)" CHAR(12),
#     "UTILIZADO(KB)" CHAR(12),
#     "LIVRE(KB)" CHAR(12),
#     "% UTILIZADO" CHAR(4),
#     MOUNT POINT CHAR(100)
# )'''
# cursor.execute(sql)
# print(sql)
# add_vals = '''INSERT INTO disk_info(
#    HOSTNAME, NFS, TAMANHO TOTAL(KB)", "UTILIZADO(KB)", "LIVRE(KB)", "% UTILIZADO", MOUNT POINT
#     ) VALUES
#    (%s, %s, %s, %s, %s, %s, %s)'''
    
# cursor.execute(add_vals,)
# conn.commit()
# conn.close()

#cmd = "hostname && df -kT |awk '{print $1,$3,$4,$5,$6,$7}' |sed 's/ \+/,/g'|egrep -v 'tmpfs|sda|nfs|vda|root'"
res = subprocess.getoutput("df -kT |awk '{print $1,$3,$4,$5,$6,$7}' |sed 's/ \+/,/g'|egrep -v 'tmpfs|sda|nfs|vda|root'")
host = subprocess.getoutput("hostname")
list = res.split(",")
nfs = list[1]
#print(f"O espaço detalhado é: {list}")
print(f"O espaço do {host}: Tem o NFS:{nfs}")
