from datetime import datetime
from .models import Hotel
import csv


def parse_client_data(client_data_input):
    """
    Parses a string containing a client type and stay dates.
    client_data_input: string
    returns: dictionary
    """
    # Parse input string
    input_arguments_list = client_data_input.split(":")
    client_type = input_arguments_list[0]
    raw_date_strings = input_arguments_list[1].split(",")
    formatted_date_strings = [string.strip().split("(")[0] for string in raw_date_strings]
    client_data = {
        "type": client_type.capitalize(),
        "stay_dates": formatted_date_strings
    }
    return client_data


def get_all_hotels():
    """
    Retrieves and instantiates all hotels from csv file.
    Returns: list of Hotel() objects
    """
    hotel_objects = []

    with open("src/tables/hotels.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["name"]
            classification = int(row["classification"])
            hotel_object = Hotel(name, classification)
            hotel_objects.append(hotel_object)

    return hotel_objects
