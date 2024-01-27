import os
import requests
import sentiment_analysis as sa
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

API_KEY = os.environ.get("myapi")
req_url = os.environ.get("request_url")

req = requests.get(req_url)

news_list = req.json()["results"]
title = len(req.json()["results"])
news_header = []
data = []
sentiment_score = []

#Traverse through entire news list and add data into lists
for i in range(len(news_list)):
    curr = news_list[i]["title"]
    print(curr)
    result = sa.analyze_text(curr)
    news_header.append(curr)
    data.append(result)
    sentiment_score.append(data[i][2] - data[i][0])
    
dict = {
    "header" : news_header,
    "sentiment_result" : data,
    "score" : sentiment_score
}
df = pd.DataFrame(data = dict)


print(df)
print("length:", len(df))
print(sum(df["score"])/len(df))






