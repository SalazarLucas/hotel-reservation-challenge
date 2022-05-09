from src.my_module import get_cheapest_hotel

if __name__ == "__main__":   
    try:
        input_string = str(input("Get cheapest hotel -> "))
        cheapest = get_cheapest_hotel(input_string)
        print(cheapest)
    
    except:
        print("Usage:")
        print("Input format:\n<client_type>: <date1>, <date2>, <date3>, ...\n")
        print("Output format:\n<cheapest_hotel_name>\n")
        print("Examples:")
        print('''
        Input 1:
        Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)
        Output 1:
        Lakewood''')
        print('''
        Input 2:
        Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)
        Output 2:
        Bridgewood''')
        print('''
        Input 3:
        Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)
        Output 3:
        Ridgewood''')
