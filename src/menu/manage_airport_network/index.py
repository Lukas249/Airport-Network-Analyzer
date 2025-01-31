from src.menu.manage_airport_network.add.airport import add_airport_menu
from src.menu.manage_airport_network.add.airport_connection import add_airport_connection_menu
from src.menu.manage_airport_network.delete.airport import delete_airport_menu
from src.menu.manage_airport_network.delete.airport_connection import delete_airport_connection_menu
from src.menu.manage_airport_network.modify.airport import modify_airport_menu
from src.menu.manage_airport_network.modify.airport_connection import modify_airport_connection_menu
from src.menu.print_menu import print_menu


def display_manage_airport_graph_menu():
    display = True

    options = {
        "1": lambda: add_airport_menu(),
        "2": lambda: add_airport_connection_menu(),
        "3": lambda: modify_airport_menu(),
        "4": lambda: modify_airport_connection_menu(),
        "5": lambda: delete_airport_menu(),
        "6": lambda: delete_airport_connection_menu(),
        "7": None
    }

    while display:
        print_menu(
            "1. Add airport",
            "2. Add airport connection",
            "3. Modify airport",
            "4. Modify airport connection",
            "5. Delete airport",
            "6. Delete airport connection",
            "7. Back"
        )

        key = input("Enter option number: ")

        while key not in options:
            key = input("Enter option number: ")

        if options[key] is None:
            display = False
        else:
            options[key]()


