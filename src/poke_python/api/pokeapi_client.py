"""
PokeAPI client.

This module contains a simple client for making requests to the PokeAPI.
It handles the HTTP side of things (building URLs, sending requests,
and dealing with errors).

The client returns raw data from the API as dictionaries. It does not
convert the data into application models — that is handled elsewhere
(e.g. in a service layer).

This keeps the client independent from any specific modelling library
(such as Pydantic). If the way data is modelled changes in the future,
this client should not need to change.

Keeping this module focused on HTTP makes the code easier to test,
reuse, and extend.
"""

import requests


class PokeApiError(Exception):
    """Base exception for PokeAPI errors."""


class PokeApiClient:
    """
    A small client for talking to the PokeAPI.

    This class is only responsible for making HTTP requests and returning
    the data from the API.

    It does NOT try to turn the data into Python objects — that should be
    handled elsewhere (e.g. in a service layer).
    """

    BASE_URL = "https://pokeapi.co/api/v2"

    # Use a session for connection pooling instead of opening a new connection per request
    def __init__(self, timeout: int = 10):
        self.session = requests.Session()
        self.timeout = timeout

    def get_pokemon(self, identifier: int | str) -> dict:
        """
        Get Pokémon data from the PokeAPI.

        You can pass either a Pokémon name or ID. The method will call the API
        and return the response as a dictionary.

        The data is returned exactly as the API provides it — no processing or
        validation is done here.

        Args:
            identifier: Pokémon name (e.g. "pikachu") or ID (e.g. 25)

        Returns:
            A dictionary of Pokémon data from the API

        Raises:
            PokeApiError: If the request fails
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
