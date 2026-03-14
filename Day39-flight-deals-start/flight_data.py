class FlightData:

    def __init__(self, city):
        self.city = city

    def get_cheapest_flight(self, flights):
        if len(flights) > 0:
            cheapest = flights[0]
            prices = [flight['price']['grandTotal'] for flight in flights]
            print("Prices", prices)
            for flight in flights:
                flight_price = float(flight["price"]["grandTotal"])
                if flight_price < float(cheapest["price"]["grandTotal"]):
                    cheapest = flight
            print("Cheapest", cheapest['price']['grandTotal'])
            return cheapest
        else:
            return None

    def is_cheapest_flight_acceptable(self, flight):
        return float(flight["price"]["grandTotal"]) <= float(self.city["lowestPrice"])

