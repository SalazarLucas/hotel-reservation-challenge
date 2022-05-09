# Hotel Reservation Problem

## About
This is a technical challenge for the Internship Program of [Digital Syngenta](https://www.syngentadigital.com.br/), where this project is supposed to solve the hotel reservation problem described bellow.

## The Hotel Reservation Problem
A hotel chain in Miami would like to offer an internet reservation service. The chain comprises three hotels: Lakewood, Bridgewood and Ridgewood. Each hotel has different rates for the weekday or weekend, including specific rates for loyalty program participants. Additionally, each hotel has a rating, indicating service excellence.

- Lakewood is rated 3 and its weekday rates are R$110 for regular customers and R$80 for loyalty program participants. Weekend rates are R$90 and R$80 respectively for regular customers and loyalty program participants.

- Bridgewood has a rating of 4 and its weekday rates are R$160 for regular customers and R$110 for loyalty program participants. Weekend rates are R$60 and R$50 respectively for regular customers and loyalty program participants.

- Ridgewood has a rating of 5 and its weekday rates are R$220 for regular customers and R$100 for loyalty program participants. Weekend rates are R$150 and R$40 respectively for regular customers and loyalty program participants.

The program is supposed to find the cheapest hotel out of those three. The program input is a sequence of dates for a customer participating or not in the loyalty program.

"Regular" refers to a regular customer and "Reward" to a customer participating in the loyalty program. The output will be the cheapest available hotel name and in the event of a tie, the hotel with the highest rating willmust be returned.

### Examples
```
Input 1:
Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)
Output 1:
Lakewood
```
```
Input 2:
Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)
Output 2:
Bridgewood
```
```
Input 3:
Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)
Output 3:
Ridgewood
```

## The solution

This project solves the problem by storing the hotels data into CSV files for the hotels and prices, then inside the ```src.my_module.get_cheapest_hotel``` function, this data will be instantiated to objects using the Python classes ```src.models.Hotel``` and ```src.models.Price```. 

The function ```get_cheapest_hotel```, using a helper function, will then parse a string from a user into a dictionary containing a client type and its stay dates, then this data will be used to instantiate an object of the class ```src.models.Client```.

Finally the ```get_cheapest_hotel``` function, using the Hotel method ```get_costs(<client_object>)```, will compare all the three hotels by price and classification, returning the cheapest hotel name with the highest classification possible.

ps: I couldn't write all tests because my models implementation made it very difficult to figure it out a way to write them in the time to meet the deadline 😅.

## How to run this project?
Clone this repository:
```
$ git clone https://github.com/SalazarLucas/hotel-reservation-challenge.git
```
Install the required dependencies:
```
$ pip install -r requirements.txt
```
or
```
$ pip3 install -r requirements.txt
```
Then get in the project directory and run the script that starts the program:
```
$ cd hotel-reservation-challenge
$ python cheapest_hotel.py
```

## How to run this project tests

After installing the dependencies, just:

```
$ py.test
```