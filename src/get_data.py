import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("myapi")
print(API_KEY)