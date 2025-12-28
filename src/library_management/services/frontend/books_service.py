from models.book_model import Book
from services.frontend.api_helper import ApiHelper

class BooksService:
    
    @staticmethod
    def get_all_books() -> list[Book]:

        try:
            response = ApiHelper.get("/db/books")
        except Exception as e:
            raise Exception(f"An error occurred while fetching the book: {e}")

        if response.status_code != 200:
            raise Exception(f"Failed to fetch books: {response.json().get('detail')}")

        return [Book.from_json(b) for b in response.json()]
    
    @staticmethod
    def get_book_by_id(book_id: int) -> Book:

        try:
            response = ApiHelper.get(f"/db/books/{book_id}")
        except Exception as e:
            raise Exception(f"An error occurred while fetching the book: {e}")

        if response.status_code != 200:
            raise Exception(f"Failed to fetch books: {response.json().get('detail')}")

        return Book.from_json(response.json())
    
    @staticmethod
    def create_book(book: Book) -> Book:

        try:
            response = ApiHelper.post("/db/books", data=book.to_json())
        except Exception as e:
            raise Exception(f"An error occurred while creating the book: {e}")

        if response.status_code != 200:
            raise Exception(f"Failed to fetch books: {response.json().get('detail')}")

        return Book.from_json(response.json())
    
    @staticmethod
    def search_books(query: str) -> list[Book]:

        try:
            response = ApiHelper.get(f"/db/books/search/all", query_params={"q": query})
        except Exception as e:
            raise Exception(f"An error occurred while searching for books: {e}")

        if response.status_code != 200:
            raise Exception(f"Failed to search books: {response.json().get('detail')}")

        return [Book.from_json(b) for b in response.json()]
    
