from django.shortcuts import render
import newsapi

# Create your views here.
from newsapi.newsapi_client import NewsApiClient


def index(request):
    # init
    newsapi = NewsApiClient(api_key='3e83d44300aa47ef9eb376c1ca787d9b')

    # top headlines of tuchcrunch
    top = newsapi.get_top_headlines(sources='bbc-news,the-verge')

    # getting only articels
    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'index.html', context={"mylist": mylist})
