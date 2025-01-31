from src.graph.airport_connection import AirportConnection
import pydeck as pdk

from src.graph.airports import Airports
from src.graph.airports_connections import AirportsConnections


class GraphVisualizeARC:

    @staticmethod
    def visualize_path(airports: Airports, airports_connections: AirportsConnections, flight_path: list[str]) -> None:
        flights = []

        for i in range(len(flight_path) - 1):
            airport_connection_data = airports_connections.get_connection_data(flight_path[i], flight_path[i + 1])
            flights.append(
                AirportConnection(
                    flight_path[i],
                    flight_path[i + 1],
                    airport_connection_data.flight_duration_minutes,
                    airport_connection_data.flight_cost_cents
                )
            )

        GraphVisualizeARC.visualize(airports, flights)

    @staticmethod
    def visualize_airports_connections(airports: Airports, airports_connections: AirportsConnections) -> None:
        flights = []

        all_airports_connections = airports_connections.get_airports_connections()

        for connected_airports in all_airports_connections.values():
            for airports_connection in connected_airports.values():
                flights.append(airports_connection)

        GraphVisualizeARC.visualize(airports, flights)

    @staticmethod
    def visualize(airports: Airports, flights_list: list[AirportConnection]) -> None:
        flights = []

        for flight in flights_list:
            from_airport_data = airports.get_airport_data(flight.from_airport)
            to_airport_data = airports.get_airport_data(flight.to_airport)

            flights.append({
                    "from_id": from_airport_data.airport_id,
                    "to_id": to_airport_data.airport_id,
                    "from_city": from_airport_data.city,
                    "to_city": to_airport_data.city,
                    "from_country": from_airport_data.country,
                    "to_country": to_airport_data.country,
                    "from": [
                        from_airport_data.longitude,
                        from_airport_data.latitude
                    ],
                    "to": [
                        to_airport_data.longitude,
                        to_airport_data.latitude
                    ],
                    "flight_duration": flight.get_flight_duration_hour(),
                    "flight_cost": flight.get_flight_cost_dollar()
            })

        layer = pdk.Layer(
            "ArcLayer",
            flights,
            getSourcePosition="from",
            getTargetPosition="to",
            getWidth="3",
            getHeight="0.7",
            get_source_color=[0, 255, 255, 150],
            get_target_color=[0, 255, 255, 150],
            pickable=True,
        )

        view_state = pdk.ViewState(latitude=30, longitude=0, zoom=1.5, pitch=30)

        TOOLTIP_TEXT = {
            "html": """({from_id}) {from_city}, {from_country} → ({to_id}) {to_city}, {to_country}</br> 
                            Flight duration: {flight_duration}</br>
                            Flight cost: {flight_cost}"""
        }
        deck = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip=TOOLTIP_TEXT)
        deck.to_html("graph.html", True)

    @staticmethod
    def visualize_connectivity(airports: Airports, flights_list: list[AirportConnection]) -> None:
        flights = []

        for flight in flights_list:
            from_airport_data = airports.get_airport_data(flight.from_airport)
            to_airport_data = airports.get_airport_data(flight.to_airport)

            flights.append({
                "from_id": from_airport_data.airport_id,
                "to_id": to_airport_data.airport_id,
                "from_city": from_airport_data.city,
                "to_city": to_airport_data.city,
                "from_country": from_airport_data.country,
                "to_country": to_airport_data.country,
                "from": [
                    from_airport_data.longitude,
                    from_airport_data.latitude
                ],
                "to": [
                    to_airport_data.longitude,
                    to_airport_data.latitude
                ]
            })

        layer = pdk.Layer(
            "ArcLayer",
            flights,
            getSourcePosition="from",
            getTargetPosition="to",
            getWidth="3",
            getHeight="0.7",
            get_source_color=[0, 255, 255, 150],
            get_target_color=[0, 255, 255, 150],
            pickable=True,
        )

        view_state = pdk.ViewState(latitude=30, longitude=0, zoom=1.5, pitch=30)

        TOOLTIP_TEXT = {
            "html": """({from_id}) {from_city}, {from_country} → ({to_id}) {to_city}, {to_country}"""
        }
        deck = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip=TOOLTIP_TEXT)
        deck.to_html("graph.html", True)