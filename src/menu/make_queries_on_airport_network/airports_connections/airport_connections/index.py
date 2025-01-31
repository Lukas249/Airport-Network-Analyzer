from src.database.session.index import SessionDB
from src.graph.airports import Airports
from src.graph.airports_connections import AirportsConnections
from src.menu.input_queries.airport.index import get_airport_id


def display_airport_connections():

    airports: Airports = SessionDB.get("airports")
    connections: AirportsConnections = SessionDB.get("connections")

    airport_id = get_airport_id("Enter an airport ID: ", airports)

    airport_connections = connections.get_airport_connections(airport_id)

    print(f"{airport_id} is connected with: ")
    for airport_id, connection_data in airport_connections.items():
        print(f"Airport ID: {airport_id}, Flight cost (cents): {connection_data.flight_cost_cents}, Flight duration (minutes): {connection_data.flight_duration_minutes}")
