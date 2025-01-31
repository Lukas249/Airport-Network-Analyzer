from src.menu.make_queries_on_airport_network.airports.connected.index import display_is_airport_connected_menu
from src.menu.make_queries_on_airport_network.airports.connectivity_of_airports.index import \
    display_connectivity_of_airports_menu
from src.menu.make_queries_on_airport_network.airports.directly_connected.index import \
    display_is_airport_directly_connected_menu
from src.menu.make_queries_on_airport_network.airports.find_shortest_path.index import display_find_shortest_path_menu
from src.menu.make_queries_on_airport_network.airports.highest_connections.index import \
    display_highest_number_of_connections_menu
from src.menu.make_queries_on_airport_network.airports.list.index import display_airports_list
from src.menu.make_queries_on_airport_network.airports.lowest_connections.index import \
    display_lowest_number_of_connections_menu
from src.menu.make_queries_on_airport_network.airports.strongly_connected_components.index import \
    display_strongly_connected_components
from src.menu.print_menu import print_menu


def display_make_queries_on_airports_menu():
    display = True

    options = {
        "1": lambda: display_find_shortest_path_menu(),
        "2": lambda: display_strongly_connected_components(),
        "3": lambda: display_connectivity_of_airports_menu(),
        "4": lambda: display_is_airport_connected_menu(),
        "5": lambda: display_is_airport_directly_connected_menu(),
        "6": lambda: display_lowest_number_of_connections_menu(),
        "7": lambda: display_highest_number_of_connections_menu(),
        "8": lambda: display_airports_list(),
        "9": None,
    }

    while display:
        print_menu(
            "1. Find shortest path",
            "2. Strongly connected components",
            "3. Connectivity of airports",
            "4. Check if two airports are connected",
            "5. Check if two airports are connected directly",
            "6. Airports with lowest connections",
            "7. Airports with highest connections",
            "8. List of airports",
            "9. Back"
        )

        key = input("Enter option number: ")

        while key not in options:
            key = input("Enter option number: ")

        if options[key] is None:
            display = False
        else:
            options[key]()
