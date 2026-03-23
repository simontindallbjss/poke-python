import pytest
from poke_python.api.pokeapi_client import PokeApiClient, PokeApiError


def test_get_pokemon():
    api_client = PokeApiClient()

    pokemon_from_id = api_client.get_pokemon(25)
    assert pokemon_from_id["name"] == "pikachu"

    pokemon_from_name = api_client.get_pokemon("pikachu")
    assert pokemon_from_name["id"] == 25

    with pytest.raises(PokeApiError):
        api_client.get_pokemon(-1)

    with pytest.raises(PokeApiError):
        api_client.get_pokemon("not a pokemon")
