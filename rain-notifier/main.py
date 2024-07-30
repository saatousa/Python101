import os
import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = ""
account_sid = ""
auth_token = ""


weather_params = {
    "lat": 35.689198,
    "lon": 51.388973,
    "appid": api_key,
    "exclude": "current,minutely,daily,",
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its going to rain today. Remember to bring an umbrella",
        from_='+17086690263',
        to='to a verified number on twilio +989..'
    )

print(message.status)





