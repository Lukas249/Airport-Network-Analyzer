import copy

from src.graph.abstract_airport_connection import AbstractAirportConnection
from src.graph.abstract_airports_connections import AbstractAirportsConnections, AbstractAirports

class AirportsConnections(AbstractAirportsConnections):

    def __init__(self, airports: AbstractAirports, airports_connections: dict[str, dict[str, AbstractAirportConnection]]):
        super().__init__(airports, airports_connections)

    def get_airport_connections(self, airport_id: str) -> dict[str, AbstractAirportConnection]:
        if not self.exists_source_airport(airport_id):
            return {}

        return {
            to_airport_id: airport_connection.clone()
            for to_airport_id, airport_connection in self._airports_connections.get(airport_id).items()
        }

    def get_airports_connections(self) -> dict[str, dict[str, AbstractAirportConnection]]:
        return {
            from_airport_id: {
                to_airport_id: connection.clone() for to_airport_id, connection in connected_airports.items()
            } for from_airport_id, connected_airports in self._airports_connections.items()
        }

    def get_connection_data(self, from_airport: str, to_airport: str) -> AbstractAirportConnection | None:
        if not self.exists_connection(from_airport, to_airport):
            return None

        return self.get_airport_connections(from_airport).get(to_airport).clone()

    def exists_connection(self, from_airport_id: str, to_airport_id: str) -> bool:
        connected_airports = self._airports_connections.get(from_airport_id, None)
        return (
                connected_airports is not None and
                connected_airports.get(to_airport_id, None) is not None
        )

    def exists_source_airport(self, airport_id) -> bool:
        return airport_id in self._airports_connections

    def add_source_airport(self, airport_id) -> bool:
        if not self._airports.exists(airport_id) or self.exists_source_airport(airport_id):
            return False

        self._airports_connections[airport_id] = {}

        return True

    def delete_airport(self, airport_id):
        self._airports_connections.pop(airport_id, None)

        to_delete = []

        for from_airport_id, connected_airports in self._airports_connections.items():
            for to_airport_id in connected_airports:
                if to_airport_id == airport_id:
                    to_delete.append([from_airport_id, to_airport_id])

        for from_airport_id, to_airport_id in to_delete:
            self.delete_connection(from_airport_id, to_airport_id)

        return True

    def add_connection(self, connection: AbstractAirportConnection) -> bool:
        if (
                self.exists_connection(connection.from_airport, connection.to_airport) or
                not self._airports.exists(connection.from_airport) or
                not self._airports.exists(connection.to_airport)
        ):
            return False


        if not self.exists_source_airport(connection.from_airport):
            self.add_source_airport(connection.from_airport)

        connected_airports = self._airports_connections.get(connection.from_airport)

        connected_airports[connection.to_airport] = connection

        return True

    def modify_connection(self, connection: AbstractAirportConnection) -> bool:
        if not self.exists_connection(connection.from_airport, connection.to_airport):
            return False

        self._airports_connections[connection.from_airport][connection.to_airport] = connection

        return True


    def delete_connection(self, from_airport_id: str, to_airport_id: str) -> AbstractAirportConnection | None:
        if not self.exists_connection(from_airport_id, to_airport_id):
            return None

        return self._airports_connections[from_airport_id].pop(to_airport_id)

    def to_dict(self) -> dict[str, dict[str, dict[str, int]]]:
        return {
           from_airport_id: {
               to_airport_id: connection_data.to_dict() for to_airport_id, connection_data in connected_airport.items()
           } for from_airport_id, connected_airport in self._airports_connections.items()
        }