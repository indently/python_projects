from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


@dataclass
class Coordinates:
    latitude: float
    longitude: float

    def coordinates(self):
        return self.latitude, self.longitude


def get_coordinates(address: str) -> Coordinates | None:
    """Creates a geolocator that returns coordinates for the given address."""

    geolocator = Nominatim(user_agent="distance_calculator")
    location = geolocator.geocode(address)

    # If there is a location for the address, extract the information
    if location:
        return Coordinates(latitude=location.latitude, longitude=location.longitude)


def calculate_distance_km(home: Coordinates, target: Coordinates) -> float | None:
    """Calculates the distance in km for the home coordinates and the target coordinates."""

    # Make sure we have both the home and the target coordinates
    if home and target:
        distance: float = geodesic(home.coordinates(), target.coordinates()).kilometers
        return distance


def get_distance_km(home: str, target: str) -> float | None:
    """Gets the distance and returns it as a float."""

    # Get coordinates
    home_coordinates: Coordinates = get_coordinates(home)
    target_coordinates: Coordinates = get_coordinates(target)

    # Calculate the distance
    if distance := calculate_distance_km(home_coordinates, target_coordinates):
        print(f'{home} -> {target}')
        print(f'{distance:.2f} kilometres')
        return distance
    else:
        print('Failed to calculate the distance.')


def main():
    # Start address for testing
    home_address: str = 'Helsinkigade 10, Copenhagen 2150, Denmark'
    print(f'Home address: {home_address}')

    # Get the users address and calculate the distance
    target_address: str = input('Enter an address: ')
    print('Calculating...')
    get_distance_km(home_address, target=target_address)


if __name__ == '__main__':
    main()
