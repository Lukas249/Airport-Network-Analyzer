from src.database.session.index import SessionDB
from src.graph.airports import Airports
from src.graph.airports_connections import AirportsConnections
from src.graph.graph import AirportGraph


def display_strongly_connected_components():

    airports: Airports = SessionDB.get("airports")
    connections: AirportsConnections = SessionDB.get("connections")

    graph = AirportGraph(airports, connections)
    strongly_connected_components = graph.strongly_connected_components()

    components = [[] for _ in range(strongly_connected_components["components_count"])]

    for airport_id, component_id in strongly_connected_components["components"].items():
        components[component_id].append(airport_id)

    for i in range(len(components)):
        component = components[i]
        print(f"Component {i + 1}:")
        print(", ".join(component))
