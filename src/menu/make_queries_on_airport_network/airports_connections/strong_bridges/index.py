from src.database.session.index import SessionDB
from src.graph.airports import Airports
from src.graph.airports_connections import AirportsConnections
from src.graph.graph import AirportGraph
from src.graph.visualize.graph_visualize_arc import GraphVisualizeARC


def display_strong_bridges():
    airports: Airports = SessionDB.get("airports")
    connections: AirportsConnections = SessionDB.get("connections")

    graph = AirportGraph(airports, connections)
    critical_connections = graph.critical_connections()

    visualize = input("Visualize strong bridges (t/n): ")

    if visualize == "t":
        GraphVisualizeARC.visualize(airports, critical_connections)

