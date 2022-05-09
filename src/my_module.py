from .helpers import parse_client_data, get_all_hotels
from .models import Hotel, Client


def get_cheapest_hotel(number):   #DO NOT change the function's name
    """
    Gets the name of the cheapest hotel given some dates.
    number: string of dates and client type
    returns: the string name of a hotel
    """
    data = parse_client_data(number)
    client = Client(type=data["type"], stay_dates=data["stay_dates"])
    hotels = get_all_hotels()
    cheapest_hotel = None

    for hotel in hotels:
        if not cheapest_hotel:
            cheapest_hotel = hotel

        costs = hotel.get_costs(client)
        classification = hotel.classification

        if costs <= cheapest_hotel.get_costs(client) and classification > cheapest_hotel.classification:
            cheapest_hotel = hotel

    return cheapest_hotel.name
