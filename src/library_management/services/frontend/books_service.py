from models.book_model import Book

class BooksService:
    
    @staticmethod
    def get_all_books() -> list[Book]:
        from services.frontend.api_helper import ApiHelper

        try:
            response = ApiHelper.get("/db/books")
        except Exception as e:
            print(f"An error occurred while fetching books: {e}")
            return []

        if response.status_code != 200:
            print(f"Failed to fetch books: {response.json().get('detail')}")
            return []

        return [Book.from_json(book) for book in response.json()]