from src.database.session.index import SessionDB
from src.graph.airports_connections import AirportsConnections
from src.menu.input_queries.airport_connection.index import get_connection_source_airport_id, \
    get_connection_destination_airport_id


def delete_airport_connection_menu():
    connections: AirportsConnections = SessionDB.get("connections")

    source_airport_id = get_connection_source_airport_id("Enter source airport ID: ", connections)
    destination_airport_id = get_connection_destination_airport_id("Enter destination airport ID: ", source_airport_id, connections)

    if connections.delete_connection(source_airport_id, destination_airport_id):
        print("Airport connection successfully deleted")
    else:
        print("Something went wrong")