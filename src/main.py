from src.graph.graph import AirportGraph
from src.graph.airports import Airports
from src.graph.airports_connections import AirportsConnections
from src.import_file.json.import_file import ImportJSON
from src.menu.index import display_main_menu

data = ImportJSON.import_file("../data/data.json")

airports: Airports = data["airports"]
connections: AirportsConnections = data["connections"]

airportGraph = AirportGraph(airports, connections)

display_main_menu()



