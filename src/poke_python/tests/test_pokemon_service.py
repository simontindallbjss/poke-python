from poke_python.services.pokemon_service import PokemonService
from poke_python.api.pokeapi_client import PokeApiClient


def test_get_pokemon(pikachu, zubat):
    service = PokemonService(client=PokeApiClient())
    pikachu_api = service.get_pokemon(25)
    zubat_api = service.get_pokemon("zubat")

    assert pikachu == pikachu_api
    assert zubat == zubat_api
