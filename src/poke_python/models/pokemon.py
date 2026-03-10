from __future__ import annotations
from pydantic import BaseModel

class Pokemon(BaseModel):
    id: int
    name: str
    height: int
    weight: int

    @classmethod
    def from_json(cls, json: dict) -> Pokemon:
        return cls(
            id = json["id"],
            name = json["name"],
            height = json["height"],
            weight = json["weight"]
        )