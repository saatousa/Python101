import requests
from pprint import pprint

# Sheety:
USER_NAME = "51f2c3eacf2fc89bf61017cde66b322e"
PROJECT_NAME = "myFlightDeals"
PRICES_ENDPOINT_NAME = "prices"

APP_ID = "8e461890"
SHEET_API_KEY = "93362516b01b78ca84b86b46c1e3b014"
SHEET_ENDPOINT = f"https://api.sheety.co/{USER_NAME}/{PROJECT_NAME}"

sheet_headers = {
    "x-app-id": APP_ID,
    "x-app-key": SHEET_API_KEY,
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destinations_data = {}
        self.costumer_data = {}

    def get_destinations_data(self):
        sheet_response = requests.get(url=f"{SHEET_ENDPOINT}/{PRICES_ENDPOINT_NAME}", headers=sheet_headers)
        self.destinations_data = sheet_response.json()["prices"]

        # pprint(self.destinations_data)
        return self.destinations_data

    def update_destination_codes(self):
        # row_id = 2
        for city in self.destinations_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }

            response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}", headers=sheet_headers, json=new_data)
            print(response.text)

    def get_costumer_emails(self):
        response = requests.get(url=f"{SHEET_ENDPOINT}/users", headers=sheet_headers)
        self.costumer_data = response.json()["users"]
        return self.costumer_data
