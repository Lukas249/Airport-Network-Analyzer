from src.database.session.index import SessionDB
from src.graph.airports import Airports
from src.graph.airports_connections import AirportsConnections
from src.graph.visualize.graph_visualize_arc import GraphVisualizeARC


def display_list_of_connections():
    airports: Airports = SessionDB.get("airports")
    connections: AirportsConnections = SessionDB.get("connections")

    for from_airport_id, connected_airports in connections.get_airports_connections().items():
        print(f"{from_airport_id}: ")
        for to_airport_id in connected_airports:
            print(f"{from_airport_id} -> {to_airport_id}", end=" | ")
        print()

    visualize = input("Visualize connections (t/n): ")

    if visualize == "t":
        GraphVisualizeARC.visualize_airports_connections(airports, connections)

