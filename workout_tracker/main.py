import os

import requests
from dotenv import load_dotenv

load_dotenv()

request_dict = {
    "get": requests.get,
    "post": requests.post,
    "delete": requests.delete,
    "put": requests.put,
}

nutritonix_headers = {
    "x-app-id": os.environ.get("NUTRITIONIX_APP_ID"),
    "x-app-key": os.environ.get("NUTRITIONIX_API_KEY"),
}

user_exercise = input("What was your workout?\n")
nutritonix_data = {
    # "query": "rowed 10 kilometers in 1 hour",
    "query": user_exercise,
    "gender": "male",
    "weight_kg": "103",
    "height_cm": "175.26",
    "age": 30,
}
response = requests.post(
    url="https://trackapi.nutritionix.com/v2/natural/exercise",
    headers=nutritonix_headers,
    data=nutritonix_data,
)
print(response.json())
