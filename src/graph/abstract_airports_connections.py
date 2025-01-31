from abc import abstractmethod, ABC

from src.graph.abstract_airport_connection import AbstractAirportConnection
from src.graph.abstract_airports import AbstractAirports


class AbstractAirportsConnections(ABC):

    def __init__(self, airports: "AbstractAirports", airports_connections: dict[str, dict[str, AbstractAirportConnection]]):
        self._airports = airports
        self._airports_connections = airports_connections

    @abstractmethod
    def get_airport_connections(self, airport_id: str) -> dict[str, AbstractAirportConnection]:
        pass

    @abstractmethod
    def get_airports_connections(self) -> dict[str, dict[str, AbstractAirportConnection]]:
        pass

    @abstractmethod
    def get_connection_data(self, from_airport: str, to_airport: str) -> AbstractAirportConnection | None:
        pass

    @abstractmethod
    def exists_connection(self, from_airport_id: str, to_airport_id: str) -> bool:
        pass

    @abstractmethod
    def exists_source_airport(self, airport_id: str) -> bool:
        pass

    @abstractmethod
    def add_source_airport(self, airport_id: str) -> bool:
        pass

    @abstractmethod
    def delete_airport(self, airport_id: str):
        pass

    @abstractmethod
    def add_connection(self, connection: AbstractAirportConnection) -> bool:
        pass

    @abstractmethod
    def modify_connection(self, connection: AbstractAirportConnection) -> bool:
        pass

    @abstractmethod
    def delete_connection(self, from_airport_id: str, to_airport_id: str) -> AbstractAirportConnection | None:
        pass

    @abstractmethod
    def to_dict(self) -> dict[str, dict[str, dict[str, int]]]:
        pass