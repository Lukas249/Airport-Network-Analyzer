import json

from src.graph.airports import Airports
from src.graph.airports_connections import AirportsConnections
from src.file_handler import FileHandler
from src.parse.json.parse_airports import ParseJSONData


class ImportJSON:

    @staticmethod
    def import_file(filename: str) -> dict[str, Airports|AirportsConnections]:
        json_str = FileHandler.read(filename)

        json_data = json.loads(json_str)

        airports = ParseJSONData.parse_airports(json_data["airports"])
        connections = ParseJSONData.parse_connections(json_data["connections"])

        return {
            "airports": Airports(airports),
            "connections": AirportsConnections(Airports(airports), connections)
        }
