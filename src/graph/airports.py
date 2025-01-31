from src.graph.abstract_airport import AbstractAirport
from src.graph.abstract_airports import AbstractAirports


class Airports(AbstractAirports):
    def __init__(self, airports: dict[str, AbstractAirport]):
        super().__init__(airports)

    def get_airports_list(self) -> list[str]:
        return [airport_id for airport_id in self._airports]

    def get_airports(self) -> dict[str, AbstractAirport]:
        return {
           airport_id: airport.clone() for airport_id, airport in self._airports
        }

    def get_airport_data(self, airport_id: str) -> AbstractAirport:
        return self._airports.get(airport_id).clone()

    def airports_number(self) -> int:
        return len(self._airports)

    def exists(self, airport_id: str) -> bool:
        return airport_id in self._airports

    def add(self, airport: AbstractAirport) -> AbstractAirport|None:
        if self.exists(airport.airport_id):
            return None

        self._airports[airport.airport_id] = airport.clone()

        return self._airports[airport.airport_id]

    def modify(self, airport: AbstractAirport) -> AbstractAirport|None:
        if not self.exists(airport.airport_id):
            return None

        self._airports[airport.airport_id] = airport.clone()

        return self._airports[airport.airport_id]

    def delete(self, airport_id: str) -> bool:
        if not self.exists(airport_id):
            return False

        self._airports.pop(airport_id)

        return True

    def to_dict(self) -> dict[str, dict[str, str | float]]:
        return {
            airport_id: airport.to_dict() for airport_id, airport in self._airports.items()
        }