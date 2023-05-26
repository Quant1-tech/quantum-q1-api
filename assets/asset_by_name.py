from os import environ


import requests
url = "https://quantum-q1-api.p.rapidapi.com/assets/by/name/{asset_name}"

payload={}
headers = {
    "X-RapidAPI-Key": environ.get('X_RapidAPI_Key'),
    "X-RapidAPI-Host": "quantum-q1-api.p.rapidapi.com",
    # Token de acesso do provedor Quantum.
    "Authorization": "Bearer " + environ.get('TOKEN')
}

response = requests.get(url, headers=headers)

print(response.text)