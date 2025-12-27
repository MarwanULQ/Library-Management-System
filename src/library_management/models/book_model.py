from dataclasses import dataclass
from typing import List, Optional
from author_model import Author
from catergory_model import Category

@dataclass
class Book:
    book_id: int
    book_name: str
    isbn: Optional[str]
    publication_year: int
    language: str
    cover: Optional[str]
    authors: List[Author]=[]
    categories: List[Category]=[]

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            book_id=data.get("book_id"),
            book_name=data.get("book_name"),
            isbn=data.get("isbn"),
            publication_year=data.get("publication_year"),
            language=data.get("language"),
            cover=data.get("cover"),
            authors=data.get("authors", []),
            categories=data.get("categories", [])
        )
    
    def to_json(self) -> dict:
        return {
            "book_id": self.book_id,
            "book_name": self.book_name,
            "isbn": self.isbn,
            "publication_year": self.publication_year,
            "language": self.language,
            "cover": self.cover,
            "authors": [author.to_json() for author in self.authors],
            "categories": [category.to_json() for category in self.categories]
        }