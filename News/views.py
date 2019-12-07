from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import requests,random

behaviorTestingSet = ["rape","women-empowerment","women-defence","business"
,"sports","politics","entertainment"]

resultTestSet = ["rape","women-empowerment","women-defence","business"
,"sports","politics","entertainment"]


api_key = "dbc8a478776349d38e84e14244524b68"
base_url = "https://newsapi.org/v2/everything?q={}&apiKey={}"

def index(request):
    news=[]

    for x in behaviorTestingSet:
        response = requests.get(base_url.format(x,api_key))
        allNew = response.json()['articles']
        num = random.randrange(1, len(allNew))
        news.append(allNew[num])

    return JsonResponse({"articles":news})

def training(request):
    news=[]

    for x in behaviorTestingSet:
        response = requests.get(base_url.format(x,api_key))
        allNew = response.json()['articles']
        num = random.randrange(1, len(allNew))
        news.append(allNew[num])

    return JsonResponse({"articles":news})