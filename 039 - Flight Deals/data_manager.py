import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/5957899adadb7f88faa33374bb792675/flightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
    # Get Sheety Data and assign to destination data.
    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # pprint formats json data in terminal.
        # pprint(data)
        return self.destination_data

    # Destination date is set from main.py
    # For each city the sheety iataCode is updated from the return from the Tequila Api.
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)


