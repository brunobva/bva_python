import os
import csv


cmd = "df -k |sed 's/ \+/,/g'"
saida = subprocess.check_output(cmd)
#os.popen(cmd).readlines()
#os.system(df)

with open('bases_space_info.csv', 'w') as new_file:
    csv_writer = csv.writer(new_file, delimiter=',')

    for line in os.system(saida):
        csv_writer.writerow(line)
        
