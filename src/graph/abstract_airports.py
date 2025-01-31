from abc import ABC, abstractmethod

from src.graph.abstract_airport import AbstractAirport

class AbstractAirports(ABC):
    def __init__(self, airports: dict[str, "AbstractAirport"]):
        self._airports = airports

    @abstractmethod
    def get_airports_list(self) -> list[str]:
        pass

    @abstractmethod
    def get_airports(self) -> dict[str, "AbstractAirports"]:
        pass

    @abstractmethod
    def get_airport_data(self, airport_id: str) -> AbstractAirport:
        pass

    @abstractmethod
    def airports_number(self) -> int:
        pass

    @abstractmethod
    def exists(self, airport_id: str) -> bool:
        pass

    @abstractmethod
    def add(self, airport: AbstractAirport) -> AbstractAirport|None:
        pass

    @abstractmethod
    def modify(self, airport: AbstractAirport) -> AbstractAirport|None:
        pass

    @abstractmethod
    def delete(self, airport_id: str) -> bool:
        pass

    @abstractmethod
    def to_dict(self) -> dict[str, dict[str, dict[str, str | float]]]:
        pass