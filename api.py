import requests
import json

url =  "https://api.thecatapi.com/v1/images/search?limit=10"

a = requests.get(url)
data = a.json()

for urls in data:
  print(urls['url'])