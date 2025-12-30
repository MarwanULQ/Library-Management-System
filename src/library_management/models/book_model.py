from dataclasses import dataclass, field
from typing import List, Optional
from .author_model import Author
from .catergory_model import Category

@dataclass
class Book:
    book_id: int
    book_name: str
    isbn: Optional[str]
    publication_year: int
    language: str
    cover: Optional[str]
    authors: List[Author]=field(default_factory=list)
    category: List[Category]=field(default_factory=list)

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            book_id=data.get("book_id"),
            book_name=data.get("book_name"),
            isbn=data.get("isbn"),
            publication_year=data.get("publication_year"),
            language=data.get("language"),
            cover=data.get("cover"),
            authors=[Author.from_json(a) for a in data.get("authors", [])],
            category=[Category.from_json(c) for c in data.get("category", [])]
        )
    
    def to_json(self) -> dict:
        return {
            "book_id": self.book_id,
            "book_name": self.book_name,
            "isbn": self.isbn,
            "publication_year": self.publication_year,
            "language": self.language,
            "cover": self.cover,
            "authors": [a.to_json() for a in self.authors],
            "category": [c.to_json() for c in self.category]
        }
