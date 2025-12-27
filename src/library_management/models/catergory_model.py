from dataclasses import dataclass

@dataclass
class Category:
    category_id: int
    category_name: str

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            category_id=data.get("category_id"),
            category_name=data.get("category_name")
        )
    
    def to_json(self) -> dict:
        return {
            "category_id": self.category_id,
            "category_name": self.category_name
        }