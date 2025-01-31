from src.graph.airports_connections import AirportsConnections
from src.graph.graph import WeightKeys
from src.menu.input_queries.index import get_input


def get_connection_source_airport_id(prompt_message: str, connections: AirportsConnections) -> str:
    source_airport_id = get_input(prompt_message)

    while not connections.exists_source_airport(source_airport_id):
        print("No connection exists with the source airport ID")
        source_airport_id = get_input(prompt_message)

    return source_airport_id

def get_connection_destination_airport_id(prompt_message: str, source_airport_id: str, connections: AirportsConnections) -> str:
    destination_airport_id = get_input(prompt_message)

    while not connections.exists_connection(source_airport_id, destination_airport_id):
        print("No connection exists with the destination airport ID")
        destination_airport_id = get_input(prompt_message)

    return destination_airport_id

def get_flight_duration(prompt_message: str) -> int:
    flight_duration = get_input(prompt_message)

    display = True

    while display:
        try:
            flight_duration = int(flight_duration)

            if flight_duration < 0:
                raise Exception()

            display = False
        except:
            print("Invalid flight duration. It must be a positive integer")
            flight_duration = get_input(prompt_message)

    return flight_duration

def get_flight_cost(prompt_message: str) -> int:
    flight_cost = get_input(prompt_message)

    display = True

    while display:
        try:
            flight_cost = int(flight_cost)

            if flight_cost < 0:
                raise Exception()

            display = False
        except:
            print("Invalid flight cost. It must be a positive integer")
            flight_cost = get_input(prompt_message)

    return flight_cost

def get_weight_key(prompt_message: str, menu_options: list[str], weight_options: dict[str, WeightKeys]) -> WeightKeys:
    for option in menu_options:
        print(option)

    option = input(prompt_message)

    while option not in weight_options:
        option = input(prompt_message)

    return weight_options[option]