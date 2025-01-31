from src.database.session.index import SessionDB
from src.graph.airports import Airports
from src.graph.airports_connections import AirportsConnections
from src.graph.graph import AirportGraph, WeightKeys
from src.graph.visualize.graph_visualize_arc import GraphVisualizeARC
from src.menu.input_queries.airport_connection.index import get_weight_key
from src.menu.manage_airport_network.delete.airport import get_airport_id


def display_find_shortest_path_menu():

    airports: Airports = SessionDB.get("airports")
    connections: AirportsConnections = SessionDB.get("connections")

    source = get_airport_id("Enter source airport ID: ", airports)
    destination = get_airport_id("Enter destination airport ID: ", airports)
    weight = get_weight_key(
        "Choose the weight for the shortest path calculation: ",
        ["1. Flight cost", "2. Flight time"],
        {
            "1": WeightKeys.FLIGHT_COST_CENTS,
            "2": WeightKeys.FLIGHT_DURATION_MINUTES
        }
    )

    graph = AirportGraph(airports, connections)
    shortest_path = graph.shortest_path(source, destination, weight)

    if len(shortest_path) == 0:
        print("There is no path")
        return

    path: list[str] = shortest_path["path"]
    value: list[str] = shortest_path[weight.value]

    print("Path: ")
    print(" -> ".join(path))
    print(f"{weight.value}: {value}")

    visualize = input("Visualize path (t/n): ")

    if visualize == "t":
        GraphVisualizeARC.visualize_path(airports, connections, path)
