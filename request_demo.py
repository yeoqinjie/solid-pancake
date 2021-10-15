import requests
import json

url = "https://covid-19-data.p.rapidapi.com/report/country/name"

querystring = {"name":"Malaysia","date":"2021-09-01"}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "96e378cea5msh261b20bbf9c9ba8p1d5686jsndec440cbf6f2"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

js = json.loads(response.text)
print(js[0]['provinces'][0]['province'])


