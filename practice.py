import requests
url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'apiKey=01619d6a528846528e9d4745b10271fe')
response = requests.get(url)
print(response.json()['articles'][0])