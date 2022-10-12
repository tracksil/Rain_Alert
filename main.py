import requests
from twilio.rest import Client

API_KEY = API_KEY
LAT = "47.040983"
LON = "28.771651"

account_sid = account_sid
auth_token = auth_token

params = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

request = requests.get("https://api.openweathermap.org/data/2.5/onecall?", params=params)
request.raise_for_status()
whether_data = request.json()


whether_slice = whether_data["hourly"][:12]

will_rain = False

for hour_data in whether_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="Bring an umbrella! It's going to rain today.",
                                     from_=from_,
                                     to=me)
