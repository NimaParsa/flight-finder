from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
print(sheet_data)


flight_search = FlightSearch()
for items in sheet_data:
    c = items["city"]
    print(items["city"])
    iata_data = flight_search.get_city_code(c)
    iata_code = iata_data[0]["id"]

    flight_data = flight_search.get_flights(iata_code)
    found_price = flight_data[0]["price"]
    print(found_price)
    if found_price < items['lowestPrice']:
        notification_manager = NotificationManager()
        city_name = flight_data[0]["cityTo"]
        iata = flight_data[0]["flyTo"]
        date = flight_data[0]["local_departure"]
        notification_manager.telegram_bot_sendtext(price=found_price, city_name=city_name, iata=iata, date=date)

    items["iataCode"] = iata_code

    # if
    # data_manager.destination_data = sheet_data
    # data_manager.update_destination_codes()
