from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from datetime import timedelta, datetime

data_manager = DataManager()
sheet_data = data_manager.get_destinations_data()

flight_search = FlightSearch()
ORIGIN_CITY_IATA = flight_search.get_destination_code("London")

notification_manager = NotificationManager()

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destinations_data = sheet_data
    # data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6 * 30))


for destination in data_manager.destinations_data:
    flight = flight_search.check_flights(origin_city_code=ORIGIN_CITY_IATA,
                                         destination_city_code=destination["iataCode"],
                                         from_time=tomorrow,
                                         to_time=six_months_from_today)

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        users = data_manager.get_costumer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\n\nFlight has {flight.stop_overs}, via {flight.via_city}."

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        # notification_manager.send_mail(emails=emails, message=message)
        print(message)



