from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime
from football_livescore.settings import API_KEY


# Create your views here.
def index(request):
    today = datetime.today().strftime('%Y-%m-%d')
    live_url = "https://apiv3.apifootball.com/?action=get_events&match_live=1&from="+today+"&to="+today+"&league_id=149&APIkey="+API_KEY
    url = "https://apiv3.apifootball.com/?action=get_events&from=" + today + "&to=" + today + "&league_id=149&APIkey=" + API_KEY
    live_response = requests.get(live_url)
    live_json_response = live_response.json()
    if "error" in live_json_response:
        response = requests.get(url)
        json_response = response.json()
    else:
        return render(request, 'blog/index.html', {'json_response': live_json_response})
    return render(request, 'blog/index.html', {'json_response': json_response})


def specific(request):
    A = [1, 2, 3, 4, 5]
    return HttpResponse(A)


def article(request,article_id):
    return render(request, 'blog/index.html')
