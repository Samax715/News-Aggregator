from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'apiKey=01619d6a528846528e9d4745b10271fe')
    response = requests.get(url)
    headline_title = []
    headline_desc = []
    headline_url = []
    headline_images = []

    for i in range(1):
        headline_title.append(response.json()['articles'][i]['title'])
        headline_desc.append(response.json()['articles'][i]['description'])
        headline_url.append(response.json()['articles'][i]['url'])
        headline_images.append(response.json()['articles'][i]['urlToImage'])
    topheadline = zip(headline_title, headline_desc,headline_url,headline_images)
    context = {
            'topheadline': topheadline,
            }
    return render(request,'index.html',context)

def first(request):
    return render(request,'first.html')