from dataclasses import dataclass

@dataclass
class Author:
    author_id: int
    full_name: str

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            author_id=data.get("author_id"),
            full_name=data.get("full_name")
        )
    
    def to_json(self) -> dict:
        return {
            "author_id": self.author_id,
            "full_name": self.full_name
        }