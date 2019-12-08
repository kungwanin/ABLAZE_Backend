from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import requests,random

behaviorTestingSet = ["rape","women-empowerment","women-defence","business"
,"sports","politics","entertainment"]

#resultTestSet = ["rape","women-empowerment","women-defence","business"
#,"sports","politics","entertainment"]

dataForMaleP = ["women-empowerment","business","politics","entertainment"]

dataForMaleN = ["women-empowerment"]

dataForFemale = ["women-empowerment","sports"]

no_of_new_articles = 7

api_key = "dbc8a478776349d38e84e14244524b68"
base_url = "https://newsapi.org/v2/everything?q={}&apiKey={}"

def index(request):
    news=[]

    if request.GET["type"] == "1":

        per_category = (no_of_new_articles)//len(behaviorTestingSet) + 1

        for x in behaviorTestingSet:
            response = requests.get(base_url.format(x,api_key))
            allNew = response.json()['articles']
            for n in range(per_category):
                num = random.randrange(1, len(allNew))
                news.append(allNew[num])
        #print(len(news))

    elif request.GET["type"] == "2":

        per_category = (no_of_new_articles)//len(dataForFemale) + 1

        for x in dataForFemale:
            response = requests.get(base_url.format(x,api_key))
            allNew = response.json()['articles']
            #print(dataForFemale)
            for n in range(per_category):
                num = random.randrange(1, len(allNew))
                news.append(allNew[num])

    return JsonResponse({"articles":news})

def training(request):
    news=[]

    if request.GET["type"] == "3":
        print("hey",request.GET["type"])
        per_category = (no_of_new_articles)//len(dataForMaleP) + 1
        for x in dataForMaleP:
            print(x)
            response = requests.get(base_url.format(x,api_key))
            allNew = response.json()['articles']
            for n in range(per_category):
                num = random.randrange(1, len(allNew))
                news.append(allNew[num])

    elif request.GET["type"] == "4":
        print("hey",request.GET["type"])
        per_category = (no_of_new_articles)//len(dataForMaleN) + 1

        for x in dataForMaleN:
            print(x)
            response = requests.get(base_url.format(x,api_key))
            allNew = response.json()['articles']
            for n in range(per_category):
                num = random.randrange(1, len(allNew))
                news.append(allNew[num])

    else:#female
        per_category = (no_of_new_articles)//len(dataForFemale) + 1

        for x in dataForFemale:
            print(x)
            response = requests.get(base_url.format(x,api_key))
            allNew = response.json()['articles']
            for n in range(per_category):
                num = random.randrange(1, len(allNew))
                news.append(allNew[num])

    return JsonResponse({"articles":news})