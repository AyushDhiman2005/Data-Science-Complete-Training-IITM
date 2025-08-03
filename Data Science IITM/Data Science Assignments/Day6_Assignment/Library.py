class Book():
    def __init__(self,title,author,price):
        self.book_Title = title
        self.book_Author = author
        self.book_Price = price
        self.__availability=True
        print("Book Added to library successfully!")

    def borrow_book(self,person_name):
        if self.__availability==False:
            print(f"{person_name}, The book is not available right now!")
        else:
            print(f"Book is given to {person_name}")
            self.__availability=False
    def return_book(self,person_name):
        print(f"Book is returned successfully by {person_name}")
        self.__availability=True
    def get_book_Info(self):
        print(f"\n{'_'*30}Book Details{'_'*30}\n|Book Title : {self.book_Title}\n|Author Name: {self.book_Author}\n|Price : ${self.book_Price}\n|Availability : {self.__availability}\n|{'_'*72}")

book1=Book('To Kill a monkingbird','Harper Lee',600)
book1.get_book_Info()
book1.borrow_book('John')
book1.borrow_book('Nick')
book1.get_book_Info()
book1.return_book('John')
book1.get_book_Info()
book1.borrow_book('Nick')
book1.get_book_Info()