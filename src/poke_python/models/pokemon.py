from pydantic import BaseModel
from poke_python.enums import PokemonType


class PokemonTypeInfo(BaseModel):
    slot: int
    name: PokemonType
    url: str


class Pokemon(BaseModel):
    id: int
    name: str
    height: int
    weight: int
    types: list[PokemonTypeInfo]
