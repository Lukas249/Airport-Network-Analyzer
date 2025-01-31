from src.database.session.index import SessionDB
from src.graph.airport import Airport
from src.graph.airports import Airports
from src.menu.input_queries.airport.index import get_longitude, get_latitude, get_airport_id
from src.menu.input_queries.index import get_input

def modify_airport_menu():

    airports: Airports = SessionDB.get("airports")

    airport_data = [
        get_airport_id("Enter the airport ID: ", airports),
        get_input("Enter new label or name of the airport: "),
        get_input("Enter new city where the airport is located: "),
        get_input("Enter new country where the airport is located: "),
        get_longitude("Enter new longitude of the airport: "),
        get_latitude("Enter new latitude of the airport: ")
    ]

    if airports.modify(Airport(*airport_data)):
        print("Airport successfully modified")
    else:
        print("Something went wrong")