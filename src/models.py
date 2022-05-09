from datetime import datetime
import csv


class Hotel:
    def __init__(self, name, classification):
        self.name = name
        self.classification = classification
        self.prices = Price(hotel_name=self.name)
    
    def get_costs(self, client):
        """
        Calculates the stay costs for a client.
        client: object of type Client()
        returns: float
        """
        weekdays_count = 0
        weekend_days_count = 0
        
        # Count week and weekend days
        for string in client.stay_dates:
            date = datetime.strptime(string, "%d%b%Y")
            if date.weekday() == 5 or date.weekday() == 6:
                weekend_days_count += 1
            else:
                weekdays_count += 1
        
        # Check client type
        if client.type == "Rewards":
            weekday_costs = weekdays_count * self.prices.discounted_weekday
            weekend_costs = weekend_days_count * self.prices.discounted_weekend
        else:
            weekday_costs = weekdays_count * self.prices.weekday
            weekend_costs = weekend_days_count * self.prices.weekend
    
        total_costs = weekday_costs + weekend_costs
        return total_costs


class Price:
    def __init__(self, hotel_name):
        # Get price data for a hotel from csv
        price_data = None
        with open("src/tables/prices.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if hotel_name == row["hotel_name"]:
                    price_data = row
                    break
        
        # Declare attributes
        self.hotel_name = price_data["hotel_name"]
        self.weekday = float(price_data["weekday"])
        self.weekend = float(price_data["weekend"])
        self.discounted_weekday = float(price_data["discounted_weekday"])
        self.discounted_weekend = float(price_data["discounted_weekend"])


class Client:
    def __init__(self, type, stay_dates):
        self.type = type
        self.stay_dates = stay_dates
