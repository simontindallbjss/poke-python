from pydantic import BaseModel
from poke_python.enums import PokemonType, StatName


class PokemonTypeInfo(BaseModel):
    slot: int
    name: PokemonType
    url: str


class PokemonStatInfo(BaseModel):
    name: StatName
    value: int
    effort: int
    url: str


class Pokemon(BaseModel):
    id: int
    name: str
    height: int
    weight: int
    types: list[PokemonTypeInfo]
    stats: list[PokemonStatInfo]
