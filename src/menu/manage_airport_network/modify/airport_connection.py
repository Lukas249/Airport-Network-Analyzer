from src.database.session.index import SessionDB
from src.graph.airport_connection import AirportConnection
from src.graph.airports_connections import AirportsConnections
from src.menu.input_queries.airport_connection.index import get_connection_source_airport_id, get_flight_duration, \
    get_flight_cost, get_connection_destination_airport_id


def modify_airport_connection_menu():
    connections: AirportsConnections = SessionDB.get("connections")

    source_airport_id = get_connection_source_airport_id("Enter source airport ID: ", connections)
    destination_airport_id = get_connection_destination_airport_id("Enter destination airport ID: ", source_airport_id, connections)

    connection_data = [
        get_flight_duration("Enter new flight duration in minutes: "),
        get_flight_cost("Enter new flight cost in cents: ")
    ]

    if connections.modify_connection(AirportConnection(source_airport_id, destination_airport_id, *connection_data)):
        print("Airport connection successfully modified")
    else:
        print("Something went wrong")