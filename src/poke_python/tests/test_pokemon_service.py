from poke_python.services.pokemon_service import PokemonService
from poke_python.api.pokeapi_client import PokeApiClient


def test_get_pokemon():
    service = PokemonService(client=PokeApiClient())
    test_pokemon = service.get_pokemon(25)

    assert test_pokemon.id == 25
    assert test_pokemon.name == "pikachu"
