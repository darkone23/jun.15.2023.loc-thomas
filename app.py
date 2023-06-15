import requests
import json

DATA_URL = "https://think.cs.vt.edu/corgis/datasets/json/airlines/airlines.json"
YEAR = 2005

def get_flight_year(item):
    return item["Time"]["Year"]

def get_flights_data(url):
    json_resp = requests.get(DATA_URL)
    item = json_resp.json()    
    # data = FlightsData() # create an opportunity for validation
    return item

def get_data_for_year(flights_data, year):
    year_data = []
    for flight in flights_data:
        if get_flight_year(flight) == 2005:
            year_data.append(flight)
    return year_data

def sum_total_flights(flights_data):
    sum = 0
    for flight in flights_data:
        total = flight["Statistics"]["Flights"]["Total"]
        sum += total
    return sum    
    
def sum_by_delay_reason(flights_data, delay_reason):
    sum = 0
    for flight in flights_data:
        delayed = flight["Statistics"]["# of Delays"][delay_reason]
        sum += delayed
    return sum

def main():
    flights_data = get_flights_data(DATA_URL)
    data_for_year = get_data_for_year(flights_data, YEAR)

    total_flights = sum_total_flights(data_for_year)
    delayed_for_aviation = sum_by_delay_reason(data_for_year, "National Aviation System")

    # if total_flights == 0:
    #     # divide by zero case
    percentage_delayed_for_aviation = delayed_for_aviation / total_flights

    print(percentage_delayed_for_aviation)

if __name__ == "__main__":
    main()
