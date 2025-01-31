from abc import ABC, abstractmethod


class AbstractAirport(ABC):

    def __init__(self, airport_id: str, label: str, city: str, country: str, longitude: float, latitude: float):
        self._airport_id = airport_id
        self._label = label
        self._city = city
        self._country = country
        self._longitude = longitude
        self._latitude = latitude

    @property
    @abstractmethod
    def airport_id(self) -> str:
        pass

    @property
    @abstractmethod
    def label(self) -> str:
        pass

    @property
    @abstractmethod
    def city(self) -> str:
        pass

    @property
    @abstractmethod
    def country(self) -> str:
        pass

    @property
    @abstractmethod
    def longitude(self) -> float:
        pass

    @property
    @abstractmethod
    def latitude(self) -> float:
        pass

    @abstractmethod
    def to_dict(self) -> dict[str, str|float]:
        pass

    @abstractmethod
    def clone(self) -> "AbstractAirport":
        pass