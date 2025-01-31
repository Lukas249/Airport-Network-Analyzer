from src.database.session.index import SessionDB
from src.graph.airports import Airports
from src.graph.airports_connections import AirportsConnections
from src.graph.graph import AirportGraph
from src.menu.input_queries.airport.index import get_airport_id


def display_is_airport_directly_connected_menu():
    airports: Airports = SessionDB.get("airports")
    connections: AirportsConnections = SessionDB.get("connections")

    source_airport_id = get_airport_id("Enter the source airport ID:", airports)
    destination_airport_id = get_airport_id("Enter the destination airport ID:", airports)

    graph = AirportGraph(airports, connections)
    is_directly_connected = graph.is_directly_connected(source_airport_id, destination_airport_id)

    print(f"{source_airport_id} {"is" if is_directly_connected else "isn't" } directly connected with {destination_airport_id}")