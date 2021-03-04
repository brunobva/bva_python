import csv, os slack

#read csv with ip addresses
with open(r'test.csv') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    new_list = list(reader)
    output = ''

    #loop through csv list
    for row in new_list:
        ip_addr = row[0]
        #ping each server
        resp = os.system("ping -c 2 " + ip_addr)
        if resp == 0:
            output += ip_addr + ', is up! \n'
        else:
            output += ip_addr + ', is down! \n'

#open csv for writing
with open('output.csv'),'w', newline='') as fd:
    fd.write(output)

#define parameters for slack
url = 'link da api do slack'
headers = { 
    'Content-Type': "application/json",
    'cache-control:' "no-cache"
}

#call slack function
slack.slack('output.csv'),url,hearders)