from src.database.session.index import SessionDB
from src.graph.airport import Airport
from src.graph.airports import Airports
from src.graph.airports_connections import AirportsConnections
from src.menu.input_queries.airport.index import get_new_airport_id, get_longitude, get_latitude
from src.menu.input_queries.index import get_input

def add_airport_menu():

    airports: Airports = SessionDB.get("airports")
    connections: AirportsConnections = SessionDB.get("connections")

    airport_data = [
        get_new_airport_id("Enter the unique ID for the airport: ", airports),
        get_input("Enter the label or name of the airport: "),
        get_input("Enter the city where the airport is located: "),
        get_input("Enter the country where the airport is located: "),
        get_longitude("Enter the longitude of the airport: "),
        get_latitude("Enter the latitude of the airport: ")
    ]

    airports.add(Airport(*airport_data))
    connections.add_source_airport(airport_data[0])

    print("Airport successfully added")