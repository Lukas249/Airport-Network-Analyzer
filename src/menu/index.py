from src.database.session.index import SessionDB
from src.menu.export_airport_network.index import display_export_menu
from src.menu.import_airport_network.index import display_import_menu
from src.menu.make_queries_on_airport_network.index import display_make_queries_on_airport_network_menu
from src.menu.manage_airport_network.index import display_manage_airport_graph_menu
from src.menu.print_menu import print_menu


def display_main_menu():
    menu_options = {
        True: {
            "print_menu": lambda: print_menu(
                "1. Import airport network",
                "2. Manage airport network",
                "3. Make queries on airport network",
                "4. Export airport network",
                "5. Exit"
            ),
            "options": {
                "1": lambda: display_import_menu(),
                "2": lambda: display_manage_airport_graph_menu(),
                "3": lambda: display_make_queries_on_airport_network_menu(),
                "4": lambda: display_export_menu(),
                "5": lambda: exit(1)
            }
        },
        False: {
            "print_menu": lambda: print_menu(
                "1. Import airport network",
                "2. Exit"
            ),
            "options": {
                "1": lambda: display_import_menu(),
                "2": lambda: exit(1)
            },
        }
    }

    while True:
        is_data_imported = SessionDB.contains("airports") and SessionDB.contains("connections")

        selected_menu = menu_options[is_data_imported]

        selected_menu["print_menu"]()
        options = selected_menu["options"]

        key = input("Enter option number: ")

        while key not in options:
            key = input("Enter option number: ")

        options[key]()

