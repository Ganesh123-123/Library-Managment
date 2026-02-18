
from library.models import user

# create libraryServices
class libraryservices():
    def __init__(self):
        self.books={}



    #add user
    #remove user


    #add book
    def addBook(self,book_name,author_name):
        #creating object for book class
        new_book_id=len(self.books) + 1
        Book =Book(book_id=new_book_id,
                    title=book_name,
                    author=author_name)

        #adding new book object
        self.books[new_book_id] =book_name
        return f"{book_name} added bookid is {new_book_id}"


    #remove book
    def removeBook(self,bookid:int):
        if bookid in self .books:
            book_obj =self.books[bookid]
            book_obj.is_available =False
            return "book Is Un avaliable
        return "Book id not Found"
    #barrow book
    def barrowBook(self,bookid:int):
        if bookid in self.books:
            #make it book is_avaliable false
            book_obj = self.books[bookid]
            book_obj.is_available = False
            return f"Book barrowed successfully"
        return "Book id not Found"

    #return book
    #get avialable books

