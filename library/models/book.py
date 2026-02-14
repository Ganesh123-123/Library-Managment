class Book:
    def __init__(self, bookid,title,author):
        self.bookid =bookid
        self.title = title
        self.author = author
        self.is_avialable = True

        # git book details
        def book_details(self):
            return f"book name is {self.title} and author name is {self.author}"

        #convert book details to dictionary
        def to_dict(self):
            book = {}
            book["bookid"] = self.id
            book["title"] =self.title
            book['author']=self.author
            book['is_aviailable']=True
            return book