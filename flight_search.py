import requests
from datetime import datetime, timedelta

TEQUILA_API = "JzoRPtWDsNzSQKahmDAkfC-cPfQm1c_W"
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQUILA_ENDPOINT_Location = "https://api.tequila.kiwi.com/locations/query"

RANGE = 6
START_CITY = "airport:IST"

today = datetime.now()
date_today = today.strftime("%d/%m/%Y")
six_days_ahead = today + timedelta(days=6)
six_days_date = six_days_ahead.strftime("%d/%m/%Y")


class FlightSearch:
    def __init__(self):
        self.flight_data = {}
        self.flight_location = {}

    def get_flights(self, iata):
        self.parameters = {
            "fly_from": START_CITY,
            "fly_to": iata,
            "date_from": date_today,
            "date_to": six_days_date,
            "limit": 1,
            "flight_type": "oneway",
            "max_stopovers": 0,
        }
        self.headers = {
            "apikey": TEQUILA_API,
            "accept": "application/json",
        }
        response = requests.get(url=TEQUILA_ENDPOINT, params=self.parameters, headers=self.headers)
        response.raise_for_status()
        self.flight_data = response.json()
        return self.flight_data["data"]

    def get_city_code(self, city):
        self.parameters2 = {
            "term": city,
            "location_types": "airport",
            "limit": 2,
        }
        self.headers2 = {
            "apikey": TEQUILA_API,
            "accept": "application/json",
        }
        response2 = requests.get(url=TEQUILA_ENDPOINT_Location, params=self.parameters2, headers=self.headers2)
        response2.raise_for_status()
        self.flight_location = response2.json()
        return self.flight_location["locations"]
