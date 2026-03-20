from __future__ import annotations
from pydantic import BaseModel

class Pokemon(BaseModel):
    id: int
    name: str
    height: int
    weight: int
