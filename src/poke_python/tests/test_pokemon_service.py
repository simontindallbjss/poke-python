from poke_python.services.pokemon_service import PokemonService
from poke_python.api.pokeapi_client import PokeApiClient


def test_get_pokemon():
    service = PokemonService(client=PokeApiClient())
    test_pokemon = service.get_pokemon(25)

    assert test_pokemon.id == 25
    assert test_pokemon.name == "pikachu"
    assert len(test_pokemon.types) == 1
    assert len(test_pokemon.stats) == 6

    test_pokemon = service.get_pokemon("zubat")

    assert test_pokemon.id == 41
    assert test_pokemon.name == "zubat"
    assert len(test_pokemon.types) == 2
    assert len(test_pokemon.stats) == 6
