from pydantic import Basemodel

class Pokemon(Basemodel):
    id: int
    name: str
    height: int
    weight: int