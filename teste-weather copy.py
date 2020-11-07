import requests

url = "https://rapidapi.p.rapidapi.com/weather"

cidade = input("Digite uma cidade: ")
querystring = {"q":"jacarei, br","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"\"metric\" or \"imperial\"","mode":"xml, html"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "0aef20368emsh70ddff03d7b5630p1bb9bfjsnc3d7a6922ac8"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)