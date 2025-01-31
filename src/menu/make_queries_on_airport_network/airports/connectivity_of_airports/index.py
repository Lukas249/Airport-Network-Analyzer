from src.database.session.index import SessionDB
from src.graph.airport_connection import AirportConnection
from src.graph.airports import Airports
from src.graph.airports_connections import AirportsConnections
from src.graph.graph import AirportGraph
from src.graph.visualize.graph_visualize_arc import GraphVisualizeARC


def display_connectivity_of_airports_menu():
    airports: Airports = SessionDB.get("airports")
    connections: AirportsConnections = SessionDB.get("connections")

    graph = AirportGraph(airports, connections)
    connectivity = graph.connectivity()

    for airport, connected_airports in connectivity.items():
        print("-"*50)
        print(f"{airport} has connection to {", ".join(connected_airports) if len(connected_airports) else "no other airports"}")
        print("-"*50)

    visualize = input("Visualize connectivity (t/n): ")

    if visualize == "t":
        flight_list: list[AirportConnection] = []

        for airport, connected_airports in connectivity.items():
            for connected_airport in connected_airports:
                flight_list.append(AirportConnection(airport, connected_airport, 0, 0))

        GraphVisualizeARC.visualize_connectivity(airports, flight_list)