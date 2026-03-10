import requests

class PokeApiError(Exception):
    """Base exception for PokeAPI errors."""


class PokeApiClient:

    BASE_URL = "https://pokeapi.co/api/v2"

    # Use a session for connection pooling instead of opening a new connection per request
    def __init__(self, timeout: int = 10):
        self.session = requests.Session()
        self.timeout = timeout

    def get_pokemon(self, identifier: int | str) -> dict:
        """
        Method to query the pokeapi to return a pokemon object given either an id or a name
        """
        url = f"{self.BASE_URL}/pokemon/{identifier}"

        response = self.session.get(url, timeout=self.timeout)

        try: 
            response.raise_for_status()
        except requests.exceptions.HTTPError as exc:
            raise PokeApiError(
                f"Failed to retrieve pokemon '{identifier}' "
                f"(status {response.status_code})"
            ) from exc

        return response.json()

        