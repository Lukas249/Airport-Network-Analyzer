from src.database.session.index import SessionDB
from src.graph.airports import Airports
from src.graph.airports_connections import AirportsConnections
from src.graph.graph import AirportGraph


def display_highest_number_of_connections_menu():
    airports: Airports = SessionDB.get("airports")
    connections: AirportsConnections = SessionDB.get("connections")

    graph = AirportGraph(airports, connections)
    airport_highest_connections = graph.highest_connections_airports()

    print(f"Airports with highest number of connections: {", ".join(airport_highest_connections)}")