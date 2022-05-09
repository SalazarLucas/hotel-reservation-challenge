from unittest import TestCase
from context import src
from src.my_module import get_cheapest_hotel
from src.helpers import parse_client_data, get_all_hotels
from src.models import Hotel, Price, Client

class MyTest(TestCase):
    def test1(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    def test2(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test3(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))
    
    def test_parse_client_data_1(self):
        result = {
            "type": "Regular",
            "stay_dates": ["16Mar2009", "17Mar2009", "18Mar2009"]
        }
        self.assertEqual(result, parse_client_data("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    def test_parse_client_data_2(self):
        result = {
            "type": "Regular",
            "stay_dates": ["20Mar2009", "21Mar2009", "22Mar2009"]
        }
        self.assertEqual(result, parse_client_data("Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test_parse_client_data_3(self):
        result = {
            "type": "Rewards",
            "stay_dates": ["26Mar2009", "27Mar2009", "28Mar2009"]
        }
        self.assertEqual(result, parse_client_data("Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))
    
    def test_get_all_hotels(self):
        hotel_names = ["Lakewood", "Bridgewood", "Ridgewood"]
        is_hotel_stored = all([hotel.name in hotel_names for hotel in get_all_hotels()])
        self.assertTrue(is_hotel_stored)
