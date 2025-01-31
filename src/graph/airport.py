from src.graph.abstract_airport import AbstractAirport


class Airport(AbstractAirport):

    def __init__(self, airport_id: str, label: str, city: str, country: str, longitude: float, latitude: float):
        super().__init__(airport_id, label, city, country, longitude, latitude)

    @property
    def airport_id(self) -> str:
        return self._airport_id

    @property
    def label(self) -> str:
        return self._label

    @property
    def city(self) -> str:
        return self._city

    @property
    def country(self) -> str:
        return self._country

    @property
    def longitude(self) -> float:
        return self._longitude

    @property
    def latitude(self) -> float:
        return self._latitude

    def to_dict(self) -> dict[str, str|float]:
        return {
            "label": self.label,
            "city": self.city,
            "country": self.country,
            "longitude": self.longitude,
            "latitude": self.latitude
        }

    def clone(self) -> "Airport":
        return Airport(self.airport_id, self.label, self.city, self.country, self.longitude, self.latitude)