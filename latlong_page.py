import requests
from datetime import datetime


url = "http://api.sunrise-sunset.org/json"
LAT = 60.194290
LONG = 24.956970

params = {
    'lat': LAT,
    'lng': LONG,
    'formatted': 0
}

response = requests.get(url=url, params=params)
response.raise_for_status()
data = response.json()

sunraise = data['results']['sunrise'].split('T')[1].split(':')[0]
time_now = datetime.now()

print(sunraise)
print(time_now.hour)
