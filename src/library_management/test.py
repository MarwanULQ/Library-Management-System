from services.frontend.books_service import BooksService
from models.book_model import Book

x= Book(
    book_id=2,
    book_name="Sample Book",
    isbn="123-d45sf67890123",
    publication_year=2023,
    language="English",
    cover="dfefefefef",
    authors=[],
    category=[]
)
try: 
    y= BooksService.search_books("not")
except Exception as e:
    y= str(e)

print(y)

