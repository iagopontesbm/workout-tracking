import requests
import os
from datetime import datetime

# Variáveis do ambiente
NUTRITIONIX_API_ID = os.getenv("NUTRITIONIX_API_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
SHEET_BEARER_KEY = os.getenv("SHEET_BEARER_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

# Endipoints APIs
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = SHEETY_ENDPOINT

# Header NUTRITIONIX API
headers = {
    "x-app-id": NUTRITIONIX_API_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0"
}

exercise = input("Informe a atividade realizada: ")

# Informação enviada para NUTRITIONIX
exercise_data = {
    "query": exercise,  # Atividade executada
    "gender": "male",  # Gênero
    "weight_kg": 68,  # Peso
    "height_cm": 180,  # Altura
    "age": 30  # Idade
}

# POST e retorno informações NUTRITIONIX
response = requests.post(exercise_endpoint, exercise_data, headers=headers)
response_data = response.json()["exercises"][0]

today = datetime.today()

# Informações enviada para SHEET
sheet_data = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.time().strftime("%X"),
        "exercise": response_data["name"].title(),
        "duration": response_data["duration_min"],
        "calories": response_data["nf_calories"]
    }
}

# Header SHEET API -- https://stackoverflow.com/questions/29931671/making-an-api-call-in-python-with-an-api-that-requires-a-bearer-token
sheet_headers = {
    "Authorization": f"Bearer {SHEET_BEARER_KEY}"
}

sheet_response = requests.post(url=sheet_endpoint, json=sheet_data, headers=sheet_headers)

print(sheet_response.text)
