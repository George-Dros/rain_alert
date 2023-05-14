import requests
from twilio.rest import Client

endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "your api key goes here"
account_sid = "your account sid goes here"
auth_token = "your authorization token goes here"

parameters = {
    "lat": 00.000000,
    "lon": 00.000000,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}



response = requests.get(endpoint, params=parameters)
response.raise_for_status()

data = response.json()
hourly_data = data["hourly"]
hourly_slice = hourly_data[:12]

will_rain = False

for hour in hourly_slice:
    hour_data = hour["weather"]
    id = hour_data[0]["id"]
    if id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, bring an umbrella! ",
        from_="your free twillio phone number",
        to="your actual phone number"
    )

    print(message.status)