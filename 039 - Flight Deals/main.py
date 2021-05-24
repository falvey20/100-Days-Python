from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

today = datetime.now()
tomorrow = (today + timedelta(days=1)).strftime("%d/%m/%Y")
six_months = (today + timedelta(days=180)).strftime("%d/%m/%Y")

for destination in sheet_data:
    flight = flight_search.get_flight_prices(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_date=tomorrow,
        to_date=six_months
    )

    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from "
                    f"{flight.origin_city}-{flight.origin_airport} to "
                    f"{flight.destination_city}-{flight.destination_airport} "
                    f"from {flight.out_date} to {flight.return_date}"
        )


