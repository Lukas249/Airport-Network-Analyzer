from src.menu.make_queries_on_airport_network.airports_connections.airport_connections.index import \
    display_airport_connections
from src.menu.make_queries_on_airport_network.airports_connections.bridges_connecting_scc.index import \
    display_bridges_connecting_scc
from src.menu.make_queries_on_airport_network.airports_connections.list_of_connections.index import \
    display_list_of_connections
from src.menu.make_queries_on_airport_network.airports_connections.strong_bridges.index import display_strong_bridges
from src.menu.print_menu import print_menu


def display_make_queries_on_airport_connections_menu():
    display = True

    options = {
        "1": lambda: display_strong_bridges(),
        "2": lambda: display_bridges_connecting_scc(),
        "3": lambda: display_airport_connections(),
        "4": lambda: display_list_of_connections(),
        "5": None,
    }

    while display:
        print_menu(
            "1. Strong bridges",
            "2. Bridges connecting strongly connected components",
            "3. Airport connections",
            "4. List of connections",
            "5. Back"
        )

        key = input("Enter option number: ")

        while key not in options:
            key = input("Enter option number: ")

        if options[key] is None:
            display = False
        else:
            options[key]()
