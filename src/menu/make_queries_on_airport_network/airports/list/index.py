from src.database.session.index import SessionDB
from src.graph.airports import Airports


def display_airports_list():
    airports: Airports = SessionDB.get("airports")
    airports_list = airports.get_airports_list()

    print(f"All airports: {", ".join(airports_list)}")