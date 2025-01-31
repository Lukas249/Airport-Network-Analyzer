from src.graph.airports import Airports
from src.menu.input_queries.index import get_input


def get_new_airport_id(prompt_message: str, airports: Airports) -> str:
    airport_id = get_input(prompt_message)

    while len(airport_id) <= 2 or airports.exists(airport_id):
        print("Airport ID must be unique and consist of at least 3 characters.")
        airport_id = get_input(prompt_message)

    return airport_id

def get_airport_id(prompt_message:str, airports: Airports) -> str:
    source_airport_id = get_input(prompt_message)

    while not airports.exists(source_airport_id):
        print("The airport ID does not exist")
        source_airport_id = get_input(prompt_message)

    return source_airport_id

def get_longitude(prompt_message: str) -> float:
    longitude = get_input(prompt_message)

    display = True

    while display:
        try:
            longitude = float(longitude)

            if not -180 <= longitude <= 180:
                raise Exception()

            display = False
        except:
            print("Value must be between -180 and 180")
            longitude = get_input(prompt_message)

    return longitude


def get_latitude(prompt_message: str) -> float:
    latitude = get_input(prompt_message)

    display = True

    while display:
        try:
            latitude = float(latitude)

            if not -90 <= latitude <= 90:
                raise Exception()

            display = False
        except:
            print("Value must be between -90 and 90")
            latitude = get_input(prompt_message)

    return latitude