from poke_python.api.pokeapi_client import PokeApiClient
from poke_python.models.pokemon import Pokemon


class PokemonService:
    def __init__(self, client: PokeApiClient):
        self.client = client

    def get_pokemon(self, id: int | str) -> Pokemon:
        data = self.client.get_pokemon(id)
        return Pokemon(**data)
