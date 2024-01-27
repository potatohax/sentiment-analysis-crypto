import os
import requests
import sentiment_analysis as sa
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("myapi")
req_url = os.environ.get("request_url")

req = requests.get(req_url)
title = len(req.json()["results"][0]["title"])

result = sa.analyze_text(title)

print(title)





