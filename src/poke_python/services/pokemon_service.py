from poke_python.api.pokeapi_client import PokeApiClient
from poke_python.models.pokemon import Pokemon, PokemonTypeInfo
from poke_python.enums import PokemonType


class PokemonService:
    def __init__(self, client: PokeApiClient):
        self.client = client

    def get_pokemon(self, id: int | str) -> Pokemon:
        data = self.client.get_pokemon(id)

        pokemon_type_list = [
            PokemonTypeInfo(
                slot=t["slot"],
                name=PokemonType(t["type"]["name"]),
                url=t["type"]["url"],
            )
            for t in data["types"]
        ]

        return Pokemon(
            id=data["id"],
            name=data["name"],
            height=data["height"],
            weight=data["weight"],
            types=pokemon_type_list,
        )
