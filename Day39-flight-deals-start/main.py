from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

flight_search = FlightSearch()
data_manager = DataManager()
for city in data_manager.data:
    flights = flight_search.get_flights(ORIGIN_CITY_IATA, city["iataCode"])
    #flights2 = flight_search.get_flights_by_date_range(ORIGIN_CITY_IATA, city["iataCode"], city["lowestPrice"])
    #print("Flights by range", flights2)
    flight_data = FlightData(city)
    flight = flight_data.get_cheapest_flight(flights)
    if flight is None:
        pass
    elif flight_data.is_cheapest_flight_acceptable(flight):
        notification_manager = NotificationManager()
        notification_manager.send_notification(flight, city)
        print(f"Notification! Cheap flight {flight['price']['grandTotal']} met minimum {city['lowestPrice']}\n")
    else:
        print(f"Ignored. Cheap flight {flight['price']['grandTotal']} above threshold {city['lowestPrice']}\n")
