class Book:
    def __init__(self,title:str,author:str,is_avaiable:bool=True):
        self.title = title
        self.author = author
        self.__is_avaiable = is_avaiable
    
    @property
    def is_avaiable(self):
        return self.__is_avaiable
    
    def borrow(self):
        if not self.__is_avaiable:
            return  f"{self.title} not available"
        else:
            self.__is_avaiable=False
            return f" return {self.title} borrowed successfully"
    
    def return_book(self):
        if  self.__is_avaiable:
            return f"{self.title} already on shelf"
        
        self.__is_avaiable=True
        return  f"{self.title} returned successfully"
    
    
    def display(self):
        return f"Title: {self.title} | Author: {self.author} | Available: {self.__is_avaiable}"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self,book):
        self.books.append(book)
        print (f"{book.title} added to the library")
    
    def find_book(self,title):
        for book in self.books:
            if book.title ==title:
                return book
        return None
    
    def show_all(self):
        for book in self.books:
            print(book.display())
            
            
# test

library = Library()

b1 = Book("Sonar Tori", "Rabindranath Tagore")
b2 = Book("Python Crash Course", "Eric Matthes")
b3 = Book("Clean Code", "Robert Martin")

library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

print("\n--- All Books ---")
library.show_all()

print("\n--- Find Book ---")
found = library.find_book("Sonar Tori")
if found:
    print(found.display())
else:
    print("Book not found")

print("\n--- Borrow ---")
print(b1.borrow())
library.show_all()