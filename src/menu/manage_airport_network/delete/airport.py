from src.database.session.index import SessionDB
from src.graph.airports import Airports
from src.graph.airports_connections import AirportsConnections
from src.menu.input_queries.airport.index import get_airport_id


def delete_airport_menu():

    airports: Airports = SessionDB.get("airports")
    connections: AirportsConnections = SessionDB.get("connections")

    airport_id = get_airport_id("Enter the airport ID to delete: ", airports)

    if airports.delete(airport_id) and connections.delete_airport(airport_id):
        print("Airport successfully deleted")
    else:
        print("Something went wrong")