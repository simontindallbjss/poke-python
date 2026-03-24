import pytest
from poke_python.models.pokemon import Pokemon, PokemonTypeInfo, PokemonStatInfo
from poke_python.enums import PokemonType, StatName


@pytest.fixture
def pikachu():
    return Pokemon(
        id=25,
        name="pikachu",
        height=4,
        weight=60,
        exp=112,
        types=[
            PokemonTypeInfo(
                slot=1,
                name=PokemonType.ELECTRIC,
                url="https://pokeapi.co/api/v2/type/13/",
            )
        ],
        stats=[
            PokemonStatInfo(
                name=StatName.HP,
                value=35,
                effort=0,
                url="https://pokeapi.co/api/v2/stat/1/",
            ),
            PokemonStatInfo(
                name=StatName.ATTACK,
                value=55,
                effort=0,
                url="https://pokeapi.co/api/v2/stat/2/",
            ),
            PokemonStatInfo(
                name=StatName.DEFENSE,
                value=40,
                effort=0,
                url="https://pokeapi.co/api/v2/stat/3/",
            ),
            PokemonStatInfo(
                name=StatName.SPECIAL_ATTACK,
                value=50,
                effort=0,
                url="https://pokeapi.co/api/v2/stat/4/",
            ),
            PokemonStatInfo(
                name=StatName.SPECIAL_DEFENSE,
                value=50,
                effort=0,
                url="https://pokeapi.co/api/v2/stat/5/",
            ),
            PokemonStatInfo(
                name=StatName.SPEED,
                value=90,
                effort=2,
                url="https://pokeapi.co/api/v2/stat/6/",
            ),
        ],
    )


@pytest.fixture
def zubat():
    return Pokemon(
        id=41,
        name="zubat",
        height=8,
        weight=75,
        exp=49,
        types=[
            PokemonTypeInfo(
                slot=1, name=PokemonType.POISON, url="https://pokeapi.co/api/v2/type/4/"
            ),
            PokemonTypeInfo(
                slot=2, name=PokemonType.FLYING, url="https://pokeapi.co/api/v2/type/3/"
            ),
        ],
        stats=[
            PokemonStatInfo(
                name=StatName.HP,
                value=40,
                effort=0,
                url="https://pokeapi.co/api/v2/stat/1/",
            ),
            PokemonStatInfo(
                name=StatName.ATTACK,
                value=45,
                effort=0,
                url="https://pokeapi.co/api/v2/stat/2/",
            ),
            PokemonStatInfo(
                name=StatName.DEFENSE,
                value=35,
                effort=0,
                url="https://pokeapi.co/api/v2/stat/3/",
            ),
            PokemonStatInfo(
                name=StatName.SPECIAL_ATTACK,
                value=30,
                effort=0,
                url="https://pokeapi.co/api/v2/stat/4/",
            ),
            PokemonStatInfo(
                name=StatName.SPECIAL_DEFENSE,
                value=40,
                effort=0,
                url="https://pokeapi.co/api/v2/stat/5/",
            ),
            PokemonStatInfo(
                name=StatName.SPEED,
                value=55,
                effort=1,
                url="https://pokeapi.co/api/v2/stat/6/",
            ),
        ],
    )
