import pytest
from src.poke_python.api.pokeapi_client import PokeApiClient, PokeApiError

def test_get_pokemon():

    api_client = PokeApiClient()

    response_from_id = api_client.get_pokemon(25)
    assert response_from_id["name"] == "pikachu"

    response_from_name = api_client.get_pokemon("pikachu")
    assert response_from_name["id"] == 25

    with pytest.raises(PokeApiError):
        api_client.get_pokemon(-1)

    with pytest.raises(PokeApiError):
        api_client.get_pokemon("not a pokemon")