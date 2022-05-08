from datetime import datetime


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
