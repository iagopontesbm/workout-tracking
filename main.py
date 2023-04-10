import requests
import os
from datetime import datetime

NUTRITIONIX_API_ID = os.getenv("NUTRITIONIX_API_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
SHEET_BEARER_KEY = os.getenv("SHEET_BEARER_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/1c8881ec505e12e09cd78b4c264b7242/myWorkouts/workouts"

headers = {
    "x-app-id": NUTRITIONIX_API_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0"
}

exercise_data = {
    "query": "swim 200 meters",
    "gender": "male",
    "weight_kg": 68,
    "height_cm": 180,
    "age": 30
}

response = requests.post(exercise_endpoint, exercise_data, headers=headers)
response_data = response.json()["exercises"][0]

print(response_data)

today = datetime.today()

sheet_data = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.time().strftime("%X"),
        "exercise": response_data["name"].title(),
        "duration": response_data["duration_min"],
        "calories": response_data["nf_calories"]
    }
}

sheet_headers = {
    "Authorization": f"Bearer {SHEET_BEARER_KEY}"
}

print(sheet_data)

sheet_response = requests.post(url=sheet_endpoint, json=sheet_data, headers=sheet_headers)

print(sheet_response.text)
