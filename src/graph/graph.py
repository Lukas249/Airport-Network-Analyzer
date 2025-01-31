from elegant_heap_queue import HeapQueue, HeapType
from enum import Enum

from src.graph.abstract_airport_connection import AbstractAirportConnection
from src.graph.airport_connection import AirportConnection
from src.graph.airports import Airports
from src.graph.airports_connections import AirportsConnections


class WeightKeys(Enum):
    FLIGHT_DURATION_MINUTES = "flight_duration_minutes"
    FLIGHT_COST_CENTS = "flight_cost_cents"

class AirportGraph:

    def __init__(self, airports: Airports, connections: AirportsConnections):
        self.__airports = airports
        self.__connections = connections

    def shortest_path(self, source: str, destination: str, weight_key: WeightKeys) -> dict[str, any]:
        if not self.__airports.exists(source) or not self.__airports.exists(destination):
            return {}

        min_heap = HeapQueue(heap_type=HeapType.MIN_HEAP)

        airports_connections = self.__connections.get_airports_connections()

        airports_list = list(airports_connections.keys())
        airports_count = len(airports_list)
        airports_dict = { airports_list[v]: v for v in range(airports_count) }

        min_heap.push((0, source, None))

        parents = [None for _ in range(airports_count)]

        visited = set()

        while len(min_heap) != 0:

            airport = min_heap.pop()

            airport_id = airport[1]
            previous_airport_id = airport[2]

            if airport_id in visited:
                continue

            parents[airports_dict.get(airport_id)] = previous_airport_id

            if airport_id == destination:
                path = []

                curr_airport: str|None = destination

                while curr_airport is not None:
                    path.append(curr_airport)
                    curr_airport = parents[airports_dict.get(curr_airport)]

                path.reverse()

                return {
                    weight_key.value: airport[0],
                    "airport_id": airport[1],
                    "path": path
                }

            visited.add(airport_id)

            connected_airports = self.__connections.get_airport_connections(airport_id)

            for connected_airport_id, airport_connection in connected_airports.items():
                min_heap.push((
                    airport[0] + getattr(airport_connection, weight_key.value),
                    connected_airport_id,
                    airport_id
                ))

        return {}

    def critical_connections(self) -> list[AirportConnection]:
        airports_connections = self.__connections.get_airports_connections()

        ssc_before_deletion = self.strongly_connected_components()

        critical_connections = []

        for from_airport_id, connected_airport in airports_connections.items():
            for to_airport_id in connected_airport:
                connection: AirportConnection | None = self.__connections.delete_connection(from_airport_id, to_airport_id)

                scc_after_deletion = self.strongly_connected_components()

                self.__connections.add_connection(connection)

                if scc_after_deletion.get("components_count") > ssc_before_deletion.get("components_count"):
                    critical_connections.append(
                        AirportConnection(
                            from_airport_id,
                            to_airport_id,
                            connection.flight_duration_minutes,
                            connection.flight_cost_cents
                        )
                    )

        return critical_connections

    def connections_between_strongly_connected_components(self) -> AirportsConnections:
        airports_connections = self.__connections.get_airports_connections()

        scc = self.strongly_connected_components().get("components")

        connections = { airport_id: {} for airport_id in self.__airports.get_airports_list() }

        for from_airport_id, connected_airport in airports_connections.items():
            for to_airport_id, connection in connected_airport.items():
                if scc.get(from_airport_id) != scc.get(to_airport_id):
                    connections[from_airport_id][to_airport_id] = connection.clone()

        return AirportsConnections(self.__airports, connections)

    def is_connected(self, source: str, destination: str) -> bool:
        queue = [source]

        visited = {source}

        while len(queue) != 0:

            airport_id = queue.pop()

            if airport_id == destination:
                return True

            connected_airports = self.__connections.get_airport_connections(airport_id)

            for next_airport_id in connected_airports:
                if next_airport_id in visited:
                    continue

                visited.add(next_airport_id)
                queue.append(next_airport_id)

        return False

    def is_directly_connected(self, source: str, destination: str) -> bool:
        return destination in self.__connections.get_airport_connections(source)

    def airport_connections(self, airport_id: str) -> dict[str, AbstractAirportConnection]:
        return self.__connections.get_airport_connections(airport_id)

    def lowest_connections_airports(self) -> list[str]:
        airports_connections = self.__connections.get_airports_connections()

        if len(airports_connections) == 0:
            return []

        airport_ids = []
        lowest_connections = float("inf")

        for airport_id, connected_airports in airports_connections.items():
            count_connections = len(connected_airports)

            if count_connections < lowest_connections:
                lowest_connections = count_connections
                airport_ids = [airport_id]
            elif count_connections == lowest_connections:
                airport_ids.append(airport_id)

        return airport_ids

    def highest_connections_airports(self) -> list[str]:
        airports_connections = self.__connections.get_airports_connections()

        if len(airports_connections) == 0:
            return []

        airport_ids = []
        highest_connections = float("-inf")

        for airport_id, connected_airports in airports_connections.items():
            count_connections = len(connected_airports)

            if count_connections > highest_connections:
                highest_connections = count_connections
                airport_ids = [airport_id]
            elif count_connections == highest_connections:
                airport_ids.append(airport_id)

        return airport_ids

    def connectivity(self) -> dict[str, list[str]]:
        airports_connections = self.__connections.get_airports_connections()

        airports_count = self.__airports.airports_number()

        airports_list = list(airports_connections.keys())
        airports_dict = { airports_list[v]: v for v in range(airports_count) }

        matrix = [[0 for _ in range(airports_count)] for _ in range(airports_count)]

        for from_airport_id in airports_connections:
            id_from = airports_dict.get(from_airport_id)

            for to_airport_id in airports_connections.get(from_airport_id):
                id_to = airports_dict.get(to_airport_id)

                matrix[id_from][id_to] = 1

        for k in range(airports_count):
            for i in range(airports_count):
                for j in range(airports_count):
                    if matrix[i][k] and matrix[k][j]:
                        matrix[i][j] = 1

        connectivity_dict: dict[str, list[str]] = { v: [] for v in airports_list }

        for i in range(airports_count):
            for j in range(airports_count):
                if matrix[i][j]:
                    connectivity_dict[airports_list[i]].append(airports_list[j])

        return connectivity_dict

    def strongly_connected_components(self) -> dict[str,  dict[any, int] | int]:
        airports_connections = self.__connections.get_airports_connections()

        airports_list = list(airports_connections.keys())

        airports_connections_reverted = {}

        for airport_id in airports_list:
            airports_connections_reverted[airport_id] = {}

        for from_airport_id, connected_airport in airports_connections.items():
            for to_airport_id, airport_connection_data in connected_airport.items():
                airports_connections_reverted[to_airport_id][from_airport_id] = airport_connection_data

        visited = set()
        airport_stack = []

        component = []

        def dfs(airport_id):

            connected_airports = airports_connections.get(airport_id).keys()

            visited.add(airport_id)

            for connected_airport in connected_airports:
                if connected_airport in visited:
                    continue

                dfs(connected_airport)

            airport_stack.append(airport_id)

        def dfs2(airport_id):
            connected_airports = airports_connections_reverted.get(airport_id).keys()

            visited.add(airport_id)

            component.append(airport_id)

            for connected_airport in connected_airports:
                if connected_airport in visited:
                    continue

                dfs2(connected_airport)

        for airport_id in airports_list:
            if airport_id in visited:
                continue

            dfs(airport_id)

        airport_stack.reverse()
        visited = set()

        components = {}
        component_id = 0

        for airport_id in airport_stack:
            if airport_id in visited:
                continue

            dfs2(airport_id)

            for airport_id in component:
                components[airport_id] = component_id

            component = []
            component_id += 1

        return { "components": components, "components_count": component_id }