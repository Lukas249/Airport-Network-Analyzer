from src.graph.airport import Airport
from src.graph.airport_connection import AirportConnection

class ParseJSONData:

    @staticmethod
    def parse_airports(airports_json: dict[str, dict[str, any]]) -> dict[str, Airport]:
        airports: dict[str, Airport] = {}

        for airport_id, airport_data in airports_json.items():
            airport = Airport(
                airport_id,
                airport_data.get("label"),
                airport_data.get("city"),
                airport_data.get("country"),
                airport_data.get("longitude"),
                airport_data.get("latitude")
            )
            airports[airport_id] = airport

        return airports

    @staticmethod
    def parse_connections(connections_json: dict[str, dict[str, dict[str, any]]]) -> dict[str, dict[str, AirportConnection]]:
        airports_connections: dict[str, dict[str, AirportConnection]] = {}

        for airport_id_from, connected_airport in connections_json.items():
            airports_connections[airport_id_from] = {}

            for airport_id_to, connection_data in connected_airport.items():
                airports_connections[airport_id_from][airport_id_to] = AirportConnection(
                    airport_id_from,
                    airport_id_to,
                    connection_data["flight_duration_minutes"],
                    connection_data["flight_cost_cents"]
                )

        return airports_connections