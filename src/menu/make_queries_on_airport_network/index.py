from src.menu.make_queries_on_airport_network.airports.index import display_make_queries_on_airports_menu
from src.menu.make_queries_on_airport_network.airports_connections.index import \
    display_make_queries_on_airport_connections_menu
from src.menu.print_menu import print_menu


def display_make_queries_on_airport_network_menu():
    display = True

    options = {
        "1": lambda: display_make_queries_on_airports_menu(),
        "2": lambda: display_make_queries_on_airport_connections_menu(),
        "3": None,
    }

    while display:
        print_menu(
            "1. Airports",
            "2. Airports connections",
            "3. Back"
        )

        key = input("Enter option number: ")

        while key not in options:
            key = input("Enter option number: ")

        if options[key] is None:
            display = False
        else:
            options[key]()
