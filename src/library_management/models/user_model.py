from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class User(ABC):
    full_name: str
    email: str

    @abstractmethod
    def to_json(self) -> dict:
        pass

    @classmethod
    @abstractmethod
    def from_json(cls, data: dict):
        pass