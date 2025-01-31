from abc import ABC, abstractmethod


class AbstractAirportConnection(ABC):

    def __init__(self, from_airport: str, to_airport: str, flight_duration_minutes: int, flight_cost_cents: int):
        self._from_airport = from_airport
        self._to_airport = to_airport
        self._flight_duration_minutes = flight_duration_minutes
        self._flight_cost_cents = flight_cost_cents

    @property
    @abstractmethod
    def from_airport(self) -> str:
       pass

    @property
    @abstractmethod
    def to_airport(self) -> str:
        pass

    @property
    @abstractmethod
    def flight_duration_minutes(self) -> int:
        pass

    @property
    @abstractmethod
    def flight_cost_cents(self) -> int:
        pass

    @abstractmethod
    def get_flight_cost_dollar(self) -> str:
        pass

    @abstractmethod
    def get_flight_duration_hour(self) -> str:
        pass

    @abstractmethod
    def to_dict(self) -> dict[str, int]:
        pass

    @abstractmethod
    def clone(self) -> "AbstractAirportConnection":
        pass