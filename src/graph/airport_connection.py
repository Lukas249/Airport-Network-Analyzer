from src.graph.abstract_airport_connection import AbstractAirportConnection


class AirportConnection(AbstractAirportConnection):

    def __init__(self, from_airport: str, to_airport: str, flight_duration_minutes: int, flight_cost_cents: int):
        super().__init__(from_airport, to_airport, flight_duration_minutes, flight_cost_cents)

    @property
    def from_airport(self) -> str:
        return self._from_airport

    @property
    def to_airport(self) -> str:
        return self._to_airport

    @property
    def flight_duration_minutes(self) -> int:
        return self._flight_duration_minutes

    @property
    def flight_cost_cents(self) -> int:
        return self._flight_cost_cents

    def get_flight_cost_dollar(self) -> str:
        return f"${self.flight_cost_cents / 100}"

    def get_flight_duration_hour(self) -> str:
        hours = str(self.flight_duration_minutes // 60).rjust(2, "0")
        minutes = str(self.flight_duration_minutes % 60).rjust(2, "0")

        return f"{hours}:{minutes}h"

    def to_dict(self) -> dict[str, int]:
        return {
            "flight_duration_minutes": self.flight_duration_minutes,
            "flight_cost_cents": self.flight_cost_cents
        }

    def clone(self) -> "AirportConnection":
        return AirportConnection(self.from_airport, self.to_airport, self.flight_duration_minutes, self.flight_cost_cents)