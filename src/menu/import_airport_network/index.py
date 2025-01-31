import os

from src.database.session.index import SessionDB
from src.import_file.json.import_file import ImportJSON
from src.menu.print_menu import print_menu


def display_import_menu():
    display = True

    while display:
        print_menu("1. Back")

        file_path = input("Enter path to file: ")

        if file_path == "1":
            display = False
            continue

        while not os.path.exists(file_path):
            file_path = input("Enter path to file: ")

        try:
            data = ImportJSON.import_file(file_path)
            SessionDB.save("airports", data["airports"])
            SessionDB.save("connections", data["connections"])
            display = False
            print("File successfully imported")
        except:
            print("Error occurred. Make sure entered path follow to a valid JSON file")