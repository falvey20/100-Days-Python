import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall" 
account_sid = "ACdb96d1a7631338653a2fa4df7b348861" # Free Acc
auth_token = "e5aec426dac4362e40b7cd0e9f39b7fe" # Free Acc

weather_params = {
    "lat": 50.7192,
    "lon": -1.8808,
    "appid": "1b4b9e5116acf31360a75cae598aee58",
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
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

    message = client.messages \
        .create(
        body="It's going to rain, bring an ☔️",
        from_="+18582270663",
        to="+447447502467"
    )
    print(message.status)


