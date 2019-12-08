from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import requests,random
#import numpy as np 
#import pandas as pd 
#import matplotlib.pyplot as plt 
  
#from sklearn.cluster import DBSCAN 
#from sklearn.preprocessing import StandardScaler 
#from sklearn.preprocessing import normalize 
#from sklearn.decomposition import PCA 
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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

    max_time=0
    if request.GET["type"] == "1":

        for i in request.GET.keys():
            max_time = max(int(request.GET[i]),max_time)
            print(max_time)

        if int(max_time) <= 30*60:
            print(dataForMaleP)
            print("hey",request.GET["type"])
            per_category = (no_of_new_articles)//len(dataForMaleP) + 1
            for x in dataForMaleP:
                print(x)
                response = requests.get(base_url.format(x,api_key))
                allNew = response.json()['articles']
                for n in range(per_category):
                    num = random.randrange(1, len(allNew))
                    news.append(allNew[num])

        else:
            print("hey",request.GET["type"])
            per_category = (no_of_new_articles)//len(dataForMaleN) + 1
            print(dataForMaleN)
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

"""
def predictSentiment(request):
    desc = request.GET("description")
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(desc)
    if sentiment_dict['compound'] >= 0.5 : 
        return "Positive" 
    elif sentiment_dict['compound'] <= - 0.5 : 
        return "Negative" 
    else : 
        return "Neutral"

def predictAnalogousBehavior(request):
    df = pd.DataFrame(request.GET("dataframe"))
    db = DBSCAN(eps = 0.0375, min_samples = 50).fit(df)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool) 
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_  

    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0) 


"""
