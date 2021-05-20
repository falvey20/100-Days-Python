import os
import requests
from datetime import datetime


GENDER = "male"
WEIGHT_KG = 98
HEIGHT_CM = 200
AGE = 32

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
SHEETY_ENDPOINT = os.environ['SHEETY_ENDPOINT']
BEARER_HEADER = os.environ['BEARER_HEADER']

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me what exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)



now = datetime.now()
today_date = now.strftime("%d/%m/%Y")
current_time = now.strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {BEARER_HEADER}"
}

for exercise in result["exercises"]:
    sheety_params = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=bearer_headers)

    print(sheety_response)
