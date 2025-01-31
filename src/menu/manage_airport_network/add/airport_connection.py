from src.database.session.index import SessionDB
from src.graph.airport_connection import AirportConnection
from src.graph.airports import Airports
from src.graph.airports_connections import AirportsConnections
from src.menu.input_queries.airport.index import get_airport_id
from src.menu.input_queries.airport_connection.index import get_flight_duration, get_flight_cost


def add_airport_connection_menu():

    airports: Airports = SessionDB.get("airports")
    connections: AirportsConnections = SessionDB.get("connections")

    connection_data = [
        get_airport_id("Enter source airport ID: ", airports),
        get_airport_id("Enter destination airport ID: ", airports),
        get_flight_duration("Enter flight duration in minutes: "),
        get_flight_cost("Enter flight cost in cents: ")
    ]

    if connections.add_connection(AirportConnection(*connection_data)):
        print("Airport connection successfully added")
    else:
        print("Something went wrong. Airport connection might already exist.")