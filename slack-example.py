import requests, csv

#slack function, makes a POST request to Slack API
def slack(file,url, headers)
    #opencsv
    with open(file) as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        status_list = list(reader)
        status_list.pop(0)

    payload = ""
    for x in status_list:
        # print(x)
        payload += "".json(x)+'\n'
    
    data = '{\"text\":\"'+ payload +'\"}'

    return requests.requests("POST", url, data=data, headers=headers)
