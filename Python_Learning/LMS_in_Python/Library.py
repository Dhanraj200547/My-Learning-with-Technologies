from Book import Book
from User import User

class Library():
    
    
    def __init__(self):
        self.bookCount = 0
        self.books = []
        self.users = []
    
    def addBook(self,title,author):
        self.bookCount += 1
        newBook = Book(self.bookCount,title,author)
        self.books.append(newBook)
        print(f"Book added : {title}")
    
    def addUser(self,name):
        newUser = User(len(self.users) , name)
        self.users.append(newUser)
        print(f"User {name} added")
    
    def displaybooks(self):
        print("Library Books : ")
        if not self.books:
            print("No books available")
        else:
            for book in self.books:
                print(f"ID: {book.getId()} | Title: {book.getTitle()} | Author: {book.getAuthor()}")

    def issueBook(self, bookid):
        for book in self.books:
            if book.getId() == bookid:
                book.issueBook()
                return
        print(f"Book id {bookid} not found")
    
    def returnBook(self,bookid):
        for book in self.books:
            if book.getId() == bookid:
                book.returnBook()
                return
        print(f"Bookid {bookid} is not found")
        