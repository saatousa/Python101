import requests
from datetime import timedelta, datetime
from flight_data import FlightData
import pprint

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "S_bITvN2YX4VRC3wv2yWzeYsnG4wzruQ"



headers = {
    "apikey": TEQUILA_API_KEY,
}
six_months_from_today = 6 * 30
tomorrow = datetime.now() + timedelta(days=1)
six_month_time_period = tomorrow + timedelta(days=six_months_from_today)


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):
        query = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=query, headers=headers)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):

        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "curr": "GBP",
            "max_stopovers": 0
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=query, headers=headers)
        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query)
            data = response.json()["data"][0]
            pprint(data)

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
                )
            return flight_data

        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
            )
            return flight_data

