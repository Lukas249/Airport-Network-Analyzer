import json

from src.graph.airports import Airports
from src.graph.airports_connections import AirportsConnections
from src.file_handler import FileHandler

class ExportJSON:

    @staticmethod
    def export(filename: str, airports: Airports, airports_connections: AirportsConnections) -> None:

        json_dict = {
            "airports": airports.to_dict(),
            "connections": airports_connections.to_dict()
        }

        FileHandler.write(filename, json.dumps(json_dict))
