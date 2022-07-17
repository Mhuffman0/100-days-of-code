import os
import requests
from datetime import datetime
from dotenv import load_dotenv

GENDER = "male"
WEIGHT_KG = 103
HEIGHT_CM = 175.26
AGE = 30
####################################
load_dotenv()

request_dict = {
    "get": requests.get,
    "post": requests.post,
    "delete": requests.delete,
    "put": requests.put,
}


def make_request(
    request_type: str = "post",
    url: str = None,
    params: dict = None,
    data: dict = None,
    json: dict = None,
    headers: dict = None,
) -> dict:
    request_type = request_dict[request_type]
    response = request_type(
        url=url, params=params, data=data, json=json, headers=headers
    )
    response.raise_for_status()
    return response.json()


def make_nutritonix_request(user_exercise: str):
    nutritonix_headers = {
        "x-app-id": os.environ.get("NUTRITIONIX_APP_ID"),
        "x-app-key": os.environ.get("NUTRITIONIX_API_KEY"),
    }

    nutritonix_data = {
        "query": user_exercise,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
    }

    return make_request(
        url="https://trackapi.nutritionix.com/v2/natural/exercise",
        headers=nutritonix_headers,
        data=nutritonix_data,
    )


def make_sheety_request(request_type: str = "post", workout_data: dict = None):
    now = datetime.now()
    sheety_headers = {
        "Authorization": os.environ.get("SHEETY_AUTHORIZATION"),
    }
    for workout in workout_data["exercises"]:
        print(workout)
        sheety_data = {
            "workout": {
                "date": now.strftime("%d/%m/%Y"),
                "time": now.strftime("%X"),
                "exercise": workout["name"].title(),
                "duration": workout["duration_min"],
                "calories": workout["nf_calories"],
            }
        }
        print(make_request(
            request_type=request_type,
            json=sheety_data,
            url="https://api.sheety.co/a0b700de5ada17cb2d20a8f5580a4735/myWorkouts/workouts",
            headers=sheety_headers,
        ))


user_exercise = input("What was your workout?\n").lower()
# user_exercise = "walked for 10 seconds then ran for 50 minutes"
workout_data = make_nutritonix_request(user_exercise)
make_sheety_request(
        request_type="post", workout_data=workout_data
)
