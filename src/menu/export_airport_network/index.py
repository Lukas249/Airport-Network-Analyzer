from src.database.session.index import SessionDB
from src.export.json.export import ExportJSON
from src.menu.print_menu import print_menu


def display_export_menu():
    display = True

    while display:
        print_menu("1. Back")

        file_path = input("Enter path to file: ")

        if file_path == "1":
            display = False
            continue

        try:
            ExportJSON.export(file_path, SessionDB.get("airports"), SessionDB.get("connections"))
            display = False
        except:
            print("Error occurred")